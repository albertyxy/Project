# -*- coding: utf-8 -*-
"""Executor 节点：在沙箱中安全执行代码，捕获结果。

执行前自动修复 LLM 常见的导入幻觉（如 from tools / from cross_reference_utils），
并注入正确的 import 语句。
"""

import re
import os
from typing import Dict, Any

from .sandbox import execute_code
from .tools_description import get_tool_scripts_dir


# 工具函数 -> 所属模块文件名（均为同名 .py 文件）
_FUNC_TO_MODULE = {
    "list_signals": "list_signals",
    "extract_signal": "extract_signal",
    "extract_around_edges": "extract_around_edges",
    "find_time_ranges": "find_time_ranges",
    "signal_statistics": "signal_statistics",
    "plot_signals": "plot_signals",
    "cross_reference": "cross_reference",
}

# 有效模块名集合（用于校验 import）
_VALID_MODULES = set(_FUNC_TO_MODULE.values())


def _fix_imports(code: str) -> str:
    """修复 LLM 生成的代码中的导入语句。

    1. 扫描代码中实际调用了哪些工具函数
    2. 删除所有非标准库的 import 行（LLM 幻觉的各种包名）
    3. 在文件开头注入正确的 from xxx import xxx
    """
    tools_dir = get_tool_scripts_dir()

    # 检测代码中实际使用的工具函数
    used = set()
    for func in _FUNC_TO_MODULE:
        if re.search(r'(?<!\w)' + re.escape(func) + r'\s*\(', code):
            used.add(func)

    if not used:
        return code

    # 逐行处理：移除可疑的 import
    safe_prefixes = (
        "sys", "os", "re", "json", "time", "math",
        "numpy", "matplotlib", "PIL", "pathlib",
    )
    lines = code.split("\n")
    clean_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("from ") or stripped.startswith("import "):
            module_name = ""
            if stripped.startswith("from "):
                parts = stripped.split()
                if len(parts) >= 2:
                    module_name = parts[1].rstrip(".")
            elif stripped.startswith("import "):
                parts = stripped.split()
                if len(parts) >= 2:
                    module_name = parts[1].rstrip(".")

            if module_name and (
                module_name in _VALID_MODULES
                or module_name.startswith(safe_prefixes)
                or module_name in ("sys", "os", "re", "json", "math", "time")
            ):
                clean_lines.append(line)
                continue
            print(f"[Executor] 移除可疑导入: {stripped}")
            continue

        clean_lines.append(line)

    # 构建正确的导入头
    header = [
        "import sys, os",
        f"sys.path.insert(0, r'{tools_dir}')",
    ]
    for func in sorted(used):
        module = _FUNC_TO_MODULE.get(func, func)
        header.append(f"from {module} import {func}")
    header.append("")

    return "\n".join(header) + "\n".join(clean_lines)


def executor_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Executor 节点：执行 Coder 生成的 Python 代码。

    执行前自动修复导入语句，防止 LLM 幻觉包名。
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

    # 修复导入
    code = _fix_imports(generated_code)

    print(f"[Executor] 执行代码长度: {len(code)} 字符（第 {retries} 次执行）")

    result = execute_code(code, timeout=60)

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
