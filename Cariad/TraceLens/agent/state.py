# -*- coding: utf-8 -*-
"""LangGraph State 定义。"""

from typing import TypedDict, Optional, List, Dict, Any


class ProcessorState(TypedDict):
    """TraceLens Agent 全局状态"""

    # === 输入 ===
    user_query: str                          # 用户自然语言输入
    selected_file: str                      # 用户选择的 MF4 文件路径（必选）
    data_dir: str                           # MF4 数据目录

    # === Planner 输出 ===
    plan: Optional[Dict[str, Any]]          # 结构化任务 {"signals": [...], "operation": str, "params": {...}}
    plan_reasoning: Optional[str]           # Planner 的推理过程
    needs_clarification: bool               # 是否需要向用户追问（需求模糊时为 True）
    clarification_question: Optional[str]   # 追问内容

    # === Coder 输出 ===
    generated_code: Optional[str]           # LLM 生成的 Python 代码

    # === Executor 输出 ===
    execution_result: Optional[Dict[str, Any]]  # {"success": bool, "output": str, "images": [...], "error": str}
    retries: int                            # 当前重试次数
    max_retries: int                        # 最大重试次数（默认 2）

    # === 消息历史 ===
    messages: List[Dict[str, Any]]          # 错误上下文（用于重试时传递错误信息）
