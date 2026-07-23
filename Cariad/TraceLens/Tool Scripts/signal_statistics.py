# -*- coding: utf-8 -*-
"""
信号统计摘要工具模块。
计算信号的各项统计指标，自动适配数值型和枚举型信号。
"""

from typing import Dict, Any, List, Tuple, Optional

import numpy as np


def signal_statistics(
    timestamps: np.ndarray,
    samples: np.ndarray,
    percentiles: Optional[List[float]] = None,
) -> Dict[str, Any]:
    """计算信号的统计摘要信息。

    对数值型信号计算均值、标准差、最值、RMS 等指标；
    对枚举型信号统计值分布和最频繁状态。

    Args:
        timestamps: 一维时间戳数组（秒），长度 N。
        samples: 一维信号采样值数组，长度 N，与 timestamps 等长。
        percentiles: 可选的分位数列表（仅数值型信号生效），
            例如 [1, 5, 95, 99] 输出 P1, P5, P95, P99。
            默认不计算分位数。

    Returns:
        统计结果字典。数值型信号包含以下键：
            - count (int): 采样点数量
            - duration (float): 信号总时长（秒）
            - start_time (float): 起始时间（秒）
            - end_time (float): 结束时间（秒）
            - mean (float): 算术平均值
            - std (float): 标准差
            - min (float): 最小值
            - max (float): 最大值
            - range (float): 极差（max - min）
            - rms (float): 均方根值
            - percentiles (dict, 可选): 分位数 {f"P{n}": value}
        枚举型信号包含以下键：
            - count (int): 采样点数量
            - duration (float): 信号总时长（秒）
            - start_time (float): 起始时间（秒）
            - end_time (float): 结束时间（秒）
            - unique_count (int): 不同取值的数量
            - most_common (dict): {"value": str, "count": int} 出现最多的值
            - value_distribution (dict): {str_value: count} 各值的出现次数

    Raises:
        ValueError: 当输入参数无效时。
    """
    # 参数校验
    if len(timestamps) != len(samples):
        raise ValueError(
            f"timestamps 和 samples 长度不一致: "
            f"{len(timestamps)} vs {len(samples)}"
        )

    if len(timestamps) == 0:
        raise ValueError("输入数据为空，无法计算统计信息")

    # 公共基础信息
    duration = float(timestamps[-1] - timestamps[0])
    result: Dict[str, Any] = {
        "count": len(samples),
        "duration": round(duration, 6),
        "start_time": float(timestamps[0]),
        "end_time": float(timestamps[-1]),
    }

    is_numeric = np.issubdtype(samples.dtype, np.number)

    if is_numeric:
        _compute_numeric_stats(samples, result, percentiles)
    else:
        _compute_enum_stats(samples, result)

    return result


def _compute_numeric_stats(
    samples: np.ndarray,
    result: Dict[str, Any],
    percentiles: Optional[List[float]],
) -> None:
    """计算数值型信号的统计指标，结果写入 result 字典。"""
    # 过滤 NaN 和 Inf 值用于统计计算
    valid_mask = np.isfinite(samples)
    valid_samples = samples[valid_mask]
    nan_count = len(samples) - len(valid_samples)

    if len(valid_samples) == 0:
        result.update({
            "mean": float("nan"),
            "std": float("nan"),
            "min": float("nan"),
            "max": float("nan"),
            "range": float("nan"),
            "rms": float("nan"),
            "nan_count": nan_count,
        })
        return

    # 基本统计量
    mean_val = float(np.mean(valid_samples))
    std_val = float(np.std(valid_samples, ddof=1)) if len(valid_samples) > 1 else 0.0
    min_val = float(np.min(valid_samples))
    max_val = float(np.max(valid_samples))

    # 均方根 (RMS)
    rms_val = float(np.sqrt(np.mean(np.square(valid_samples))))

    result.update({
        "mean": round(mean_val, 6),
        "std": round(std_val, 6),
        "min": round(min_val, 6),
        "max": round(max_val, 6),
        "range": round(max_val - min_val, 6),
        "rms": round(rms_val, 6),
    })

    if nan_count > 0:
        result["nan_count"] = nan_count

    if percentiles:
        pcts = {}
        for p in percentiles:
            if not (0 <= p <= 100):
                continue
            p_val = float(np.percentile(valid_samples, p))
            pcts[f"P{p}"] = round(p_val, 6)
        if pcts:
            result["percentiles"] = pcts


def _compute_enum_stats(
    samples: np.ndarray,
    result: Dict[str, Any],
) -> None:
    """计算枚举型信号的统计指标，结果写入 result 字典。"""
    # 统计各值出现次数
    value_counts: Dict[str, int] = {}
    for s in samples:
        key = s.decode("utf-8") if isinstance(s, bytes) else str(s)
        value_counts[key] = value_counts.get(key, 0) + 1

    # 按出现次数降序排列
    sorted_values = sorted(value_counts.items(), key=lambda x: x[1], reverse=True)

    result.update({
        "unique_count": len(value_counts),
        "most_common": {
            "value": sorted_values[0][0],
            "count": sorted_values[0][1],
        },
        "value_distribution": dict(sorted_values),
    })
