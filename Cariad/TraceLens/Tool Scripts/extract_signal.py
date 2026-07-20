# -*- coding: utf-8 -*-
"""
从 MF4 文件中提取指定信号数据的工具模块。
"""

import os
from typing import Tuple

import numpy as np

from asammdf import MDF


def extract_signal(
    file_path: str,
    signal_name: str,
    start_time: float = None,
    end_time: float = None,
) -> Tuple[np.ndarray, np.ndarray]:
    """提取指定信号的数据，支持按时间范围裁剪。

    Args:
        file_path: MF4 文件的路径。
        signal_name: 要提取的信号名称。
        start_time: 可选，裁剪起始时间（秒）。None 表示从文件开头开始。
        end_time: 可选，裁剪结束时间（秒）。None 表示到文件末尾结束。

    Returns:
        一个元组 (timestamps, samples)：
        - timestamps: 一维 numpy 数组，包含时间戳（秒）。
        - samples: 一维 numpy 数组，包含对应的信号采样值。

    Raises:
        FileNotFoundError: 当指定的文件不存在时。
        KeyError: 当指定的信号在文件中不存在时。
        ValueError: 当 MF4 文件无法解析时。
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(
            f"文件不存在: {file_path}\n"
            f"请检查文件路径是否正确，确保文件未被移动或删除。"
        )

    try:
        with MDF(file_path) as mdf:
            # 检查信号是否存在
            occurrences = mdf.whereis(signal_name)
            if not occurrences:
                available = [ch.name for ch in mdf.iter_channels()]
                raise KeyError(
                    f"信号 '{signal_name}' 在文件中不存在。\n"
                    f"文件中可用的信号有 ({len(available)} 个):\n"
                    + "\n".join(f"  - {name}" for name in available)
                )

            # 根据时间范围决定是否裁剪
            if start_time is not None or end_time is not None:
                mdf = mdf.cut(start=start_time, stop=end_time)

            signal = mdf.get(signal_name)
            timestamps = signal.timestamps.astype(np.float64)
            samples = signal.samples

            # 尝试转为 float64，若信号为枚举/文本类型则保留原始值
            try:
                samples = samples.astype(np.float64)
            except (ValueError, TypeError):
                pass  # 保留原始 dtype（如 bytes、object 等）

            return timestamps, samples

    except (FileNotFoundError, KeyError):
        raise
    except Exception as e:
        raise ValueError(
            f"无法从文件中提取信号 '{signal_name}': {file_path}\n"
            f"错误详情: {e}"
        ) from e
