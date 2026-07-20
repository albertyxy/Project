# -*- coding: utf-8 -*-
"""解析 Tool Scripts 的函数签名和文档，格式化为 LLM 可读的工具描述。

通过 AST 解析源码文件获取函数签名，避免导入实际模块（防止依赖问题如 asammdf）。
"""

import os
import ast
from typing import Dict, List, Optional


_TOOL_SCRIPTS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Tool Scripts")
)

# 四个工具模块及其中需要描述的函数名
_TOOL_MODULES: Dict[str, str] = {
    "list_signals.py": "list_signals",
    "extract_signal.py": "extract_signal",
    "extract_around_edges.py": "extract_around_edges",
    "plot_signals.py": "plot_signals",
}


def _parse_type_annotation(node) -> str:
    """将 AST 类型注解节点转为字符串"""
    if node is None:
        return ""
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Subscript):
        base = _parse_type_annotation(node.value)
        slice_str = _parse_type_annotation(node.slice)
        return f"{base}[{slice_str}]"
    if isinstance(node, ast.Tuple):
        elts = [_parse_type_annotation(e) for e in node.elts]
        return ", ".join(elts)
    if isinstance(node, ast.Constant):
        if node.value is None:
            return "None"
        return repr(node.value)
    if isinstance(node, ast.Attribute):
        return f"{_parse_type_annotation(node.value)}.{node.attr}"
    return ""


def _parse_default(node) -> str:
    """将 AST 默认值节点转为字符串"""
    if node is None:
        return ""
    if isinstance(node, ast.Constant):
        if isinstance(node.value, str):
            return repr(node.value)
        if node.value is None:
            return "None"
        return str(node.value)
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.UnaryOp):
        if isinstance(node.op, ast.USub):
            return f"-{_parse_default(node.operand)}"
        return str(node)
    return "..."


def _extract_function_from_ast(
    source: str, func_name: str
) -> Optional[dict]:
    """从 Python 源码字符串中提取指定函数的签名和文档。

    Returns:
        {
            "name": str,           # 函数名
            "params": list[dict],  # [{"name": str, "type": str, "default": str}]
            "doc": str,            # 文档字符串
        }
        找不到函数时返回 None。
    """
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name == func_name:
                # 提取参数信息
                params = []
                for arg in node.args.args:
                    param_info = {
                        "name": arg.arg,
                        "type": _parse_type_annotation(arg.annotation),
                        "default": "",
                    }
                    params.append(param_info)

                # 填充默认值（默认值在 args.defaults 中，与后 N 个参数对应）
                defaults = node.args.defaults
                if defaults:
                    offset = len(params) - len(defaults)
                    for i, d in enumerate(defaults):
                        params[offset + i]["default"] = _parse_default(d)

                # 提取 docstring
                doc = ast.get_docstring(node) or ""

                return {
                    "name": func_name,
                    "params": params,
                    "doc": doc,
                }

    return None


def _format_function_desc(func_info: dict) -> str:
    """将函数信息格式化为 LLM 可读的描述字符串"""
    name = func_info["name"]
    params = func_info["params"]
    doc = func_info["doc"]

    # 构建签名
    param_strs = []
    for p in params:
        p_str = p["name"]
        if p["type"]:
            p_str += f": {p['type']}"
        if p["default"]:
            p_str += f" = {p['default']}"
        param_strs.append(p_str)

    lines = [
        f"## {name}",
        f"签名: {name}({', '.join(param_strs)})",
    ]

    if doc:
        doc_lines = doc.strip().split("\n")
        lines.append(f"功能: {doc_lines[0].strip()}")
        if len(doc_lines) > 1:
            lines.append("详细说明:")
            for dl in doc_lines[1:]:
                dl_stripped = dl.strip()
                if dl_stripped:
                    lines.append(f"  {dl_stripped}")
    else:
        lines.append("功能: 无文档")

    lines.append("参数:")
    for p in params:
        type_str = f": {p['type']}" if p["type"] else ""
        default_str = f" (默认: {p['default']})" if p["default"] else ""
        lines.append(f"    - {p['name']}{type_str}{default_str}")

    return "\n".join(lines)


def get_tools_description() -> str:
    """获取所有工具函数的 LLM 可读描述文本。

    通过 AST 解析源码获取函数签名和文档，不导入实际模块。

    Returns:
        格式化的工具函数描述字符串。
    """
    descriptions = []

    for filename, func_name in _TOOL_MODULES.items():
        file_path = os.path.join(_TOOL_SCRIPTS_DIR, filename)
        if not os.path.isfile(file_path):
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()

        func_info = _extract_function_from_ast(source, func_name)
        if func_info:
            descriptions.append(_format_function_desc(func_info))

    return "\n\n".join(descriptions)


def get_tools_summary() -> str:
    """获取工具函数的简要摘要（用于 Planner 节点）。

    Returns:
        简短的函数列表和用途说明。
    """
    return (
        "可用操作：\n"
        "  - list_signals(file_path): 列出 MF4 文件中的所有信号名\n"
        "  - extract_signal(file_path, signal_name, start_time?, end_time?): 提取信号数据\n"
        "  - extract_around_edges(timestamps, samples, edge_type?, window_before?, window_after?): 检测边沿变化\n"
        "  - plot_signals(data_dict, title, output_path, primary_signal?, mode?): 绘制信号曲线图"
    )


def get_tool_scripts_dir() -> str:
    """获取 Tool Scripts 目录的绝对路径。"""
    return _TOOL_SCRIPTS_DIR
