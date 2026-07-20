# -*- coding: utf-8 -*-
"""LangGraph 工作流组装：Planner → Coder → Executor → 重试/结束。"""

import os
import sys
from typing import Dict, Any, Optional

from langgraph.graph import StateGraph, END

# 确保项目根目录在 sys.path 中，以支持从外部调用
_project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

from agent.state import ProcessorState
from agent.planner import planner_node
from agent.coder import coder_node
from agent.executor import executor_node


# 条件路由函数
def _after_planner(state: ProcessorState) -> str:
    """Planner 之后的路由判断"""
    if state.get("needs_clarification"):
        return "clarify"
    return "coder"


def _after_executor(state: ProcessorState) -> str:
    """Executor 之后的路由判断"""
    exec_result = state.get("execution_result")
    if exec_result and exec_result.get("success"):
        return "end"

    retries = state.get("retries", 0)
    max_retries = state.get("max_retries", 2)
    if retries < max_retries:
        print(f"[Workflow] 执行失败，进入重试（{retries}/{max_retries}）...")
        return "coder"

    return "end"


def _clarify_node(state: ProcessorState) -> Dict[str, Any]:
    """追问节点：不做处理，仅将状态传回给 Streamlit 展示。"""
    print(f"[Workflow] 需要用户澄清: {state.get('clarification_question', '')}")
    return {}


def create_workflow() -> StateGraph:
    """创建并编译 TraceLens Agent 工作流。

    Returns:
        编译后的 LangGraph 工作流实例。
    """
    workflow = StateGraph(ProcessorState)

    # 添加节点
    workflow.add_node("planner", planner_node)
    workflow.add_node("coder", coder_node)
    workflow.add_node("executor", executor_node)
    workflow.add_node("clarify", _clarify_node)

    # 入口
    workflow.set_entry_point("planner")

    # Planner 分支：清晰 → Coder，模糊 → 追问
    workflow.add_conditional_edges(
        "planner",
        _after_planner,
        {"coder": "coder", "clarify": "clarify"},
    )

    # 追问节点直接结束（由 Streamlit 处理交互循环）
    workflow.add_edge("clarify", END)

    # Coder → Executor
    workflow.add_edge("coder", "executor")

    # Executor 分支：成功 → 结束，失败且可重试 → Coder，失败且不可重试 → 结束
    workflow.add_conditional_edges(
        "executor",
        _after_executor,
        {"coder": "coder", "end": END},
    )

    compiled = workflow.compile()
    print("[Workflow] 工作流编译完成")
    return compiled


def run_agent(
    user_query: str,
    selected_file: str,
    data_dir: Optional[str] = None,
    max_retries: int = 2,
) -> Dict[str, Any]:
    """运行 TraceLens Agent。

    Args:
        user_query: 用户自然语言需求。
        selected_file: MF4 文件的绝对路径。
        data_dir: 数据目录路径（可选，默认使用项目 data/ 目录）。
        max_retries: 最大重试次数，默认 2。

    Returns:
        最终状态字典，包含执行结果。
    """
    if data_dir is None:
        data_dir = os.path.join(os.path.dirname(__file__), "..", "data")

    # 规范化路径
    selected_file = os.path.abspath(selected_file)
    data_dir = os.path.abspath(data_dir)

    initial_state: ProcessorState = {
        "user_query": user_query,
        "selected_file": selected_file,
        "data_dir": data_dir,
        "plan": None,
        "plan_reasoning": None,
        "needs_clarification": False,
        "clarification_question": None,
        "generated_code": None,
        "execution_result": None,
        "retries": 0,
        "max_retries": max_retries,
        "messages": [],
    }

    workflow = create_workflow()
    result = workflow.invoke(initial_state)
    return result
