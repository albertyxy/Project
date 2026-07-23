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

# 七个工具模块及其中需要描述的函数名
_TOOL_MODULES: Dict[str, str] = {
    "list_signals.py": "list_signals",
    "extract_signal.py": "extract_signal",
    "extract_around_edges.py": "extract_around_edges",
    "find_time_ranges.py": "find_time_ranges",
    "signal_statistics.py": "signal_statistics",
    "plot_signals.py": "plot_signals",
    "cross_reference.py": "cross_reference",
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
    """将函数信息格式化为 LLM 可读的紧凑描述（省 token）。"""
    name = func_info["name"]
    params = func_info["params"]
    doc = func_info["doc"]

    # 紧凑签名：param=default，不含类型注解
    param_strs = []
    for p in params:
        p_str = p["name"]
        if p["default"]:
            p_str += f"={p['default']}"
        param_strs.append(p_str)

    # 取 docstring 第一行作为功能说明
    summary = doc.strip().split("\n")[0].strip() if doc else ""

    return f"{name}({', '.join(param_strs)})\n  {summary}"


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
        "  - find_time_ranges(timestamps, samples, condition, threshold?, lower?, upper?, value?, ...): 按条件查找时间窗口\n"
        "  - signal_statistics(timestamps, samples, percentiles?): 计算信号统计摘要\n"
        "  - plot_signals(data_dict, title, output_path, primary_signal?, mode?): 绘制信号曲线图\n"
        "  - cross_reference(file_path, trigger_signal?, target_signals, condition?, value?, triggers?): 跨信号关联查询\n"
        "    单触发: trigger_signal + condition + value; 多触发: triggers=[{signal, condition, value}, ...]\n"
        "    返回触发时刻各触发信号值和目标信号值"
    )


def get_tool_scripts_dir() -> str:
    """获取 Tool Scripts 目录的绝对路径。"""
    return _TOOL_SCRIPTS_DIR
