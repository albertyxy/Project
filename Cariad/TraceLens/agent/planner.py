# -*- coding: utf-8 -*-
"""Planner 节点：将用户自然语言需求解析为结构化任务。"""

import json
import os
import re
import sys
from typing import Dict, Any

import yaml
from openai import OpenAI
from dotenv import load_dotenv

# 加载 .env 配置
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

# Tool Scripts 导入
_TOOL_SCRIPTS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Tool Scripts")
)
if _TOOL_SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _TOOL_SCRIPTS_DIR)
from list_signals import list_signals


def _load_prompts() -> Dict[str, Any]:
    """加载 prompts.yaml 配置"""
    yaml_path = os.path.join(os.path.dirname(__file__), "prompts.yaml")
    with open(yaml_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _create_llm_client() -> OpenAI:
    """创建 Planner LLM 客户端（OpenAI 兼容 API）"""
    api_key = os.getenv("PLANNER_API_KEY", "")
    api_base = os.getenv("PLANNER_API_BASE", "https://api.openai.com/v1")

    if not api_key or api_key == "your_planner_api_key_here":
        raise ValueError(
            "请在 .env 文件中配置 PLANNER_API_KEY（Planner 使用的 LLM API Key）"
        )

    return OpenAI(api_key=api_key, base_url=api_base)


def _extract_json(text: str) -> str:
    """从 LLM 响应中提取 JSON 字符串。

    处理 LLM 可能包裹的 markdown 代码块标记。
    """
    text = text.strip()

    # 去除 markdown 代码块
    if text.startswith("```"):
        lines = text.split("\n")
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()

    return text


def _parse_planner_response(response_text: str) -> Dict[str, Any]:
    """解析 Planner LLM 的 JSON 响应。

    返回格式:
        - 需求清晰: {"needs_clarification": False, "plan": {...}, ...}
        - 需求模糊: {"needs_clarification": True, "clarification_question": "...", ...}
        - 解析失败: {"needs_clarification": True, "clarification_question": "..."}
    """
    try:
        text = _extract_json(response_text)
        data = json.loads(text)

        # 检查是否是模糊需求格式
        if data.get("needs_clarification"):
            return {
                "needs_clarification": True,
                "clarification_question": data.get(
                    "question",
                    "请更详细地描述您的需求。",
                ),
                "plan": None,
                "plan_reasoning": None,
            }

        # 需求清晰格式
        plan = {
            "signals": data.get("signals", []),
            "operation": data.get("operation", ""),
            "params": data.get("params", {}),
        }

        # 验证必要字段
        if not plan["signals"]:
            return {
                "needs_clarification": True,
                "clarification_question": "未能识别您提到的信号名称，请重新描述。",
                "plan": None,
                "plan_reasoning": None,
            }

        if plan["operation"] not in ("plot", "edges"):
            return {
                "needs_clarification": True,
                "clarification_question": (
                    f"无法识别的操作类型 '{plan['operation']}'。"
                    "支持的操作：plot（绘制波形图）、edges（边沿检测分析）。"
                ),
                "plan": None,
                "plan_reasoning": None,
            }

        return {
            "needs_clarification": False,
            "clarification_question": None,
            "plan": plan,
            "plan_reasoning": data.get("reasoning", ""),
        }

    except (json.JSONDecodeError, TypeError) as e:
        return {
            "needs_clarification": True,
            "clarification_question": (
                "无法理解您的需求描述，请用更清晰的方式重新说明：\n"
                "例如：'请绘制信号 XXX 从 10s 到 30s 的波形' 或 '分析信号 XXX 的边沿跳变'"
            ),
            "plan": None,
            "plan_reasoning": None,
        }


def planner_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Planner 节点：分析用户需求，生成结构化任务或追问。

    Args:
        state: 当前 ProcessorState。

    Returns:
        更新后的 state 字典（部分更新）。
    """
    print("[Planner] 开始分析用户需求...")

    prompts = _load_prompts()
    system_prompt = prompts["planner"]["system"]

    selected_file = state["selected_file"]
    user_query = state["user_query"]

    # 获取文件中的信号列表
    try:
        signals = list_signals(selected_file)
    except Exception as e:
        return {
            "needs_clarification": True,
            "clarification_question": (
                f"无法读取所选文件中的信号列表。\n错误信息: {str(e)}\n"
                "请检查文件是否有效，或选择其他文件。"
            ),
        }

    if not signals:
        return {
            "needs_clarification": True,
            "clarification_question": (
                "所选文件中未检测到任何信号，请检查文件是否有效。"
            ),
        }

    # 构建用户消息
    signals_str = "\n".join(f"  - {s}" for s in signals)
    user_message = (
        f"【用户需求】\n{user_query}\n\n"
        f"【可用信号列表】（共 {len(signals)} 个）\n{signals_str}"
    )

    # 调用 LLM
    try:
        client = _create_llm_client()
        model = os.getenv("PLANNER_MODEL", "qwen3.7-plus")

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            temperature=0.3,
            max_tokens=2000,
        )

        response_text = response.choices[0].message.content or ""
        print(f"[Planner] LLM 响应: {response_text[:300]}...")

    except Exception as e:
        return {
            "needs_clarification": True,
            "clarification_question": (
                f"LLM 调用失败: {str(e)}\n请检查 .env 中的 API 配置是否正确。"
            ),
        }

    result = _parse_planner_response(response_text)
    print(f"[Planner] 分析结果: needs_clarification={result['needs_clarification']}")

    return result
