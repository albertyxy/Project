# -*- coding: utf-8 -*-
"""演示：提取 MF4 信号并绘制曲线图。"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "Tool Scripts"))

from extract_signal import extract_signal
from plot_signals import plot_signals


def _is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    filename = sys.argv[1]
    raw_args = sys.argv[2:]

    # 末尾的纯数字视为时间范围
    time_args = []
    while raw_args and _is_number(raw_args[-1]):
        time_args.insert(0, float(raw_args.pop()))

    # 检测 split 模式
    mode = "overlay"
    if raw_args and raw_args[-1] == "--split":
        raw_args.pop()
        mode = "split"

    # 拦截未知的 -- 参数
    for arg in raw_args:
        if arg.startswith("--"):
            print(f"错误: 未知参数 '{arg}'，支持的模式参数: --split")
            sys.exit(1)

    signal_names = raw_args
    start_time = time_args[0] if len(time_args) >= 1 else None
    end_time = time_args[1] if len(time_args) >= 2 else None

    file_path = os.path.join(os.path.dirname(__file__), "data", filename)

    base_name = os.path.splitext(filename)[0]
    safe_signals = "_".join(
        s.replace(".", "_").replace("/", "_") for s in signal_names
    )
    output_path = os.path.join(
        os.path.dirname(__file__), "output", f"{base_name}_{safe_signals}.png"
    )

    data_dict = {}
    for name in signal_names:
        timestamps, samples = extract_signal(
            file_path, name, start_time, end_time
        )
        data_dict[name] = (timestamps, samples)

    saved_path = plot_signals(
        data_dict,
        title=f"{filename} - {', '.join(signal_names)}",
        output_path=output_path,
        primary_signal=signal_names[0],
        mode=mode,
    )
    print(f"图片已保存 ({mode}): {saved_path}")
