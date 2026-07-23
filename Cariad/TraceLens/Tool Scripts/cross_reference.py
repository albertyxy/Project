# -*- coding: utf-8 -*-
"""
跨信号关联查询工具模块。
给定触发信号和条件，查找触发时刻目标信号的值。
"""

import os
from typing import Dict, List, Optional, Union, Any

import numpy as np

from asammdf import MDF


def cross_reference(
    file_path: str,
    trigger_signal: Optional[str] = None,
    target_signals: Optional[List[str]] = None,
    condition: str = "equals",
    threshold: Optional[float] = None,
    value: Optional[Union[str, float, int]] = None,
    tolerance: float = 1e-6,
    start_time: Optional[float] = None,
    end_time: Optional[float] = None,
    max_points: int = 1,
    triggers: Optional[List[Dict[str, Any]]] = None,
) -> List[Dict[str, Any]]:
    """查找触发信号满足条件的时刻，并返回该时刻各目标信号的值。

    支持两种模式：
    - 单触发：指定 trigger_signal + condition + value/threshold
    - 多触发：指定 triggers 列表，所有条件同时满足时触发

    Args:
        file_path: MF4 文件的路径。
        trigger_signal: 触发信号名称（单触发模式）。
        target_signals: 目标信号名称列表。
        condition: 触发条件类型（单触发模式）。
            - 'equals':  触发信号值 == value
            - 'above':   触发信号值 > threshold
            - 'below':   触发信号值 < threshold
            - 'edge':    触发信号值发生变化
            - 'becomes': 触发信号从其他值跳变进入 value
        threshold: condition 为 'above' 或 'below' 时的阈值。
        value: condition 为 'equals' 或 'becomes' 时的目标值。
        tolerance: 数值型 equals 匹配容差，默认 1e-6。
        start_time: 检索起始时间（秒）。
        end_time: 检索结束时间（秒）。
        max_points: 最多返回的触发点数量，默认 1。
        triggers: 多触发条件列表（多触发模式），每项为：
            {"signal": str, "condition": str, "value": ... 或 "threshold": ...}
            所有条件同时满足时才触发。

    Returns:
        每个触发点为一个字典：
        {"timestamp": float, "triggers": {信号名: 值}, "targets": {信号名: 值}}
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"文件不存在: {file_path}")

    if target_signals is None:
        raise ValueError("target_signals 不能为空")

    if max_points < 1:
        raise ValueError(f"max_points 必须 >= 1，当前值: {max_points}")

    # 多触发模式
    if triggers:
        return _cross_reference_multi(
            file_path, triggers, target_signals,
            start_time, end_time, max_points, tolerance,
        )

    # 单触发模式
    if trigger_signal is None:
        raise ValueError("单触发模式必须指定 trigger_signal，或使用 triggers 参数")

    if condition not in ("equals", "above", "below", "edge", "becomes"):
        raise ValueError(
            f"无效的 condition: '{condition}'，"
            f"可选值为 'equals', 'above', 'below', 'edge', 'becomes'"
        )

    with MDF(file_path) as mdf:
        # 1. 提取触发信号
        if trigger_signal not in mdf.channels_db:
            raise KeyError(f"触发信号 '{trigger_signal}' 在文件中不存在")
        trig = mdf.get(trigger_signal)
        trig_t = trig.timestamps.astype(np.float64)
        trig_s = trig.samples

        # 时间范围裁剪
        if start_time is not None or end_time is not None:
            mask = np.ones(len(trig_t), dtype=bool)
            if start_time is not None:
                mask &= trig_t >= start_time
            if end_time is not None:
                mask &= trig_t <= end_time
            trig_t = trig_t[mask]
            trig_s = trig_s[mask]

        if len(trig_t) == 0:
            return []

        # 2. 在触发信号上查找满足条件的点
        trigger_indices = _find_trigger_points(
            trig_s, condition, threshold, value, tolerance
        )

        if len(trigger_indices) == 0:
            return []

        # 限制数量（均匀采样以覆盖全时间范围）
        if len(trigger_indices) > max_points:
            step = len(trigger_indices) / max_points
            sampled = []
            for i in range(max_points):
                idx = int(i * step)
                if idx < len(trigger_indices):
                    sampled.append(trigger_indices[idx])
            trigger_indices = np.array(sampled)

        trigger_times = trig_t[trigger_indices]
        trigger_values = trig_s[trigger_indices]

        # 3. 提取所有目标信号
        target_data: Dict[str, tuple] = {}
        for name in target_signals:
            if name not in mdf.channels_db:
                raise KeyError(f"目标信号 '{name}' 在文件中不存在")
            sig = mdf.get(name)
            target_data[name] = (
                sig.timestamps.astype(np.float64),
                sig.samples,
            )

    # 4. 在每个触发时刻查询目标信号值
    results: List[Dict[str, Any]] = []
    for i, t in enumerate(trigger_times):
        entry: Dict[str, Any] = {
            "timestamp": float(t),
            "triggers": {trigger_signal: _safe_value(trigger_values[i])},
            "targets": {},
        }
        for name, (t_arr, s_arr) in target_data.items():
            idx = np.argmin(np.abs(t_arr - t))
            entry["targets"][name] = _safe_value(s_arr[idx])
        results.append(entry)

    return results


def _find_trigger_points(
    samples: np.ndarray,
    condition: str,
    threshold: Optional[float],
    value: Optional[Union[str, float, int]],
    tolerance: float,
) -> np.ndarray:
    """查找触发信号中满足条件的采样点索引。"""
    is_numeric = np.issubdtype(samples.dtype, np.number)

    if condition == "equals":
        if value is None:
            raise ValueError("condition='equals' 时必须指定 value 参数")
        if is_numeric:
            mask = np.abs(samples - float(value)) <= tolerance
        else:
            target = value.decode("utf-8") if isinstance(value, bytes) else str(value)
            mask = np.array([
                (s.decode("utf-8") if isinstance(s, bytes) else str(s)) == target
                for s in samples
            ])

    elif condition == "above":
        if not is_numeric:
            raise ValueError("condition='above' 仅适用于数值型信号")
        if threshold is None:
            raise ValueError("condition='above' 时必须指定 threshold 参数")
        mask = samples > threshold

    elif condition == "below":
        if not is_numeric:
            raise ValueError("condition='below' 仅适用于数值型信号")
        if threshold is None:
            raise ValueError("condition='below' 时必须指定 threshold 参数")
        mask = samples < threshold

    elif condition == "edge":
        # 值发生变化的点（适用于枚举型）
        if is_numeric:
            mask = np.concatenate([[False], np.diff(samples) != 0])
        else:
            mask = np.concatenate([[False], samples[:-1] != samples[1:]])

    elif condition == "becomes":
        # 从其他值跳变进入目标值的时刻（非稳态保持期间）
        if value is None:
            raise ValueError("condition='becomes' 时必须指定 value 参数")
        if is_numeric:
            target = float(value)
            curr_match = np.abs(samples - target) <= tolerance
        else:
            target = value.decode("utf-8") if isinstance(value, bytes) else str(value)
            curr_match = np.array([
                (s.decode("utf-8") if isinstance(s, bytes) else str(s)) == target
                for s in samples
            ])
        # 当前匹配 且 前一采样点不匹配 → 跳变进入
        prev_match = np.concatenate([[False], curr_match[:-1]])
        mask = curr_match & ~prev_match

    return np.where(mask)[0]


def _cross_reference_multi(
    file_path: str,
    triggers: List[Dict[str, Any]],
    target_signals: List[str],
    start_time: Optional[float],
    end_time: Optional[float],
    max_points: int,
    tolerance: float,
) -> List[Dict[str, Any]]:
    """多触发模式：所有触发条件同时满足的时刻。"""
    with MDF(file_path) as mdf:
        # 1. 提取所有涉及信号
        trigger_signals = [t["signal"] for t in triggers]
        all_signals = list(dict.fromkeys(trigger_signals + target_signals))

        all_data: Dict[str, tuple] = {}
        for name in all_signals:
            if name not in mdf.channels_db:
                raise KeyError(f"信号 '{name}' 在文件中不存在")
            sig = mdf.get(name)
            all_data[name] = (
                sig.timestamps.astype(np.float64),
                sig.samples,
            )

    # 2. 用第一个目标信号的时间轴作为公共时间线
    target_t = all_data[target_signals[0]][0]
    if start_time is not None:
        target_t = target_t[target_t >= start_time]
    if end_time is not None:
        target_t = target_t[target_t <= end_time]
    if len(target_t) == 0:
        return []

    # 3. 对每个触发条件，在公共时间线上计算掩码（最近邻，与结果显示一致）
    combined_mask = np.ones(len(target_t), dtype=bool)
    # 保存各触发信号在命中时间点的插值索引，用于结果显示
    trig_indices_at_hit: Dict[str, np.ndarray] = {}
    for trig in triggers:
        t_arr, s_arr = all_data[trig["signal"]]
        cond = trig.get("condition", "equals")
        val = trig.get("value")
        thr = trig.get("threshold")

        # 对 target_t 每个点找触发信号最近采样点
        indices = np.searchsorted(t_arr, target_t, side="left")
        indices = np.clip(indices, 1, len(t_arr) - 1)
        # 比较左右邻居，取更近的
        left_idx = indices - 1
        left_dist = np.abs(target_t - t_arr[left_idx])
        right_dist = np.abs(target_t - t_arr[indices])
        best_idx = np.where(left_dist <= right_dist, left_idx, indices)
        trig_indices_at_hit[trig["signal"]] = best_idx

        interp_samples = s_arr[best_idx]
        mask = _compute_condition_mask(interp_samples, cond, val, thr, tolerance)
        combined_mask &= mask

    # 4. 找到第一个满足所有条件的时间点
    hit_indices = np.where(combined_mask)[0]
    if len(hit_indices) == 0:
        return []

    hit_indices = hit_indices[:max_points]
    hit_times = target_t[hit_indices]

    # 5. 查询触发信号值（复用步骤3的最近邻索引，与条件判定一致）
    results: List[Dict[str, Any]] = []
    for i, t in enumerate(hit_times):
        ti = hit_indices[i]  # 在 target_t 中的索引
        trigger_vals = {}
        for trig in triggers:
            idx = trig_indices_at_hit[trig["signal"]][ti]
            _, s_arr = all_data[trig["signal"]]
            trigger_vals[trig["signal"]] = _safe_value(s_arr[idx])

        entry: Dict[str, Any] = {
            "timestamp": float(t),
            "triggers": trigger_vals,
            "targets": {},
        }
        for name in target_signals:
            t_arr, s_arr = all_data[name]
            idx = np.argmin(np.abs(t_arr - t))
            entry["targets"][name] = _safe_value(s_arr[idx])
        results.append(entry)

    return results


def _compute_condition_mask(
    samples: np.ndarray,
    condition: str,
    value: Optional[Union[str, float, int]],
    threshold: Optional[float],
    tolerance: float,
) -> np.ndarray:
    """对插值后的采样值计算条件掩码。"""
    is_numeric = np.issubdtype(samples.dtype, np.number)

    if condition == "equals":
        if is_numeric:
            return np.abs(samples - float(value)) <= tolerance
        else:
            target = value.decode("utf-8") if isinstance(value, bytes) else str(value)
            return np.array([
                (s.decode("utf-8") if isinstance(s, bytes) else str(s)) == target
                for s in samples
            ])
    elif condition == "above":
        return samples > threshold
    elif condition == "below":
        return samples < threshold
    elif condition == "edge":
        if is_numeric:
            return np.concatenate([[False], np.diff(samples) != 0])
        else:
            return np.concatenate([[False], samples[:-1] != samples[1:]])
    elif condition == "becomes":
        if is_numeric:
            curr = np.abs(samples - float(value)) <= tolerance
        else:
            target = value.decode("utf-8") if isinstance(value, bytes) else str(value)
            curr = np.array([
                (s.decode("utf-8") if isinstance(s, bytes) else str(s)) == target
                for s in samples
            ])
        prev = np.concatenate([[False], curr[:-1]])
        return curr & ~prev
    return np.zeros(len(samples), dtype=bool)


def _safe_value(val) -> Union[float, str, None]:
    """将 numpy 值转为 Python 原生类型。"""
    if val is None:
        return None
    if isinstance(val, (np.floating,)):
        if np.isnan(val):
            return None
        return float(val)
    if isinstance(val, (np.integer,)):
        return int(val)
    if isinstance(val, bytes):
        return val.decode("utf-8")
    if isinstance(val, np.ndarray):
        return _safe_value(val.item()) if val.size == 1 else str(val)
    return val
