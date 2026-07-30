# -*- coding: utf-8 -*-
"""TraceLens - AI Agent for MF4 Signal Analysis - Streamlit 交互式前端。

两个 Tab:
  - 信号分析: 自然语言交互，Planner -> Coder -> Executor
  - 报告生成: 表单式，一键生成 PPT 测试报告
"""

import os
import re
import sys
import glob
import time
import importlib

import streamlit as st

# 确保项目根目录在 sys.path 中
_project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

from agent.workflow import run_agent
from agent.ppt_workflow import generate_report

# 页面配置
st.set_page_config(
    page_title="TraceLens",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)

DATA_DIR = os.path.join(_project_root, "data")
OUTPUT_DIR = os.path.join(_project_root, "output")
TEMPLATE_DIR = os.path.join(DATA_DIR, "Template")


# ============================================================================
# 信号分析 Tab - session_state
# ============================================================================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "awaiting_clarification" not in st.session_state:
    st.session_state.awaiting_clarification = False
if "pending_state" not in st.session_state:
    st.session_state.pending_state = None
if "selected_file" not in st.session_state:
    st.session_state.selected_file = None
if "execution_in_progress" not in st.session_state:
    st.session_state.execution_in_progress = False


def get_mf4_files() -> list:
    """获取 data/ 目录下的所有 .mf4/.MF4 文件"""
    if not os.path.isdir(DATA_DIR):
        return []
    files = glob.glob(os.path.join(DATA_DIR, "*.mf4"))
    files += glob.glob(os.path.join(DATA_DIR, "*.MF4"))
    return sorted([os.path.basename(f) for f in files])


def get_project_dirs() -> list:
    """获取 data/ 下包含 Trace Record.xlsx 的项目目录"""
    if not os.path.isdir(DATA_DIR):
        return []
    projects = []
    for d in os.listdir(DATA_DIR):
        full = os.path.join(DATA_DIR, d)
        if os.path.isdir(full) and d != "Template":
            excel = os.path.join(full, "Trace Record.xlsx")
            if os.path.isfile(excel):
                projects.append(d)
    return sorted(projects)


def _escape_markdown_underscores(text: str) -> str:
    """转义代码块外的下划线，防止信号名被 markdown 解析为斜体。"""
    parts = re.split(r"(```[^`]*```)", text)
    for i, part in enumerate(parts):
        if not part.startswith("```"):
            parts[i] = part.replace("_", "\\_")
    return "".join(parts)


# ============================================================================
# Tab 1: 信号分析
# ============================================================================
def render_signal_analysis_tab():
    """渲染信号分析 Tab (对话式交互)"""
    # 侧边栏：文件选择
    with st.sidebar:
        st.header("信号分析配置")

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
            if selected != st.session_state.selected_file:
                st.session_state.selected_file = selected
                st.session_state.chat_history = []
                st.session_state.awaiting_clarification = False
                st.session_state.pending_state = None

        st.divider()
        st.caption(f"选中文件: {st.session_state.selected_file or '无'}")
        if st.session_state.awaiting_clarification:
            st.info("等待用户补充信息...")

        st.divider()
        if st.button("清空对话", use_container_width=True):
            st.session_state.chat_history = []
            st.session_state.awaiting_clarification = False
            st.session_state.pending_state = None
            st.rerun()

    # 主区域
    display_chat_history()
    render_chat_input()


def display_chat_history():
    """显示对话历史"""
    for role, content in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(_escape_markdown_underscores(content))


def render_chat_input():
    """渲染聊天输入框"""
    if st.session_state.execution_in_progress:
        return

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


def handle_user_query(query: str):
    """处理用户输入，调用 Agent 并展示结果"""
    if not st.session_state.selected_file:
        st.warning("请先在侧边栏选择一个 MF4 文件。")
        return

    selected_path = os.path.join(DATA_DIR, st.session_state.selected_file)
    st.session_state.chat_history.append(("user", query))

    # 追问拼接
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

    if result.get("needs_clarification"):
        question = result.get("clarification_question", "请提供更多信息。")
        st.session_state.chat_history.append(
            ("assistant", f":blue[:grey_question: {question}]")
        )
        st.session_state.awaiting_clarification = True
        st.session_state.pending_state = result
        st.rerun()

    exec_result = result.get("execution_result", {})
    if exec_result.get("success"):
        _display_success(exec_result, result)
    else:
        _display_failure(exec_result, result)


def _display_success(exec_result: dict, result: dict):
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

    plan = result.get("plan")
    if plan:
        with st.expander("查看任务解析详情"):
            st.json(plan)

    msg = "\n\n".join(msg_parts)
    st.session_state.chat_history.append(("assistant", msg))


def _display_failure(exec_result: dict, result: dict):
    error = exec_result.get("error", "未知错误")
    retries = result.get("retries", 0)
    max_retries = result.get("max_retries", 2)

    msg_parts = [
        f"### :x: 执行失败",
        f"**错误信息**:\n```\n{error}\n```",
        f"重试次数: {retries}/{max_retries}",
    ]

    code = result.get("generated_code")
    if code:
        msg_parts.append(f"**生成的代码**:\n```python\n{code}\n```")

    msg = "\n\n".join(msg_parts)
    st.session_state.chat_history.append(("assistant", msg))


# ============================================================================
# Tab 2: 报告生成
# ============================================================================
def render_report_generation_tab():
    """渲染报告生成 Tab (表单式)"""
    st.header("PPT 报告生成")
    st.caption("从 Trace Record + XML + MF4 数据自动生成测试报告 PPT。")

    # 项目选择
    projects = get_project_dirs()
    if not projects:
        st.error("data/ 目录下未找到包含 Trace Record.xlsx 的项目文件夹。")
        return

    col1, col2 = st.columns(2)

    with col1:
        project_name = st.selectbox(
            "项目目录",
            options=projects,
            help="data/ 下包含 Trace Record.xlsx 的文件夹",
        )

    with col2:
        # 模板选择
        templates = []
        if os.path.isdir(TEMPLATE_DIR):
            templates = glob.glob(os.path.join(TEMPLATE_DIR, "*.pptx"))
            templates = [os.path.basename(t) for t in templates if not os.path.basename(t).startswith("~$")]
        if not templates:
            templates = ["(无模板)"]

        template_name = st.selectbox(
            "PPT 模板",
            options=templates,
            help="data/Template/ 下的 .pptx 文件",
        )

    # 输出设置
    output_name = f"{project_name}_Report.pptx"
    output_path = os.path.join(OUTPUT_DIR, output_name)

    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        st.text_input("输出路径", value=output_path, disabled=True, key="output_path_display")
    with col2:
        st.caption(f"将保存到 `output/{output_name}`")

    # 场景映射预览
    with st.expander("查看场景->幻灯片映射"):
        try:
            from agent.ppt_workflow import SCENARIO_SLIDE_MAP
            import yaml as yaml_lib
            yaml_path = os.path.join(_project_root, "agent", "table_mapping.yaml")
            with open(yaml_path, "r", encoding="utf-8") as f:
                cfg = yaml_lib.safe_load(f)
            scenarios_cfg = cfg.get("scenarios", {})

            rows = []
            for name, slide_num in SCENARIO_SLIDE_MAP.items():
                sc = scenarios_cfg.get(name, {})
                cols = sc.get("columns", [])
                has_table = len(cols) > 0
                rows.append((slide_num, name, "Y" if has_table else "待补充"))
            rows.sort()
            st.dataframe(
                [{"Slide": r[0], "场景": r[1], "表格配置": r[2]} for r in rows],
                use_container_width=True,
                hide_index=True,
            )
        except Exception:
            st.caption("无法加载映射配置")

    st.divider()

    # 生成按钮
    template_path = os.path.join(TEMPLATE_DIR, template_name) if template_name != "(无模板)" else None

    if st.button("生成报告", type="primary", use_container_width=True, disabled=(template_path is None)):
        if template_path is None or not os.path.isfile(template_path):
            st.error("请选择有效的 PPT 模板文件。")
            return

        project_dir = os.path.join(DATA_DIR, project_name)
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        progress_bar = st.progress(0, text="正在读取 Trace Record...")
        status_text = st.empty()

        try:
            st.info("正在生成报告，请稍候...")
            result_path = generate_report(
                project_dir=project_dir,
                template_path=template_path,
                output_path=output_path,
            )

            progress_bar.progress(100, text="报告生成完成!")
            status_text.success(f"报告已保存: `{result_path}`")

            # 提供下载
            with open(result_path, "rb") as f:
                st.download_button(
                    label="下载 PPT 报告",
                    data=f.read(),
                    file_name=output_name,
                    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                    use_container_width=True,
                )

        except Exception as e:
            progress_bar.progress(100, text="生成失败")
            status_text.error(f"报告生成失败: {str(e)}")


# ============================================================================
# 主入口
# ============================================================================
st.title("TraceLens")
st.caption("AI Agent for MF4 Signal Analysis - 自然语言信号分析 + 一键 PPT 报告生成")

tab1, tab2 = st.tabs(["信号分析", "报告生成"])

with tab1:
    render_signal_analysis_tab()

with tab2:
    render_report_generation_tab()
