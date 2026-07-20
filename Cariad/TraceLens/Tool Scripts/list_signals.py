# -*- coding: utf-8 -*-
"""
列出 MF4 文件中所有信号名称的工具模块。
"""

import os
from typing import List

from asammdf import MDF


def list_signals(file_path: str) -> List[str]:
    """读取 MF4 文件，返回所有信号名称列表。

    Args:
        file_path: MF4 文件的路径。

    Returns:
        信号名称的字符串列表。

    Raises:
        FileNotFoundError: 当指定的文件不存在时。
        ValueError: 当文件无法被 asammdf 解析时。
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(
            f"文件不存在: {file_path}\n"
            f"请检查文件路径是否正确，确保文件未被移动或删除。"
        )

    try:
        with MDF(file_path) as mdf:
            signal_names: List[str] = []
            for channel in mdf.iter_channels():
                signal_names.append(channel.name)
            return signal_names
    except Exception as e:
        raise ValueError(
            f"无法读取 MF4 文件: {file_path}\n"
            f"错误详情: {e}"
        ) from e
