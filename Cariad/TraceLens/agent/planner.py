# -*- coding: utf-8 -*-
"""Planner 节点：将用户自然语言需求解析为结构化任务。

信号匹配在代码侧预处理完成（非 LLM 职责），避免将全量信号名塞入 Prompt
导致大文件 token 超限。
"""

import json
import os
import re
import sys
from typing import Dict, Any, List, Tuple, Optional

import yaml
from openai import OpenAI
from dotenv import load_dotenv
# 加载 .env 配置
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

from asammdf import MDF

# 精细匹配的信号数上限，超过此值仅发送摘要
_MAX_MATCHED_SIGNALS_FOR_PROMPT = 80


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

        plan = {
            "signals": data.get("signals", []),
            "operation": data.get("operation", ""),
            "params": data.get("params", {}),
        }

        if not plan["signals"]:
            return {
                "needs_clarification": True,
                "clarification_question": "未能识别您提到的信号名称，请重新描述。",
                "plan": None,
                "plan_reasoning": None,
            }

        if plan["operation"] not in ("plot", "edges", "statistics", "find_ranges", "cross_reference"):
            return {
                "needs_clarification": True,
                "clarification_question": (
                    f"无法识别的操作类型 '{plan['operation']}'。"
                    "支持的操作：plot（绘制波形图）、edges（边沿检测分析）、"
                    "statistics（信号统计）、find_ranges（条件查找时间窗口）。"
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

    except (json.JSONDecodeError, TypeError):
        return {
            "needs_clarification": True,
            "clarification_question": (
                "无法理解您的需求描述，请用更清晰的方式重新说明：\n"
                "例如：'请绘制信号 XXX 从 10s 到 30s 的波形' 或 '分析信号 XXX 的边沿跳变'"
            ),
            "plan": None,
            "plan_reasoning": None,
        }


# ---------------------------------------------------------------------------
# 信号名提取与匹配（代码侧预处理，不消耗 LLM token）
# ---------------------------------------------------------------------------

# 从自然语言中提取"可能像信号名"的候选 token
# 支持 C++ struct 嵌套路径：允许连续点 (..) 和点后数字 (.1.)
_SIGNAL_TOKEN_RE = re.compile(r"[A-Za-z_]\w*(?:\.[A-Za-z_0-9]*)+")


def _extract_candidates(user_query: str) -> List[str]:
    """从用户自然语言中提取可能的信号名候选。

    规则：以点分隔的标识符（如 EPS_StgTq.Val）为高置信度候选；
    同时提取不含点的长标识符作为辅助候选。
    """
    # 主正则：含点的完整信号名（高置信度）
    primary = _SIGNAL_TOKEN_RE.findall(user_query)

    if primary:
        # 有完整信号名 → 不再捡碎片，避免短子串污染匹配
        seen = set()
        unique = []
        for c in primary:
            if c.lower() not in seen:
                seen.add(c.lower())
                unique.append(c)
        return unique

    # 次级正则：主正则无命中时，提取短关键词用于搜索
    words = re.findall(r"[A-Za-z_][A-Za-z0-9_]{2,}", user_query, flags=re.ASCII)
    candidates = []
    for w in words:
        if not w.isdigit():
            candidates.append(w)

    seen = set()
    unique = []
    for c in candidates:
        if c.lower() not in seen:
            seen.add(c.lower())
            unique.append(c)
    return unique


# 发现类查询的匹配模式（不需要走 LLM）
_DISCOVERY_PATTERNS = [
    re.compile(p)
    for p in [
        r"有哪些信号",
        r"有什么信号",
        r"信号列表",
        r"列出信号",
        r"搜索.*信号",
        r"查找.*信号",
        r"包含.*信号",
        r"list\s+signals",
        r"search\s+signals",
        r"查找\w+相关",
        r"\w+相关信号",
        r"帮我看[看下].*文件.*有哪些",
    ]
]


def _is_discovery_query(user_query: str) -> bool:
    """判断是否为信号发现类查询（"有哪些XX信号"）。"""
    return any(p.search(user_query) for p in _DISCOVERY_PATTERNS)


def _search_channels(
    signal_names: List[str], keyword: str
) -> List[str]:
    """在信号名列表中按关键词搜索匹配的信号名。

    大小写不敏感子串匹配。
    """
    kw = keyword.lower()
    return [name for name in signal_names if kw in name.lower()]


def _is_specific_name(candidate: str) -> bool:
    """判断候选是否为完整信号名（而非搜索关键词）。

    完整信号名特征：长度 >= 15 或含点，是用户明确指定的目标信号。
    短关键词（如 WBA、ESP）视为搜索关键词，允许子串匹配。
    """
    return len(candidate) >= 15 or "." in candidate


def _match_candidates(
    signal_names: List[str], candidates: List[str]
) -> Tuple[List[str], List[str]]:
    """在信号名列表中匹配候选信号名。

    匹配策略（按优先级）：
    1. 精确匹配
    2. 大小写不敏感精确匹配
    3. 仅对短关键词做子串匹配；长候选（完整信号名）匹配失败直接标记未找到

    Returns:
        (matched_signals, not_found_candidates)
    """
    lower_map = {name.lower(): name for name in signal_names}
    matched: List[str] = []
    not_found: List[str] = []

    for candidate in candidates:
        found = False

        # 1. 精确匹配
        if candidate in signal_names:
            matched.append(candidate)
            found = True
        else:
            # 2. 大小写不敏感
            cand_lower = candidate.lower()
            if cand_lower in lower_map:
                matched.append(lower_map[cand_lower])
                found = True

        if found:
            continue

        # 3. 子串匹配（仅短关键词）
        if not _is_specific_name(candidate):
            sub_matches = [n for n in signal_names if candidate.lower() in n.lower()]
            if sub_matches:
                sub_matches.sort(key=len)
                matched.extend(sub_matches[:20])
                found = True

        if not found:
            not_found.append(candidate)

    # 去重保序
    seen = set()
    unique_matched = []
    for m in matched:
        if m not in seen:
            seen.add(m)
            unique_matched.append(m)

    return unique_matched, not_found


def _discovery_response(
    user_query: str, signal_names: List[str]
) -> Dict[str, Any]:
    """处理信号发现类查询：提取关键词搜索并返回摘要。"""
    candidates = _extract_candidates(user_query)

    if candidates:
        # 有关键词：搜索匹配
        all_matched: List[str] = []
        for c in candidates:
            all_matched.extend(_search_channels(signal_names, c))
        matched = list(dict.fromkeys(all_matched))  # 去重保序
    else:
        matched = []

    if not matched:
        return {
            "needs_clarification": True,
            "clarification_question": (
                f"文件中共有 {len(signal_names)} 个信号。\n"
                "请在 query 中指定关键词以搜索信号，例如：'WBA相关信号有哪些' 或 '搜索 ESP'。"
            ),
        }

    total_signals = len(signal_names)
    matched_count = len(matched)

    if matched_count <= 80:
        signal_list = "\n".join(f"  - {s}" for s in matched)
        return {
            "needs_clarification": True,
            "clarification_question": (
                f"文件共 {total_signals} 个信号，匹配到 {matched_count} 个：\n\n"
                f"{signal_list}\n\n"
                "请选择需要分析的信号，描述具体需求（如：绘制XX从10s到30s的波形）。"
            ),
        }

    # 匹配太多 → 显示摘要
    preview = "\n".join(f"  - {s}" for s in matched[:30])
    return {
        "needs_clarification": True,
        "clarification_question": (
            f"文件共 {total_signals} 个信号，匹配到 {matched_count} 个。\n\n"
            f"前 30 个：\n{preview}\n\n"
            "匹配结果较多，建议用更具体的关键词缩小范围。"
        ),
    }


# ---------------------------------------------------------------------------
# Planner 节点
# ---------------------------------------------------------------------------


def planner_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Planner 节点：分析用户需求，生成结构化任务或追问。

    预处理流程：
    1. 读取 channels_db 获取信号名（不触发 VLSD 数据块解析）
    2. 从 query 提取候选信号名
    3. 发现类查询 → 直接搜索返回摘要
    4. 候选匹配 → 只将匹配结果发给 LLM
    5. 无候选 → 追问
    """
    print("[Planner] 开始分析用户需求...")

    prompts = _load_prompts()
    system_prompt = prompts["planner"]["system"]

    selected_file = state["selected_file"]
    user_query = state["user_query"]

    # 1. 读取 channels_db
    if not os.path.isfile(selected_file):
        return {
            "needs_clarification": True,
            "clarification_question": (
                f"文件不存在: {selected_file}\n请检查文件路径。"
            ),
        }

    try:
        with MDF(selected_file) as mdf:
            # channels_db 是代理对象，MDF close 后会被清空，必须在 with 块内转为 list
            signal_names = list(mdf.channels_db.keys())
    except Exception as e:
        return {
            "needs_clarification": True,
            "clarification_question": (
                f"无法读取 MF4 文件: {selected_file}\n"
                f"错误详情: {e}\n请检查文件是否有效。"
            ),
        }

    if not signal_names:
        return {
            "needs_clarification": True,
            "clarification_question": "所选文件中未检测到任何信号。",
        }

    total_signals = len(signal_names)
    print(f"[Planner] 文件包含 {total_signals} 个信号")

    # 2. 提取候选信号名
    candidates = _extract_candidates(user_query)
    print(f"[Planner] 从 query 提取候选: {candidates}")

    # 3. 发现类查询
    if _is_discovery_query(user_query):
        print("[Planner] 检测为发现类查询，不走 LLM")
        return _discovery_response(user_query, signal_names)

    # 4. 候选匹配
    if not candidates:
        # query 中没有任何看起来像信号名的东西
        if total_signals <= 80:
            # 小文件：全量发给 LLM
            signal_list = "\n".join(f"  - {s}" for s in signal_names)
        else:
            return {
                "needs_clarification": True,
                "clarification_question": (
                    f"文件中共有 {total_signals} 个信号，数量较多。\n"
                    "请在描述中包含信号名称（如'绘制 EPS_StgTq.Val 的波形'）"
                    "或指定关键词搜索（如'WBA相关信号有哪些'）。"
                ),
            }
    else:
        matched, not_found = _match_candidates(signal_names, candidates)
        print(f"[Planner] 匹配到 {len(matched)} 个信号，未匹配: {not_found}")

        if not matched:
            # 候选全部未命中
            if total_signals <= 80:
                signal_list = "\n".join(f"  - {s}" for s in signal_names)
                not_found_hint = (
                    f"您提到的信号名（{', '.join(not_found)}）在文件中未找到。"
                    f"以下是文件中所有 {total_signals} 个信号：\n\n{signal_list}\n\n"
                    "请从上述列表中选择正确的信号名。"
                )
                return {
                    "needs_clarification": True,
                    "clarification_question": not_found_hint,
                }
            else:
                # 根据候选类型给出不同建议
                specific_hint = ""
                if any(_is_specific_name(c) for c in not_found):
                    specific_hint = (
                        "\n提示：您输入的是完整信号名，但未在文件中精确匹配。"
                        "请检查拼写是否与文件中的信号名完全一致。"
                    )
                not_found_hint = (
                    f"您提到的信号名（{', '.join(not_found)}）在文件"
                    f"（共 {total_signals} 个信号）中未找到。{specific_hint}\n"
                    "也可使用关键词搜索：'搜索 <关键词>'。"
                )
                return {
                    "needs_clarification": True,
                    "clarification_question": not_found_hint,
                }

        # 构建发给 LLM 的信号列表
        if len(matched) <= _MAX_MATCHED_SIGNALS_FOR_PROMPT:
            signal_list = "\n".join(f"  - {s}" for s in matched)
            signal_count_note = f"已匹配 {len(matched)} 个信号"
        else:
            signal_list = "\n".join(f"  - {s}" for s in matched[:80])
            signal_count_note = (
                f"已匹配 {len(matched)} 个信号（仅展示前 80 个）"
            )

        if not_found:
            signal_count_note += (
                f"，未匹配: {', '.join(not_found)}"
            )

    # 5. 构建用户消息 → 调用 LLM
    user_message = (
        f"【用户需求】\n{user_query}\n\n"
        f"【文件信号统计】共 {total_signals} 个信号，{signal_count_note}\n\n"
        f"【匹配到的信号列表】\n{signal_list}"
    )

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
