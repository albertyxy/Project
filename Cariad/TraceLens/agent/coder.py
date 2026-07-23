# -*- coding: utf-8 -*-
"""Coder 节点：根据结构化任务生成可执行的 Python 代码。"""

import json
import os
import re
from typing import Dict, Any

import yaml
from openai import OpenAI
from dotenv import load_dotenv

from .tools_description import get_tools_description, get_tool_scripts_dir

# 加载 .env 配置
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))


def _load_prompts() -> Dict[str, Any]:
    """加载 prompts.yaml 配置"""
    yaml_path = os.path.join(os.path.dirname(__file__), "prompts.yaml")
    with open(yaml_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _create_llm_client() -> OpenAI:
    """创建 Coder LLM 客户端（OpenAI 兼容 API）"""
    api_key = os.getenv("CODER_API_KEY", "")
    api_base = os.getenv("CODER_API_BASE", "https://api.openai.com/v1")

    if not api_key or api_key == "your_coder_api_key_here":
        raise ValueError(
            "请在 .env 文件中配置 CODER_API_KEY（Coder 使用的 LLM API Key）"
        )

    return OpenAI(api_key=api_key, base_url=api_base)


def _strip_markdown_fences(code: str) -> str:
    """去除 LLM 响应中的 markdown 代码块标记。

    处理 ```python、```、```` 等各种变体。
    """
    code = code.strip()

    # 匹配开头的 ``` 标记（可能带有语言标识）
    fence_start_pattern = r"^```[\w]*\s*\n"
    match = re.match(fence_start_pattern, code)
    if match:
        code = code[match.end():]

    # 匹配结尾的 ``` 标记
    if code.endswith("```"):
        code = code[:-3].rstrip()

    return code.strip()


def _build_coder_prompt(
    plan: Dict[str, Any],
    selected_file: str,
    data_dir: str,
    error_context: str = "",
) -> str:
    """构建 Coder 节点的完整用户 Prompt。

    Args:
        plan: Planner 输出的结构化任务。
        selected_file: 用户选择的 MF4 文件绝对路径。
        data_dir: MF4 数据目录。
        error_context: 重试时的错误信息上下文。

    Returns:
        完整的用户消息字符串。
    """
    tools_desc = get_tools_description()
    tools_dir = get_tool_scripts_dir()

    # 项目根目录和输出目录
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    output_dir = os.path.join(project_dir, "output")

    # 生成输出文件名
    base_name = os.path.splitext(os.path.basename(selected_file))[0]
    safe_signals = "_".join(
        s.replace(".", "_").replace("/", "_") for s in plan.get("signals", [])
    )
    operation = plan.get("operation", "plot")
    output_filename = f"{base_name}_{operation}_{safe_signals}.png"
    output_path = os.path.join(output_dir, output_filename)

    parts = [
        "【任务描述】",
        json.dumps(plan, ensure_ascii=False, indent=2),
        "",
        "【可用工具函数】",
        tools_desc,
        "",
        "【项目路径信息】",
        f"MF4 文件路径: {selected_file}",
        f"Tool Scripts 目录: {tools_dir}",
        f"输出目录: {output_dir}",
        f"输出图片路径: {output_path}",
        "",
        "【导入规则】每个函数从同名 .py 文件导入，禁止编造模块名：",
        f"  import sys",
        f"  sys.path.insert(0, r'{tools_dir}')",
        f"  from extract_signal import extract_signal",
        f"  from cross_reference import cross_reference  # res[0]['timestamp']['triggers']['targets']",
        f"  from plot_signals import plot_signals",
        "",
        "请根据以上信息生成 Python 代码。",
    ]

    if error_context:
        parts.insert(
            0,
            f"【错误修正模式】上一次代码执行失败，错误信息：\n{error_context}\n",
        )

    return "\n".join(parts)


def coder_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Coder 节点：根据 plan 生成可执行 Python 代码。

    Args:
        state: 当前 ProcessorState。

    Returns:
        更新后的 state 字典（部分更新），包含 generated_code。
    """
    print("[Coder] 开始生成代码...")

    prompts = _load_prompts()
    system_prompt = prompts["coder"]["system"]

    plan = state.get("plan", {})
    selected_file = state["selected_file"]
    data_dir = state.get("data_dir", "")

    # 判断是否为重试模式
    is_retry = state.get("retries", 0) > 0
    error_context = ""

    if is_retry:
        exec_result = state.get("execution_result", {})
        error_context = exec_result.get("error", "")
        if not error_context:
            error_context = exec_result.get("output", "")

        # 使用重试 Prompt
        retry_template = prompts["coder"]["retry"]
        system_prompt = retry_template.format(error_message=error_context)
        print(f"[Coder] 重试模式，错误信息: {error_context[:200]}...")

    # 构建用户消息
    user_message = _build_coder_prompt(
        plan, selected_file, data_dir, error_context if is_retry else ""
    )

    # 调用 LLM
    try:
        client = _create_llm_client()
        model = os.getenv("CODER_MODEL", "deepseek-v4-pro")

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            temperature=0.2,
            max_tokens=4000,
        )

        response_text = response.choices[0].message.content or ""
        print(f"[Coder] LLM 响应长度: {len(response_text)} 字符")

    except Exception as e:
        # LLM 调用失败时返回重试信息，让 workflow 处理
        return {
            "generated_code": None,
            "execution_result": {
                "success": False,
                "output": "",
                "images": [],
                "error": f"LLM 调用失败: {str(e)}",
            },
        }

    # 清洗代码（去除 markdown 标记）
    code = _strip_markdown_fences(response_text)

    if not code:
        return {
            "generated_code": None,
            "execution_result": {
                "success": False,
                "output": "",
                "images": [],
                "error": "LLM 未生成有效代码，请重试。",
            },
        }

    print(f"[Coder] 代码生成完成，共 {len(code)} 字符")
    return {"generated_code": code}
