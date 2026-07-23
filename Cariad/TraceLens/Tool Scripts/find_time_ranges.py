# -*- coding: utf-8 -*-
"""
按条件查找信号满足指定阈值/状态的时间窗口。
支持数值型信号的阈值判断和枚举型信号的状态匹配。
"""

from typing import List, Tuple, Optional, Union

import numpy as np


def find_time_ranges(
    timestamps: np.ndarray,
    samples: np.ndarray,
    condition: str = "above",
    threshold: Optional[float] = None,
    lower: Optional[float] = None,
    upper: Optional[float] = None,
    value: Optional[Union[str, float, int]] = None,
    tolerance: float = 1e-6,
    min_duration: float = 0.0,
    merge_gap: float = 0.0,
) -> List[Tuple[float, float]]:
    """在信号数据中查找满足条件的所有连续时间窗口。

    根据 condition 类型对采样值逐点判定，将连续满足条件的采样点
    合并为时间区间。支持合并近距离窗口和过滤过短窗口。

    Args:
        timestamps: 一维时间戳数组（秒），长度 N。
        samples: 一维信号采样值数组，长度 N，与 timestamps 等长。
        condition: 判定条件类型。
            - 'above':  采样值 > threshold（仅数值型信号）
            - 'below':  采样值 < threshold（仅数值型信号）
            - 'equals': 采样值 == value（数值型用 tolerance 容差，枚举型精确匹配）
            - 'between': lower < 采样值 < upper（仅数值型信号）
        threshold: condition 为 'above' 或 'below' 时的阈值。
        lower: condition 为 'between' 时的下界。
        upper: condition 为 'between' 时的上界。
        value: condition 为 'equals' 时的目标值（数值或字符串）。
        tolerance: condition 为 'equals' 且信号为数值型时的容差，默认 1e-6。
        min_duration: 最小窗口持续时间（秒），短于此值的窗口将被过滤。默认 0（不过滤）。
        merge_gap: 相邻窗口合并阈值（秒），间距小于此值的两个窗口将合并为一个。默认 0（不合并）。

    Returns:
        满足条件的时间窗口列表，每个元素为 (start_time, end_time) 元组，
        按时间升序排列。若无满足条件的窗口则返回空列表。

    Raises:
        ValueError: 当参数无效或 condition 与信号类型不匹配时。
    """
    # 参数校验
    if len(timestamps) != len(samples):
        raise ValueError(
            f"timestamps 和 samples 长度不一致: "
            f"{len(timestamps)} vs {len(samples)}"
        )

    if len(timestamps) == 0:
        return []

    if min_duration < 0:
        raise ValueError(f"min_duration 必须 >= 0，当前值: {min_duration}")

    if merge_gap < 0:
        raise ValueError(f"merge_gap 必须 >= 0，当前值: {merge_gap}")

    if condition not in ("above", "below", "equals", "between"):
        raise ValueError(
            f"无效的 condition: '{condition}'，"
            f"可选值为 'above', 'below', 'equals', 'between'"
        )

    is_numeric = np.issubdtype(samples.dtype, np.number)

    # 根据条件生成布尔掩码
    if condition == "above":
        if not is_numeric:
            raise ValueError(
                f"condition='above' 仅适用于数值型信号，"
                f"当前信号类型为 {samples.dtype}"
            )
        if threshold is None:
            raise ValueError("condition='above' 时必须指定 threshold 参数")
        mask = samples > threshold

    elif condition == "below":
        if not is_numeric:
            raise ValueError(
                f"condition='below' 仅适用于数值型信号，"
                f"当前信号类型为 {samples.dtype}"
            )
        if threshold is None:
            raise ValueError("condition='below' 时必须指定 threshold 参数")
        mask = samples < threshold

    elif condition == "equals":
        if value is None:
            raise ValueError("condition='equals' 时必须指定 value 参数")
        if is_numeric:
            mask = np.abs(samples - float(value)) <= tolerance
        else:
            # 枚举型信号：精确字符串匹配
            # numpy.bytes_ 需要 decode 后才能与字符串比较
            if isinstance(value, (int, float)):
                value = str(value)
            target = str(value)
            mask = np.array([
                (s.decode("utf-8") if isinstance(s, bytes) else str(s)) == target
                for s in samples
            ])

    elif condition == "between":
        if not is_numeric:
            raise ValueError(
                f"condition='between' 仅适用于数值型信号，"
                f"当前信号类型为 {samples.dtype}"
            )
        if lower is None or upper is None:
            raise ValueError("condition='between' 时必须指定 lower 和 upper 参数")
        if lower >= upper:
            raise ValueError(
                f"lower 必须小于 upper，当前值: lower={lower}, upper={upper}"
            )
        mask = (samples > lower) & (samples < upper)

    # 从掩码中提取连续 True 的区间
    raw_intervals = _mask_to_intervals(timestamps, mask)

    if not raw_intervals:
        return []

    # 合并近距离窗口
    if merge_gap > 0:
        merged = _merge_nearby_intervals(raw_intervals, merge_gap)
    else:
        merged = raw_intervals

    # 过滤过短窗口
    if min_duration > 0:
        filtered = [
            (start, end)
            for start, end in merged
            if (end - start) >= min_duration
        ]
    else:
        filtered = merged

    return filtered


def _mask_to_intervals(
    timestamps: np.ndarray, mask: np.ndarray
) -> List[Tuple[float, float]]:
    """从布尔掩码中提取连续 True 区间对应的时间范围。

    每个连续的 True 段，取该段第一个采样点的时间为 start_time，
    最后一个采样点的时间为 end_time。
    """
    if not np.any(mask):
        return []

    # 找到掩码变化的位置（True/False 切换点）
    padded = np.concatenate([[False], mask, [False]])
    # 上升沿：False → True，对应区间的起始索引
    starts = np.where(padded[1:] & ~padded[:-1])[0]
    # 下降沿：True → False，对应区间的结束索引（包含）
    ends = np.where(~padded[1:] & padded[:-1])[0] - 1

    intervals = []
    for s, e in zip(starts, ends):
        # 确保索引在有效范围内
        s = max(0, int(s))
        e = min(len(timestamps) - 1, int(e))
        intervals.append((float(timestamps[s]), float(timestamps[e])))

    return intervals


def _merge_nearby_intervals(
    intervals: List[Tuple[float, float]], max_gap: float
) -> List[Tuple[float, float]]:
    """合并间距小于 max_gap 的相邻时间窗口。"""
    if not intervals:
        return []

    merged = [intervals[0]]
    for current_start, current_end in intervals[1:]:
        prev_start, prev_end = merged[-1]
        if current_start - prev_end <= max_gap:
            # 合并：延长前一个窗口的结束时间
            merged[-1] = (prev_start, max(prev_end, current_end))
        else:
            merged.append((current_start, current_end))

    return merged
