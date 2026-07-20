# -*- coding: utf-8 -*-
"""
多信号曲线绘制工具模块。
支持两种模式：
  - overlay: 所有信号叠加在一张图上，主信号突出（左 Y 轴），其余弱化
  - split:   各信号在同一张图上垂直拆分，互不重叠，共用一条左 Y 轴
自动处理枚举型信号（转换为编码并标注原始值）。
"""

import os
from typing import Dict, Tuple, Optional, List

import matplotlib
matplotlib.use("Agg")  # 非交互后端，避免 GUI 依赖
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# 配置中文字体（Windows 使用微软雅黑）
_font_candidates = ["Microsoft YaHei", "SimHei", "WenQuanYi Micro Hei"]
_available = {f.name for f in fm.fontManager.ttflist}
_cjk_font = next((f for f in _font_candidates if f in _available), None)
if _cjk_font:
    plt.rcParams["font.sans-serif"] = [_cjk_font, "DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False


def _normalize_enum(samples: np.ndarray) -> Tuple[np.ndarray, Optional[List[str]]]:
    """若为非数值型数组，转换为整数编码并返回标签列表。"""
    if np.issubdtype(samples.dtype, np.number):
        return samples, None

    unique_vals = []
    for v in samples:
        if v not in unique_vals:
            unique_vals.append(v)
    val_to_code = {v: i for i, v in enumerate(unique_vals)}
    codes = np.array([val_to_code[v] for v in samples])
    labels = [
        v.decode() if isinstance(v, bytes) else str(v)
        for v in unique_vals
    ]
    return codes, labels


def plot_signals(
    data_dict: Dict[str, Tuple[np.ndarray, np.ndarray]],
    title: str,
    output_path: str,
    primary_signal: Optional[str] = None,
    mode: str = "overlay",
) -> str:
    """绘制多个信号曲线并保存为图片。

    自动处理数值型和枚举型信号，枚举型信号会转换为编码并标注原始值。

    Args:
        data_dict: 信号数据字典，格式为 {'信号名': (时间戳数组, 数值数组)}。
        title: 图表标题。
        output_path: 图片保存路径。
        primary_signal: 主信号名称。若为 None，取 data_dict 中第一个信号。
        mode: 显示模式。
            - 'overlay': 所有信号叠加在一张图上。
            - 'split':   各信号垂直拆分在同一张图上，互不重叠。

    Returns:
        保存的图片文件的绝对路径。
    """
    if not data_dict:
        raise ValueError("data_dict 不能为空，请至少提供一个信号数据。")
    if mode not in ("overlay", "split"):
        raise ValueError(f"无效的 mode: '{mode}'，可选值为 'overlay', 'split'")

    if primary_signal is None:
        primary_signal = next(iter(data_dict.keys()))
    elif primary_signal not in data_dict:
        raise ValueError(
            f"主信号 '{primary_signal}' 不在 data_dict 中。"
            f"可用信号: {', '.join(data_dict.keys())}"
        )

    ordered_names = [primary_signal] + [
        n for n in data_dict if n != primary_signal
    ]

    # 验证并标准化数据（枚举型转编码）
    normalized: Dict[str, Tuple[np.ndarray, np.ndarray, Optional[List[str]]]] = {}
    for name in ordered_names:
        t_arr, s_arr = data_dict[name]
        if len(t_arr) != len(s_arr):
            raise ValueError(
                f"信号 '{name}' 的时间戳和采样值长度不一致: "
                f"{len(t_arr)} vs {len(s_arr)}"
            )
        if len(t_arr) == 0:
            raise ValueError(f"信号 '{name}' 的数据为空。")
        codes, labels = _normalize_enum(s_arr)
        normalized[name] = (t_arr, codes, labels)

    output_dir = os.path.dirname(os.path.abspath(output_path))
    if output_dir and not os.path.isdir(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    if mode == "overlay":
        _plot_overlay(normalized, ordered_names, title, output_path)
    else:
        _plot_split(normalized, ordered_names, title, output_path)

    return os.path.abspath(output_path)


def _plot_overlay(normalized, ordered_names, title, output_path):
    """叠加模式：所有曲线在同一张图上，主信号突出。"""
    fig, ax_primary = plt.subplots(figsize=(12, 6))
    colors = plt.cm.tab10.colors
    lines = []
    labels = []

    for i, name in enumerate(ordered_names):
        t_arr, s_arr, enum_labels = normalized[name]
        is_primary = (i == 0)
        color = colors[i % len(colors)]

        if is_primary:
            ax = ax_primary
            lw, alpha_val = 2.0, 1.0
        else:
            ax = ax_primary.twinx()
            offset = 60 * (i - 1)
            ax.spines["right"].set_position(("outward", offset))
            lw, alpha_val = 0.7, 0.45

        line = ax.plot(
            t_arr, s_arr, linewidth=lw, color=color, alpha=alpha_val, label=name
        )[0]
        lines.append(line)
        labels.append(name)

        if is_primary:
            if enum_labels:
                ax.set_yticks(range(len(enum_labels)))
                ax.set_yticklabels(enum_labels, fontsize=8)
            ax.set_ylabel(name, color=color)
            ax.tick_params(axis="y", labelcolor=color, labelsize=10)
        else:
            ax.set_yticks([])
            ax.spines["right"].set_visible(False)

    ax_primary.set_xlabel("时间 (s)")
    ax_primary.set_title(title)
    fig.legend(lines, labels, loc="upper right")
    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def _nice_ticks(vmin, vmax, max_count=4):
    """在 [vmin, vmax] 范围内生成尽量整数的刻度值。"""
    import math
    if vmin == vmax:
        return [vmin]
    span = vmax - vmin
    # 估算合适的步长
    raw_step = span / (max_count - 1)
    # 取最近的"漂亮"步长：1, 2, 5, 10, 20, 50, ... 及其小数倍数
    exp = math.floor(math.log10(raw_step)) if raw_step > 0 else 0
    base = 10 ** exp
    candidates = [base, 2 * base, 5 * base]
    step = min(candidates, key=lambda c: abs(c - raw_step))
    # 从 vmin 向上取整到 step 的倍数
    first = math.ceil(vmin / step) * step
    ticks = []
    while first <= vmax + step * 0.001:
        ticks.append(first)
        first += step
    # 限制数量
    if len(ticks) > max_count + 1:
        step = step * 2
        first = math.ceil(vmin / step) * step
        ticks = []
        while first <= vmax + step * 0.001:
            ticks.append(first)
            first += step
    # 决定小数位数
    if isinstance(step, int) and step >= 1:
        fmt = "{:.0f}"
    elif step >= 0.01:
        decimals = max(0, -math.floor(math.log10(step)) + 1)
        fmt = f"{{:.{decimals}f}}"
    else:
        fmt = "{:.4f}"
    return ticks, fmt


def _plot_split(normalized, ordered_names, title, output_path):
    """拆分模式：同一张图上垂直拆分各信号，互不重叠，共用一条左 Y 轴脊柱。"""
    n = len(ordered_names)
    colors = plt.cm.tab10.colors
    lane_h = 1.0
    total_h = n * lane_h
    pad = 0.12
    scale = 0.76

    fig, ax = plt.subplots(figsize=(14, 1.8 * n + 0.6))
    lines_list = []
    label_list = []
    all_tick_pos = []
    all_tick_labels = []

    for i, name in enumerate(ordered_names):
        t_arr, s_arr_orig, enum_labels = normalized[name]
        is_primary = (i == 0)
        color = colors[i % len(colors)]
        lw = 2.0 if is_primary else 0.7
        alpha_val = 1.0 if is_primary else 0.6

        lane_bottom = (n - 1 - i) * lane_h
        s_min, s_max = float(s_arr_orig.min()), float(s_arr_orig.max())
        if s_min == s_max:
            s_max = s_min + 1

        s_norm = (s_arr_orig - s_min) / (s_max - s_min)
        s_plot = lane_bottom + pad + s_norm * scale

        line = ax.plot(
            t_arr, s_plot, linewidth=lw, color=color, alpha=alpha_val, label=name
        )[0]
        lines_list.append(line)
        label_list.append(name)

        # 该 lane 的刻度
        lane_center = lane_bottom + pad + scale / 2
        if enum_labels:
            for j, lbl in enumerate(enum_labels):
                tpos = (lane_bottom + pad
                        + j / (len(enum_labels) - 1) * scale
                        if len(enum_labels) > 1
                        else lane_center)
                all_tick_pos.append(tpos)
                all_tick_labels.append(lbl)
        else:
            tick_vals, fmt = _nice_ticks(s_min, s_max, max_count=5)
            for v in tick_vals:
                tpos = lane_bottom + pad + (v - s_min) / (s_max - s_min) * scale
                all_tick_pos.append(tpos)
                all_tick_labels.append(fmt.format(v))

    ax.set_yticks(all_tick_pos)
    ax.set_yticklabels(all_tick_labels, fontsize=7)
    ax.set_ylim(0, total_h)

    # lane 分隔线
    for i in range(1, n):
        ax.axhline(y=i * lane_h, color="gray", linestyle="--", alpha=0.3, linewidth=0.5)

    ax.set_xlabel("时间 (s)")
    ax.set_title(title, fontsize=11)
    ax.tick_params(axis="y", labelsize=7)
    ax.spines["top"].set_visible(False)

    fig.legend(lines_list, label_list, loc="upper right", fontsize=8)
    fig.subplots_adjust(left=0.10, right=0.85, top=0.94, bottom=0.08)
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
