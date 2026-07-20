# -*- coding: utf-8 -*-
"""
信号边沿检测与窗口数据提取工具模块。
"""

from typing import Dict, List

import numpy as np


def extract_around_edges(
    timestamps: np.ndarray,
    samples: np.ndarray,
    edge_type: str = "rising",
    window_before: float = 1.0,
    window_after: float = 2.0,
    min_amplitude: float = 0.5,
    max_edges: int = 10,
) -> List[Dict]:
    """检测信号边沿，并提取每个边沿前后指定窗口的数据段。

    边沿检测基于相邻采样值之间的差分幅值：
    - 上升沿: samples[i+1] - samples[i] >= min_amplitude
    - 下降沿: samples[i] - samples[i+1] >= min_amplitude
    - 所有跳变 (both): |samples[i+1] - samples[i]| >= min_amplitude

    边沿时刻定义为跳变后第一个采样点的时间戳。

    Args:
        timestamps: 一维时间戳数组（秒），长度 N。
        samples: 一维信号采样值数组，长度 N，与 timestamps 等长。
        edge_type: 边沿类型。
            - 'rising':  仅检测上升沿。
            - 'falling': 仅检测下降沿。
            - 'both':    检测所有跳变（上升 + 下降）。
        window_before: 边沿时刻之前截取的时间窗口长度（秒）。
        window_after:  边沿时刻之后截取的时间窗口长度（秒）。
        min_amplitude: 最小跳变幅度阈值，用于滤除噪声。
        max_edges:     最多返回的边沿数量。

    Returns:
        一个列表，每个元素是一个字典，包含以下键：
        - 'edge_index':    int, 边沿在原始数组中的索引位置。
        - 'edge_time':     float, 边沿时刻（秒）。
        - 'edge_timestamps': np.ndarray, 边沿前后窗口内的时间戳。
        - 'edge_samples':    np.ndarray, 边沿前后窗口内的信号采样值。

    Raises:
        ValueError: 当输入参数无效时。
    """
    if len(timestamps) != len(samples):
        raise ValueError(
            f"timestamps 和 samples 长度不一致: "
            f"{len(timestamps)} vs {len(samples)}"
        )

    if len(timestamps) < 2:
        return []

    if edge_type not in ("rising", "falling", "both"):
        raise ValueError(
            f"无效的 edge_type: '{edge_type}'，"
            f"可选值为 'rising', 'falling', 'both'"
        )

    if window_before < 0 or window_after < 0:
        raise ValueError("window_before 和 window_after 必须为非负数")

    if max_edges < 1:
        raise ValueError(f"max_edges 必须 >= 1，当前值: {max_edges}")

    # 判断是否为数值型信号
    is_numeric = np.issubdtype(samples.dtype, np.number)

    if is_numeric:
        if min_amplitude <= 0:
            raise ValueError(
                f"min_amplitude 必须大于 0，当前值: {min_amplitude}"
            )
        diffs = np.diff(samples)
        if edge_type == "rising":
            edge_indices = np.where(diffs >= min_amplitude)[0] + 1
        elif edge_type == "falling":
            edge_indices = np.where(diffs <= -min_amplitude)[0] + 1
        else:
            edge_indices = np.where(np.abs(diffs) >= min_amplitude)[0] + 1
    else:
        # 枚举/字符串信号：值发生变化即视为边沿
        edge_indices = np.where(samples[:-1] != samples[1:])[0] + 1

    if len(edge_indices) == 0:
        return []

    # 限制边沿数量
    edge_indices = edge_indices[:max_edges]

    results: List[Dict] = []
    for idx in edge_indices:
        idx = int(idx)
        edge_time = float(timestamps[idx])

        # 确定窗口在时间轴上的范围
        t_start = edge_time - window_before
        t_end = edge_time + window_after

        # 选出落在窗口内的采样点
        mask = (timestamps >= t_start) & (timestamps <= t_end)
        window_t = timestamps[mask]
        window_s = samples[mask]

        results.append({
            "edge_index": idx,
            "edge_time": edge_time,
            "edge_timestamps": window_t,
            "edge_samples": window_s,
        })

    return results
