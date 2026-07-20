# -*- coding: utf-8 -*-
"""Executor 节点：在沙箱中安全执行代码，捕获结果。"""

from typing import Dict, Any

from .sandbox import execute_code


def executor_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Executor 节点：执行 Coder 生成的 Python 代码。

    Args:
        state: 当前 ProcessorState。

    Returns:
        更新后的 state 字典（部分更新），包含 execution_result 和 incremented retries。
    """
    print("[Executor] 开始执行代码...")

    generated_code = state.get("generated_code", "")
    retries = state.get("retries", 0) + 1

    if not generated_code:
        return {
            "execution_result": {
                "success": False,
                "output": "",
                "images": [],
                "error": "没有可执行的代码（generated_code 为空）。",
            },
            "retries": retries,
        }

    print(f"[Executor] 执行代码长度: {len(generated_code)} 字符（第 {retries} 次执行）")

    result = execute_code(generated_code, timeout=30)

    print(
        f"[Executor] 执行结果: success={result['success']}, "
        f"images={result['images']}, "
        f"output_len={len(result['output'])}"
    )

    if not result["success"]:
        error_text = result["error"] or result["output"] or "未知错误"
        print(f"[Executor] 执行失败: {error_text[:300]}")

    return {
        "execution_result": result,
        "retries": retries,
    }
