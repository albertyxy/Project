# -*- coding: utf-8 -*-
"""TraceLens - AI Agent for MF4 Signal Analysis - Streamlit 交互式前端。"""

import os
import sys
import glob
import time

import streamlit as st

# 确保项目根目录在 sys.path 中
_project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

from agent.workflow import run_agent

# 页面配置
st.set_page_config(
    page_title="TraceLens",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# session_state 初始化
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # [(role, content), ...]
if "awaiting_clarification" not in st.session_state:
    st.session_state.awaiting_clarification = False
if "pending_state" not in st.session_state:
    st.session_state.pending_state = None  # 暂存上次 Planner 返回的状态
if "selected_file" not in st.session_state:
    st.session_state.selected_file = None
if "execution_in_progress" not in st.session_state:
    st.session_state.execution_in_progress = False

DATA_DIR = os.path.join(_project_root, "data")
OUTPUT_DIR = os.path.join(_project_root, "output")


def get_mf4_files() -> list:
    """获取 data/ 目录下的所有 .mf4 文件"""
    if not os.path.isdir(DATA_DIR):
        return []
    files = glob.glob(os.path.join(DATA_DIR, "*.mf4"))
    return sorted([os.path.basename(f) for f in files])


def display_chat_history():
    """显示对话历史"""
    for role, content in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(content)


def handle_user_query(query: str):
    """处理用户输入，调用 Agent 并展示结果"""
    if not st.session_state.selected_file:
        st.warning("请先在侧边栏选择一个 MF4 文件。")
        return

    selected_path = os.path.join(DATA_DIR, st.session_state.selected_file)

    # 添加用户消息到历史
    st.session_state.chat_history.append(("user", query))

    # 如果之前有追问状态，拼接到原 query
    if st.session_state.awaiting_clarification and st.session_state.pending_state:
        old_state = st.session_state.pending_state
        combined_query = (
            f"【原始需求】\n{old_state.get('user_query', '')}\n\n"
            f"【用户补充】\n{query}"
        )
        st.session_state.awaiting_clarification = False
        st.session_state.pending_state = None
    else:
        combined_query = query

    # 执行 Agent
    st.session_state.execution_in_progress = True

    with st.spinner("Agent 正在处理..."):
        try:
            result = run_agent(
                user_query=combined_query,
                selected_file=selected_path,
            )
        except Exception as e:
            st.session_state.chat_history.append(
                ("assistant", f":red[执行异常: {str(e)}]")
            )
            st.session_state.execution_in_progress = False
            st.rerun()

    st.session_state.execution_in_progress = False

    # 检查是否需要追问
    if result.get("needs_clarification"):
        question = result.get("clarification_question", "请提供更多信息。")
        st.session_state.chat_history.append(("assistant", f":blue[:grey_question: {question}]"))
        st.session_state.awaiting_clarification = True
        st.session_state.pending_state = result
        st.rerun()

    # 处理执行结果
    exec_result = result.get("execution_result", {})
    if exec_result.get("success"):
        _display_success(exec_result, result)
    else:
        _display_failure(exec_result, result)


def _display_success(exec_result: dict, result: dict):
    """展示成功执行结果"""
    images = exec_result.get("images", [])
    output = exec_result.get("output", "")

    msg_parts = []

    if images:
        msg_parts.append("### :white_check_mark: 执行成功")
        for img_path in images:
            if os.path.isfile(img_path):
                msg_parts.append(f"![结果图片]({img_path})")
                msg_parts.append(f"*图片路径: {img_path}*")
            else:
                msg_parts.append(f":warning: 图片路径不存在: {img_path}")
    else:
        msg_parts.append("### :white_check_mark: 执行成功（无图片输出）")

    if output:
        msg_parts.append(f"```\n{output.strip()}\n```")

    # Planner 推理过程
    plan = result.get("plan")
    if plan:
        with st.expander("查看任务解析详情"):
            st.json(plan)

    msg = "\n\n".join(msg_parts)
    st.session_state.chat_history.append(("assistant", msg))


def _display_failure(exec_result: dict, result: dict):
    """展示失败执行结果"""
    error = exec_result.get("error", "未知错误")
    retries = result.get("retries", 0)
    max_retries = result.get("max_retries", 2)

    msg = (
        f"### :x: 执行失败\n\n"
        f"**错误信息**:\n```\n{error}\n```\n\n"
        f"重试次数: {retries}/{max_retries}"
    )

    # 显示生成的代码（用于调试）
    code = result.get("generated_code")
    if code:
        with st.expander("查看生成的代码"):
            st.code(code, language="python")

    st.session_state.chat_history.append(("assistant", msg))


# === UI 布局 ===

st.title("TraceLens")
st.caption("AI Agent for MF4 Signal Analysis - 通过自然语言描述需求，自动从 MF4 源数据中提取信号、检测边沿变化、生成可视化图片。")

# 侧边栏：文件选择
with st.sidebar:
    st.header("配置")

    mf4_files = get_mf4_files()
    if not mf4_files:
        st.error("data/ 目录下未找到 .mf4 文件。")
    else:
        selected = st.selectbox(
            "选择 MF4 文件",
            options=mf4_files,
            index=(
                mf4_files.index(st.session_state.selected_file)
                if st.session_state.selected_file in mf4_files
                else 0
            ),
            key="file_selector",
        )
        # 检测文件切换
        if selected != st.session_state.selected_file:
            st.session_state.selected_file = selected
            st.session_state.chat_history = []
            st.session_state.awaiting_clarification = False
            st.session_state.pending_state = None

    st.divider()

    # 显示当前状态
    st.caption(f"选中文件: {st.session_state.selected_file or '无'}")
    if st.session_state.awaiting_clarification:
        st.info("等待用户补充信息...")

    st.divider()

    if st.button("清空对话", use_container_width=True):
        st.session_state.chat_history = []
        st.session_state.awaiting_clarification = False
        st.session_state.pending_state = None
        st.rerun()

# 主区域：对话历史
display_chat_history()

# 输入区域
if not st.session_state.execution_in_progress:
    user_input = st.chat_input(
        placeholder=(
            "输入您的需求，例如：'绘制 EPS_StgTq.Val 从 10s 到 30s 的波形' "
            if not st.session_state.awaiting_clarification
            else "请补充说明..."
        ),
        key="chat_input",
    )

    if user_input and user_input.strip():
        handle_user_query(user_input.strip())
        st.rerun()
