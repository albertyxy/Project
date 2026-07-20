# TraceLens - AI Agent for MF4 Signal Analysis

## 1. 项目概述

**目标**：用户通过自然语言描述需求，Agent 自动从 MF4 源数据中提取信号、检测边沿变化、生成可视化图片。

**核心链路**：`用户选择MF4文件 + 自然语言需求 → Planner(LLM) → Coder(LLM) → Executor(代码执行) → 结束/重试`

**参考**：
- 工具层使用 `Tool Scripts/` 中的 4 个模块，Agent 层通过 LangGraph 编排调用

---

## 2. 最终项目文件结构

```
MF4 Processor/
├── data/                              # MF4 源数据文件（已有）
│   ├── measure_USS_04.mf4
│   └── ...
│
├── Tool Scripts/                      # 工具层（已有，不修改）
│   ├── list_signals.py                # 列出 MF4 中所有信号名
│   ├── extract_signal.py              # 提取指定信号数据
│   ├── extract_around_edges.py        # 边沿检测 + 窗口提取
│   └── plot_signals.py               # 多信号曲线绘制
│
├── agent/                             # Agent 层（新建）
│   ├── __init__.py
│   ├── state.py                       # LangGraph State 定义
│   ├── prompts.yaml                   # 所有 Prompt 模板（YAML 统一管理）
│   ├── planner.py                     # Planner 节点：NL → 结构化任务
│   ├── coder.py                       # Coder 节点：任务 → Python 代码
│   ├── executor.py                    # Executor 节点：执行代码、捕获结果
│   ├── tools_description.py           # 将 Tool Scripts 的函数签名转为 LLM 可读的工具描述
│   ├── sandbox.py                     # 代码安全执行沙箱
│   └── workflow.py                    # LangGraph 工作流组装 + 编译
│
├── web/                               # Streamlit 前端（新建）
│   └── app.py                         # Streamlit 交互式网页入口
│
├── output/                            # 生成的图片输出目录（已有）
├── .env                               # API Key 配置（OPENAI_API_KEY, OPENAI_API_BASE）
├── demo.py                            # 手动命令行演示脚本（已有）
└── PLAN.md                            # 本文件
```

---

## 3. Architecture 设计

### 3.1 LangGraph Workflow 图

```
                    +-----------+
                    |   START   |
                    +-----+-----+
                          |
                          v
                    +-----+------+
                    |   Planner   |  LLM: NL → 结构化任务
                    |  (assess)   |  输出: plan 或 追问
                    +-----+------+
                          |
              +-----------+-----------+
              |                       |
         需求清晰                  需求模糊
              |                       |
              v                       v
        +-----+------+          +----+----+
        |   Coder     |          | 追问用户 |  ← Streamlit 展示问题
        |  (generate) |          | (interact) |   等待用户补充
        +-----+------+          +----+----+
              |                       |
              v                       v
        +-----+------+          重新进入 Planner
        |  Executor   |          （携带补充信息）
        |  (execute)  |
        +-----+------+
              |
  +-----------+-----------+
  |                       |
成功/完成              失败/异常
  |                       |
  v                       v
+--+---+            +----+----+
|  END |            | 重试?   |
+------+            | retries |
                    | < max   |
                    +----+----+
                         |
                +--------+--------+
                |                  |
            是 (retries<max)   否 (retries>=max)
                |                  |
                v                  v
           +----+------+      +----+----+
           |   Coder   |      |  END    |
           | (重试+错误) |     | (返回错误)|
           +-----------+      +---------+
```

### 3.2 State 定义

```python
class ProcessorState(TypedDict):
    # === 输入 ===
    user_query: str                           # 用户自然语言输入
    selected_file: str                        # 用户选择的 MF4 文件路径（必选）
    data_dir: str                             # MF4 数据目录

    # === Planner 输出 ===
    plan: Optional[Dict[str, Any]]            # 结构化任务 {"signals": [...], "operation": str, "params": {...}}
    plan_reasoning: Optional[str]             # Planner 的推理过程
    needs_clarification: bool                 # 是否需要向用户追问（需求模糊时为 True）
    clarification_question: Optional[str]     # 追问内容

    # === Coder 输出 ===
    generated_code: Optional[str]             # LLM 生成的 Python 代码

    # === Executor 输出 ===
    execution_result: Optional[Dict[str, Any]]  # {"success": bool, "output": str, "images": [...], "error": str}
    retries: int                              # 当前重试次数
    max_retries: int                          # 最大重试次数（默认 2）

    # === 消息历史 ===
    messages: List[Dict[str, Any]]            # 错误上下文（用于重试时传递错误信息）
```

### 3.3 各节点职责

#### 3.3.1 Planner 节点 (`agent/planner.py`)

**对应参考**：`assess_query()` 函数

**职责**：将用户的自然语言需求解析为结构化的操作计划。

**LLM**：`qwen3.7-plus`（OpenAI 兼容 API）

**Prompt 核心要点**：
- 描述可用的操作类型：`list_signals`、`extract_signal`、`extract_around_edges`、`plot_signals`
- 描述 `selected_file` 下的可用信号（调用 `list_signals` 获取）
- 要求 LLM 输出结构化 JSON，包含：信号筛选、操作类型、参数（文件路径由系统注入，无需 Planner 输出）

**输入**：`user_query` + `selected_file` 的信号列表
**输出**：
- 需求清晰 → `plan` (JSON)
- 需求模糊 → `needs_clarification=True` + `clarification_question`（向用户追问缺失信息）

**模糊场景处理**：
- 用户未指明信号名 → 列出可用信号，请用户选择
- 用户提到的信号名不在文件中 → 提示不匹配，列出相似名称
- 用户操作意图不清 → 追问是"看波形"还是"分析边沿"
- 时间范围模糊（如"最近一段"）→ 询问具体秒数

**示例交互**：
```
用户: "帮我看一下波形"（已选择 measure_USS_04.mf4）
→ Planner: needs_clarification=True, question="请指定要查看的信号名称。文件中可用信号包括：EPS_StgTq.Val, LWI_AgStgWhl.Val, ..."

用户: "看 EPS_StgTq.Val 从 10s 到 30s"
→ Planner: {"signals": ["EPS_StgTq.Val"], 
            "operation": "plot", "params": {"start_time": 10, "end_time": 30, "mode": "overlay"}}

用户: "分析 USS_DALatHODInterpretation_en.Val 到 strong_grip_4 的跳变"（已选择 measure_USS_18_Action01.mf4）
→ Planner: {"signals": ["USS_DALatHODInterpretation_en.Val"],
            "operation": "edges", "params": {"target_state": "strong_grip_4", "window_before": 1.0, "window_after": 2.0}}
```

#### 3.3.2 Coder 节点 (`agent/coder.py`)

**职责**：根据 Planner 的结构化任务 + 工具函数签名，生成可执行的 Python 代码。

**LLM**：`deepseek-v4-pro`（DeepSeek）

**Prompt 核心要点**：
- 注入 4 个工具函数的完整签名和 docstring（从 `tools_description.py` 获取）
- 注入项目路径信息（`data_dir`、`output_dir`、`Tool Scripts` 导入方式）
- 明确输出要求：仅输出 Python 代码，不要解释文字
- 代码要求：导入 `Tool Scripts` 模块 → 调用函数 → 保存图片到指定路径 → print 结果

**输入**：`plan` + 工具描述 + 错误上下文（重试时）
**输出**：`generated_code` (纯 Python 代码字符串)

**代码生成模板示例**：
```python
import sys, os
sys.path.insert(0, r"{agent_dir}\..\Tool Scripts")
from extract_signal import extract_signal
from plot_signals import plot_signals

timestamps, samples = extract_signal(
    r"{selected_file}", "EPS_StgTq.Val", 10, 30
)
path = plot_signals(
    {"EPS_StgTq.Val": (timestamps, samples)},
    title="EPS_StgTq.Val",
    output_path=r"{output_dir}\result.png",
    mode="overlay"
)
print(f"SUCCESS:{path}")
```

#### 3.3.3 Executor 节点 (`agent/executor.py`) + 沙箱 (`agent/sandbox.py`)

**职责**：安全执行 Coder 生成的代码，捕获输出和错误。

**安全措施**（`agent/sandbox.py`）：
- 将生成的代码写入临时 `.py` 文件，通过 `subprocess.run()` 在独立子进程中执行
- 子进程隔离提供与主进程完全隔离的执行环境，避免污染主进程状态
- 设置子进程超时（默认 30 秒），超时自动终止
- 捕获子进程的 stdout/stderr，执行完毕后自动清理临时文件
- 从 stdout 中解析 `SUCCESS:` 标记提取生成的图片路径

**输入**：`generated_code`
**输出**：`execution_result` - `{"success": bool, "output": str, "images": [...], "error": str}`

#### 3.3.4 条件路由

```python
def after_planner(state) -> str:
    if state["needs_clarification"]:
        return "clarify"    # 需求模糊，向用户追问
    return "coder"          # 需求清晰，生成代码

def after_executor(state) -> str:
    if state["execution_result"]["success"]:
        return "end"
    if state["retries"] < state["max_retries"]:
        return "coder"      # 回到 Coder，附带错误信息
    return "end"            # 重试上限已到，返回错误
```

---

## 4. 实施步骤

### Step 1：工具描述生成器 (`agent/tools_description.py`)

- 通过 AST 解析 `Tool Scripts/` 下 4 个模块的函数签名、参数类型、docstring（避免 import asammdf 等重依赖）
- 格式化为 LLM 可理解的文本描述
- 暴露 `get_tools_description()` 获取完整工具描述（供 Coder 使用）
- 暴露 `get_tools_summary()` 获取简要摘要（供 Planner 参考）
- 暴露 `get_tool_scripts_dir()` 获取 Tool Scripts 绝对路径

### Step 2：State 定义 (`agent/state.py`)

- 定义 `ProcessorState(TypedDict)`
- 定义 `ExecutionResult` 等辅助类型

### Step 3：Prompt 模板 (`agent/prompts.yaml`)

- 所有 Prompt 统一在 YAML 文件中管理，结构如下：
  ```yaml
  planner:
    system: |
      你是一个 MF4 信号分析任务规划器。
      你的任务是将用户的自然语言需求解析为结构化 JSON 任务描述。
      
      你会收到以下信息：
      - 用户需求（自然语言）
      - 当前所选 MF4 文件中所有可用的信号名称列表
      
      你需要输出一个 JSON，包含：
      - signals: 用户提到的信号名称列表（从可用信号列表中模糊匹配）
       - operation: 操作类型，可选值：
           "plot"     - 绘制信号波形图
           "edges"    - 检测信号边沿变化
       - params: 操作参数，根据 operation 不同：
           plot 参数: start_time(可选), end_time(可选), mode("overlay"|"split", 默认"overlay")
           edges 参数: edge_type("rising"|"falling"|"both", 默认"rising"), window_before(默认1.0), 
                      window_after(默认2.0), target_state(可选, 筛选目标状态)
       
       如果用户需求信息不足（无信号名、信号名不匹配、操作意图不清、时间范围模糊），
       不要猜测，输出一个 JSON 包含：
       - needs_clarification: true
       - question: 向用户追问的具体问题（自然语言）

       输出格式：纯 JSON，不要包含任何解释文字。

  coder:
    system: |
      你是一个 Python 代码生成器。
      你的任务是根据结构化任务描述和工具函数签名，生成可执行、可打印的 Python 代码。
      
      你会收到以下信息：
      - 结构化任务 JSON（包含目标信号、操作类型、参数）
      - 可用工具函数的完整签名和 docstring（共 4 个：list_signals / extract_signal / 
        extract_around_edges / plot_signals）
      - 项目路径（MF4 文件路径、Tool Scripts 路径、输出目录路径）
      
      代码要求：
      - 导入 Tool Scripts 中的模块
      - 调用对应函数，传入任务参数
      - 枚举型信号无需特殊处理（plot_signals 已自动兼容）
      - 所有结果 print 到 stdout，格式：
        成功: print(f"SUCCESS:{图片路径}")
        信息: print("...")  # 边沿检测结果等
      - 仅输出 Python 代码，不要任何解释或 markdown 标记
      
    retry: |
      上一次生成的代码执行失败，以下是错误信息：
      {error_message}
      
      请根据错误信息修正代码。仅输出修正后的 Python 代码，不要其他内容。
  ```
- Planner / Coder 节点从 YAML 中加载对应 Prompt，通过 `str.format()` 注入动态参数
- **注意**：工具函数签名由 `tools_description.py` 动态注入到 Coder 的 Prompt 中，不写在 YAML 里

### Step 4：Planner 节点 (`agent/planner.py`)

- 实现 `planner_node(state) -> dict`
- 调用 `list_signals(selected_file)` 获取当前文件的信号列表，注入 Prompt
- 调用 LLM（`qwen3.7-plus`，OpenAI 兼容 API，通过 `.env` 中 `PLANNER_*` 变量配置）
- 解析 JSON 输出，区分两种结果：
  - 需求清晰 → 填充 `plan`，设置 `needs_clarification=False`
  - 需求模糊 → 设置 `needs_clarification=True`，填充 `clarification_question`
- 对 LLM 输出的 plan 进行后验证：信号名不为空、operation 在合法范围内
- 处理 JSON 解析失败（兜底：追问用户重新描述需求）
- 处理 `list_signals` 调用失败（文件损坏等异常，返回追问提示）

### Step 5：Coder 节点 (`agent/coder.py`)

- 实现 `coder_node(state) -> dict`
- 调用 LLM（`deepseek-v4-pro`，DeepSeek API）
- 注入工具描述 + plan + 错误上下文
- 从 LLM 响应中提取纯 Python 代码（去除 markdown 代码块标记）

### Step 6：沙箱 + Executor (`agent/sandbox.py` + `agent/executor.py`)

- `sandbox.py`：将代码写入临时 `.py` 文件，通过 `subprocess.run()` 在独立子进程中执行
  - 捕获 stdout/stderr，超时自动终止（默认 30 秒）
  - 从 stdout 中解析 `SUCCESS:` 标记提取图片路径
  - 执行完毕后自动清理临时文件
- `executor.py`：`executor_node(state) -> dict`，调用沙箱执行代码，返回执行结果并递增 retries 计数

### Step 7：工作流组装 (`agent/workflow.py`)

- 使用 LangGraph `StateGraph` 组装节点：planner → (coder / clarify) → executor
- 添加条件边：
  - planner → `_after_planner` → coder 或 clarify
  - executor → `_after_executor` → END 或 coder（重试）
- clarify 节点 → END（返回追问内容给 Streamlit，等待用户补充后重新进入）
- 暴露 `create_workflow()` 编译工作流，`run_agent(user_query, selected_file, data_dir=None, max_retries=2)` 作为外部调用入口

### Step 8：Streamlit 前端 (`web/app.py`)

- 单页面交互：
  - 顶部：标题 + 说明
  - 侧边栏：文件选择区（下拉框选择 `data/` 目录下的 MF4 文件），文件切换自动清空对话历史
  - 主区域：对话历史展示（聊天消息样式，区分 user/assistant 角色）
  - 输入区：底部 `chat_input`，根据是否处于追问状态切换 placeholder 提示文字
- 交互循环：`st.session_state` 中维护 `chat_history`、`awaiting_clarification`、`pending_state` 等状态
  - Planner 返回追问时，显示问题并暂停等待用户输入，用户回复后拼接到原 query 重新走全流程
  - 成功时内联展示图片（markdown 渲染），失败时展示错误信息和生成代码（expander 折叠）
- 调用 `agent/workflow.py` 的 `run_agent(user_query, selected_file)` 获取结果

### Step 9：集成测试

- 用 `demo.py` 中的典型命令作为测试用例
- 验证 Planner 能正确解析各种自然语言表达
- 验证 Coder 生成的代码能正确执行
- 验证 Streamlit 页面交互正常

---

## 5. 关键技术决策

| 决策点 | 方案 | 理由 |
|--------|------|------|
| LLM 选型 | Planner: `qwen3.7-plus`，Coder: `deepseek-v4-pro`；统一通过 OpenAI 兼容 API 调用，API Key 存放于 `.env` | Planner 任务简单用通义，Coder 代码生成用 DeepSeek；统一的 API 框架降低接入复杂度 |
| 代码生成方式 | LLM 生成完整 Python 代码 | 比 Function Calling 更灵活，能处理复杂组合逻辑 |
| 重试机制 | 最多 2 次重试，附带错误信息 | 大多数语法/逻辑错误一次更正即可修复 |
| 沙箱安全 | `subprocess.run()` 子进程隔离 | 进程级隔离比 `exec()` 更安全，不污染主进程状态，无需 Docker |
| Streamlit 状态管理 | `st.session_state` | Streamlit 原生方案，无需额外状态库 |
| Planner 的文件发现 | 用户通过下拉框直接选择文件 + `list_signals` 获取该文件信号列表 | 文件选择由前端完成，Planner 只需知道当前文件的信号名 |

---

## 6. 风险与注意事项

1. **LLM 生成代码质量不稳定**：Coder 可能生成语法错误或错误调用。**缓解**：重试机制 + 明确的 Prompt 约束 + 提供完整的工具签名
2. **MF4 文件较大，读取耗时**：**缓解**：在 Executor 中设置 30s 超时，避免前端卡死
3. **枚举型信号的特殊处理**：`plot_signals` 已内部处理，Coder 无需感知，但 Prompt 中需要注明"无需区分数值型/枚举型"
4. **安全性**：LLM 生成的代码在子进程中执行。**缓解**：`subprocess.run()` 提供进程级隔离，超时自动终止，临时文件自动清理
