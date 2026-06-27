# USS Report Agent 开发计划

## 一、项目概述

基于 OpenManus-cy 框架，开发**PPT 报告自动生成功能**。用户通过 `python main.py` 启动后，直接说"帮我做 XXX 的测试报告"，Agent 自动找到对应数据并基于统一模板生成报告。

### 目录结构

```
USS Data/
├── USSDB Test Report Template.pptx              ← 统一模板（所有报告共用）
├── Q6 etron USSDB R4.1 Test/                    ← 测试项目数据
│   ├── Q6_TF094_0662_USSDB_TS_FCT_USS_4.mf4     ← 原始测量数据（报告生成不使用）
│   ├── Q6_TF094_0662_USSDB_TS_FCT_USS_7.mf4
│   ├── ...（共10个 .mf4 文件）
│   ├── TS_FCT_USS_4/                             ← 与 Slide 3 对应
│   │   └── 01.PNG ~ 04.PNG
│   ├── TS_FCT_USS_7/                             ← 与 Slide 4 对应
│   │   └── 01.PNG ~ 04.PNG
│   ├── TS_FCT_USS_8/                             ← 与 Slide 5 对应
│   │   └── 01.PNG ~ 04.PNG
│   ├── TS_FCT_USS_9/                             ← 与 Slide 6 对应
│   │   └── 01.PNG ~ 02.PNG
│   ├── TS_FCT_USS_37/                            ← 与 Slide 7 对应
│   │   └── 01.PNG
│   ├── TS_FCT_USS_16/                            ← 与 Slide 8 对应
│   │   └── 01.PNG
│   ├── TS_FCT_USS_18_Action1/                    ← 与 Slide 9-11 对应（3个Slide共享）
│   │   ├── 01.PNG ~ 10.PNG  (图表)
│   │   └── IMG_2951.JPG ~ IMG_2960.JPG  (照片)
│   ├── TS_FCT_USS_18_Action2/                    ← 与 Slide 13 对应
│   │   ├── 01.PNG ~ 06.PNG  (图表)
│   │   └── IMG_2961.JPG ~ IMG_2966.JPG  (照片)
│   ├── TS_FCT_USS_18_Action3/                    ← 与 Slide 15-16 对应（2个Slide共享）
│   │   ├── 01.PNG ~ 08.PNG  (图表)
│   │   └── IMG_2967.JPG ~ IMG_2974.JPG  (照片)
│   └── TS_FCT_USS_18_Action4/                    ← 与 Slide 17 对应
│       ├── 01.PNG ~ 02.PNG  (图表)
│       └── IMG_2975.JPG ~ IMG_2976.JPG  (照片)
```

> **关于 .mf4 文件**：项目目录下有 10 个 .mf4 原始测量数据文件（ASAM MDF 格式），与测试用例一一对应。当前报告生成仅使用已导出的 PNG/JPG 图片，不涉及 .mf4 文件解析。

### 核心场景

```
用户: "帮我做 Q6 etron USSDB R4.1 Test 的测试报告"

Agent 自动:
  1. 扫描 USS Data/ 目录，根据项目名找到对应的数据文件夹
  2. 加载统一模板 USS Data/USSDB Test Report Template.pptx
  3. 分析模板 Slide 结构，匹配数据子文件夹中的图片
  4. 替换图片，生成报告到 workspace/
```

---

## 二、PPT 模板结构分析

经过对模板 PPT 的结构化分析（18 页），详细总结如下：

| Slide | Driver Activity 标识 | 类型 | 图片数 | 对应数据文件夹 | 数据文件数 |
|-------|---------------------|------|--------|--------------|-----------|
| 1 | (无) | 封面 | 0 | -- | -- |
| 2 | (无) | 车辆配置 | 0 | -- | -- |
| 3 | `TS_FCT_USS_4` | 测试结果 | 5 | TS_FCT_USS_4 | 4 PNG |
| 4 | `TS_FCT_USS_7` | 测试结果 | 5 | TS_FCT_USS_7 | 4 PNG |
| 5 | `TS_FCT_USS_8` | 测试结果 | 5 | TS_FCT_USS_8 | 4 PNG |
| 6 | `TS_FCT_USS_9` | 测试结果 | 2 | TS_FCT_USS_9 | 2 PNG |
| 7 | `TS_FCT_USS_37` | 测试结果 | 1 | TS_FCT_USS_37 | 1 PNG |
| 8 | `TS_FCT_USS_16` | 测试结果 | 1 | TS_FCT_USS_16 | 1 PNG |
| 9 | `TS_FCT_USS_18 Action-1` | 测试结果 | 9 | TS_FCT_USS_18_Action1 | 10 PNG + 10 JPG |
| 10 | `TS_FCT_USS_18 Action-1` | 测试结果 | 9 | 同 Action1 | (同上) |
| 11 | `TS_FCT_USS_18 Action-1` | 测试结果 | 9 | 同 Action1 | (同上) |
| 12 | `TS_FCT_USS_18 Action-1 & Action-2` | **跨Action** | 9 | Action1 + Action2 | (共享) |
| 13 | `TS_FCT_USS_18 Action-2` | 测试结果 | 9 | TS_FCT_USS_18_Action2 | 6 PNG + 6 JPG |
| 14 | `TS_FCT_USS_18 Action-2 & Action-3` | **跨Action** | 9 | Action2 + Action3 | (共享) |
| 15 | `TS_FCT_USS_18 Action-3` | 测试结果 | 9 | TS_FCT_USS_18_Action3 | 8 PNG + 8 JPG |
| 16 | `TS_FCT_USS_18 Action-3` | 测试结果 | 9 | 同 Action3 | (同上) |
| 17 | `TS_FCT_USS_18 Action-4` | 测试结果 | 6 | TS_FCT_USS_18_Action4 | 2 PNG + 2 JPG |
| 18 | (无) | 参数概览 | 1 | -- | -- |

### 关键发现

1. **每张测试结果页的 TextBox 中包含测试用例标识**，如：
   - `Driver Activity: TS_FCT_USS_4`
   - `Driver Activity: TS_FCT_USS_18  Action-1`
   - `Driver Activity: TS_FCT_USS_18  Action-1 & Action-2`（跨Action组合页）

2. **图片分为两种类型**：
   - PNG 图片：图表/曲线图
   - JPEG 图片：现场照片（来自 IMG_XXXX.JPG）

3. **Slide 与数据文件夹存在三种映射关系**：

   **类型 A：简单 1:1 映射**（Slide 3-8, 17）
   - 一个 Slide 对应一个数据文件夹，图片按文件名排序后一一替换
   - 注意：Slide 3/4/5 模板有 5 张图但数据仅 4 张，替换时按实际数据文件数量替换，多余模板图片保留不动

   **类型 B：N:1 映射**（Slide 9-11 共享 Action1，Slide 15-16 共享 Action3）
   - 多个 Slide 共享同一个数据文件夹，图片按 Slide 顺序分配：
     - Action1 共 20 张：Slide 9 → Slide 10 → Slide 11 顺序分配
     - Action3 共 16 张：Slide 15 → Slide 16 顺序分配
   - 各 Slide 按模板中实际图片占位数量取对应的图片

   **类型 C：跨文件夹组合映射**（Slide 12, 14）
   - Slide 12：取 Action1 的最后 N 张 + Action2 的前 M 张（N + M = 模板图片数 9）
   - Slide 14：取 Action2 的最后 N 张 + Action3 的前 M 张（N + M = 模板图片数 9）
   - 这种"首尾接续"体现了测试数据的连续性（连续 Action 之间的过渡）

4. **非测试数据页**（Slide 1, 2, 18）：
   - 封面（Slide 1）：标题和作者文字，不需要图片替换
   - 车辆配置（Slide 2）：仅表格，数据可能需要手动填入
   - 参数概览（Slide 18）：1 张图片 + 表格，图片来源待确认

---

## 三、架构设计

### 3.1 整体架构

```
USS Report Agent/
├── app/
│   ├── agent/
│   │   └── manus.py              ← [修改] 添加 PPTReportTool 到工具集
│   ├── tool/
│   │   └── ppt_report_tool.py    ← [新建] PPT 报告工具
│   ├── prompt/
│   │   └── report.yaml           ← [新建] Report 相关 prompt (YAML格式)
│   └── config.py                 ← [修改] 添加 USS Data 路径配置
├── config/
│   └── config.toml               ← [修改] 添加 report 配置段
└── DEVELOPMENT_PLAN.md            ← [本文件]
```

### 3.2 设计原则

- **不新建独立 Agent**：复用 Manus Agent，将 PPTReportTool 加入其工具集即可
- **不新建入口脚本**：用户统一通过 `python main.py` 交互
- **Prompt 用 YAML**：所有提示词写在 `app/prompt/report.yaml` 中，与其他 prompt 风格统一
- **自动发现**：Agent 根据用户描述的项目名，自动在 `USS Data/` 下搜索匹配的目录和模板

### 3.3 依赖新增

在 `requirements.txt` 中新增：
```
python-pptx~=0.6.23
PyYAML~=6.0.2           # 已有
```

---

## 四、详细实现步骤

### Step 1: 创建 `app/prompt/report.yaml`

**目标**：将报告生成相关的提示词集中管理在 YAML 文件中。

**文件位置**：`app/prompt/report.yaml`

**内容设计**：

```yaml
# USS Report Agent - 报告生成相关提示词

system_instruction: |
  你具备 PPT 报告自动生成能力。当用户要求生成测试报告时，你需要：
  1. 根据用户提到的项目名称，在 USS Data 目录下找到对应的项目文件夹
  2. 在该文件夹中找到 .pptx 模板文件
  3. 使用 ppt_report 工具分析模板、建立映射、替换图片
  4. 将生成的报告保存到 workspace 目录

report_workflow: |
  ## PPT报告生成工作流

  当用户要求生成测试报告时，按以下步骤执行：

  ### Step 1: 定位项目
  使用 ppt_report 工具的 `find_project` 操作，传入用户提到的项目名称。
  工具会自动在 USS Data 目录下搜索匹配的文件夹，返回模板路径和数据路径。

  ### Step 2: 分析模板
  使用 ppt_report 工具的 `analyze_template` 操作，分析模板 PPT 的结构。
  确认 Slide 数量、每页的测试用例标识、图片数量等信息。

  ### Step 3: 建立映射
  使用 ppt_report 工具的 `build_mapping` 操作，自动匹配 Slide 中的测试用例标识
  与数据子文件夹名称。工具会自动识别三种映射类型：
  - 类型 A: 简单 1:1 映射（一个 Slide 对应一个文件夹）
  - 类型 B: N:1 共享映射（多个连续 Slide 共用同一文件夹，顺序分配图片）
  - 类型 C: 跨文件夹组合映射（Slide 含 `&` 连接的两个 Action，取前尾后头）

  ### Step 4: 生成报告
  使用 ppt_report 工具的 `generate_report` 操作，一键替换所有图片并生成报告。
  工具内部按 Slide 顺序处理，维护每个文件夹的已消耗图片指针。

  ### Step 5: 汇报结果
  用中文告知用户报告已生成，说明输出路径、替换的图片总数、各映射类型的处理统计。

next_step_prompt: |
  根据用户需求，主动选择最合适的工具或工具组合。对于复杂任务，你可以分解问题并逐步使用不同工具来解决。使用每个工具后，清楚地解释执行结果并建议下一步。

  如果你需要生成测试报告，请使用 ppt_report 工具，按照 report_workflow 中定义的流程执行。

  如果你想在任何时候停止交互，请使用 `terminate` 工具/函数调用。
```

---

### Step 2: 修改 `app/prompt/manus.py`

**目标**：在 Manus 的 prompt 中加载 report.yaml，注入报告生成能力说明。

**修改方式**：

```python
import yaml
from pathlib import Path

# 加载 report prompt
_report_prompt_path = Path(__file__).parent / "report.yaml"
with open(_report_prompt_path, "r", encoding="utf-8") as f:
    _report_prompts = yaml.safe_load(f)

SYSTEM_PROMPT = (
    "你是 OpenManus，一个全能的 AI 助手..."
    "\n\n" + _report_prompts["system_instruction"]
)

NEXT_STEP_PROMPT = _report_prompts["next_step_prompt"]
```

---

### Step 3: 创建 `app/tool/ppt_report_tool.py`

**目标**：封装 python-pptx 操作，提供简洁的 Tool 接口给 Agent 调用。

**核心类**：`PPTReportTool(BaseTool)`

#### 3.1 Tool 参数定义

```python
name: str = "ppt_report"
description: str = (
    "PPT测试报告生成工具。可以分析模板PPT、自动匹配测试数据、"
    "替换Slide中的图片、生成最终报告。支持的操作："
    "find_project(根据项目名搜索数据目录和模板)、"
    "analyze_template(分析PPT结构)、"
    "build_mapping(建立Slide与数据的映射)、"
    "generate_report(一键生成完整报告)"
)

parameters = {
    "type": "object",
    "properties": {
        "action": {
            "type": "string",
            "enum": [
                "find_project",         # 根据项目名搜索USS Data目录
                "analyze_template",     # 分析模板PPT结构
                "build_mapping",        # 自动构建Slide→数据映射
                "generate_report",      # 一键生成完整报告
                "get_slide_info"        # 获取某个Slide的详细信息
            ],
            "description": "要执行的操作"
        },
        "project_name": {
            "type": "string",
            "description": "项目名称（用于 find_project 操作），如'Q6 etron USSDB R4.1 Test'"
        },
        "template_path": {
            "type": "string",
            "description": "模板PPT文件路径"
        },
        "data_dir": {
            "type": "string",
            "description": "测试数据根目录路径"
        },
        "output_path": {
            "type": "string",
            "description": "输出PPT文件路径（可选，默认保存到workspace/）"
        }
    },
    "required": ["action"]
}
```

#### 3.2 核心方法

##### `find_project(project_name: str) -> dict`
- 扫描 `USS Data/` 目录下的所有子文件夹（排除 .pptx 文件）
- 用 project_name 做模糊匹配（忽略大小写、空格差异）
- 模板固定使用 `USS Data/USSDB Test Report Template.pptx`
- 找到后返回：
  ```json
  {
    "found": true,
    "project_name": "Q6 etron USSDB R4.1 Test",
    "project_dir": "USS Data/Q6 etron USSDB R4.1 Test",
    "template_path": "USS Data/USSDB Test Report Template.pptx",
    "data_folders": ["TS_FCT_USS_4", "TS_FCT_USS_7", ...]
  }
  ```
- 如果找不到或找到多个匹配，返回提示信息

##### `analyze_template(template_path: str) -> dict`
- 使用 python-pptx 打开模板
- 遍历每个 Slide，提取：
  - Slide 编号、所有 TextBox 文本
  - 图片数量、每张图片的位置/尺寸/类型
- 返回结构化分析结果

##### `build_mapping(template_path: str, data_dir: str) -> dict`
- 调用 `analyze_template()` 获取 PPT 结构
- 扫描 data_dir 下的子文件夹
- 通过正则匹配 "Driver Activity: TS_FCT_USS_X" ↔ 子文件夹名
- **识别三种映射类型**（详见第六节）：
  - 类型 A（1:1）：一个 Slide 对应一个文件夹
  - 类型 B（N:1）：多个连续 Slide 共享一个文件夹，按顺序分配图片
  - 类型 C（跨文件夹）：Slide 含 `&` 连接符，取前一个文件夹的尾部 + 后一个文件夹的头部
- 返回映射结果（不写文件，直接返回给 Agent）

##### `generate_report(template_path, data_dir, output_path=None) -> str`
- 内部调用 `build_mapping()` 获取映射
- 用 python-pptx 打开模板
- **按 Slide 编号顺序执行替换**，维护每个数据文件夹的"已消耗指针"：
  - 类型 A：从文件夹取图，一一替换，不足时缺几张换几张
  - 类型 B：同一文件夹按 Slide 顺序连续消耗，记录已消耗 offset
  - 类型 C：从两个文件夹分别取尾部/头部图片，组合替换
- 保存到 output_path（默认 `workspace/{project_name}_Report.pptx`）
- 返回操作结果摘要，包含每种类型的处理统计

#### 3.3 图片替换策略（关键）

```
替换原则: 按 PPT 模板中图片的出现顺序（坐标排序），从数据文件夹中按序取图替换

对于 Slide 中的每张图片：
1. 记录原图片的位置 (left, top) 用于排序，以及 width, height 用于新图尺寸
2. 从分配到的图片列表中按序取一张
3. PNG 文件 → 替换 Slide 中的 PNG 图片；JPG 文件 → 替换 JPEG 图片
4. 使用 PIL 打开新图片，必要时进行格式转换
5. 在相同位置插入新图片，保持原尺寸（等比缩放居中裁剪）
6. 删除原图片 shape

数量不匹配处理:
  - PPT 图片数 >= 数据文件数: 有多少换多少，剩余 PPT 图片保留不动
  - PPT 图片数 < 数据文件数: 按序使用前 N 张，多余的跳过

共享文件夹的图片指针:
  - 对每个文件夹维护一个 consumed 计数器
  - 跨 Slide 连续使用时指针不重置（类型 B）
  - 类型 C 取尾部图片时不推进指针（是"借阅"尾部数据）
```

---

### Step 4: 修改 `app/agent/manus.py`

**目标**：将 PPTReportTool 加入 Manus 的工具集，让 `python main.py` 就能处理报告生成。

**修改内容**：

```python
from app.tool.ppt_report_tool import PPTReportTool   # 新增导入

class Manus(ToolCallAgent):
    available_tools: ToolCollection = Field(
        default_factory=lambda: ToolCollection(
            PythonExecute(),
            BrowserUseTool(),
            WebSearch(),
            StrReplaceEditor(),
            PPTReportTool(),    # ← 新增
            AskHuman(),
            Terminate(),
        )
    )
```

Prompt 也改为从 YAML 加载（如 Step 2 所述）。

---

### Step 5: 修改 `config/config.toml`

**目标**：添加 USS Data 路径和报告相关默认配置。

```toml
# USS Report 配置
[report]
# USS 测试数据根目录
data_root = "USS Data"
# 统一报告模板路径
template = "USS Data/USSDB Test Report Template.pptx"
# 报告输出目录
output_dir = "workspace"
```

**对应修改 `app/config.py`**：

新增 `ReportSettings` 配置类：

```python
class ReportSettings(BaseModel):
    data_root: str = Field("USS Data", description="USS测试数据根目录")
    template: str = Field("USS Data/USSDB Test Report Template.pptx", description="统一报告模板路径")
    output_dir: str = Field("workspace", description="报告输出目录")
```

在 `AppConfig` 中添加 `report_config` 字段，在 `_load_initial_config` 中加载。

---

### Step 6: 修改 `app/tool/__init__.py`

导出 `PPTReportTool`：

```python
from app.tool.ppt_report_tool import PPTReportTool
```

---

## 五、用户交互流程

```
用户: python main.py
  请输入你的提示: 帮我做 Q6 etron USSDB R4.1 Test 的测试报告

Agent 自动执行:
  ┌──────────────────────────────────────────┐
  │ Step 1: ppt_report.find_project          │
  │   输入: project_name="Q6 etron USSDB..."  │
  │   输出: 找到项目目录 + 模板 + 10个数据文件夹│
  │                                          │
  │ Step 2: ppt_report.analyze_template      │
  │   输入: template_path="..."               │
  │   输出: 18个Slide, 共98张图片             │
  │                                          │
  │ Step 3: ppt_report.build_mapping         │
  │   输入: template_path + data_dir          │
  │   输出: 映射结果                           │
  │     - 类型A (1:1): 6组匹配 (Slide 3-8)     │
  │     - 类型B (N:1): 2组 (Action1→Slide 9-11,│
  │                         Action3→Slide 15-16)│
  │     - 类型C (跨文件夹): 2组 (Slide 12, 14) │
  │     - 非测试页: 3页 (Slide 1, 2, 18)      │
  │                                          │
  │ Step 4: ppt_report.generate_report       │
  │   输入: template_path + data_dir          │
  │   输出: 正在替换Slide 3/18...生成成功      │
  │                                          │
  │ Step 5: terminate                        │
  │   返回: "报告已生成到 workspace/xxx.pptx"  │
  └──────────────────────────────────────────┘

输出: workspace/Q6 etron USSDB R4.1 Test_Report.pptx
```

---

## 六、映射匹配逻辑（核心算法）

### 6.1 整体流程

```
阶段 1: 扫描模板，提取每页的 Driver Activity 标识
阶段 2: 扫描数据目录，建立文件夹索引
阶段 3: 按映射类型分类处理（三种类型）
阶段 4: 按顺序逐 Slide 替换图片，生成报告
```

### 6.2 标识提取与标准化

对于 PPT 模板中的每个 Slide，用正则提取 Driver Activity 标识：

```
正则: r"Driver Activity:\s*TS_FCT_USS_\d+(?:\s*[-&]?\s*Action\s*-?\d+)*"

提取规则:
  "Driver Activity: TS_FCT_USS_4"               → ["TS_FCT_USS_4"]
  "Driver Activity: TS_FCT_USS_18  Action-1"    → ["TS_FCT_USS_18_Action1"]
  "Driver Activity: TS_FCT_USS_18  Action-1 & Action-2"
    → ["TS_FCT_USS_18_Action1", "TS_FCT_USS_18_Action2"]  (多个标识!)
  "Driver Activity: TS_FCT_USS_18  Action-2 & Action-3"
    → ["TS_FCT_USS_18_Action2", "TS_FCT_USS_18_Action3"]

标准化函数:
  - 移除多余空格
  - "Action-1" → "Action1"（去掉连字符）
  - " & " 作为分隔符，拆分为多个标识
```

### 6.3 三种映射类型

根据 Slide 提取到的标识数量和数据文件夹匹配情况，分为三种类型：

#### 类型 A：简单 1:1 映射 (Slide 3-8, 13, 17)

Slide 文本中只提取到**一个**标识，且该标识对应**独立**的数据文件夹。

```
处理方式:
  1. 收集 Slide 中所有图片 shape（按位置 left→top 排序）
  2. 从对应数据文件夹收集图片（按文件名排序）
  3. 按序替换，图片数不足时缺几张替换几张（多余模板图片保留不动）
  
  示例: Slide 3 (TS_FCT_USS_4): PPT=5张, 数据=4张 → 替换前4张, 第5张保留
```

#### 类型 B：N:1 连续共享映射 (Slide 9-11 共享 Action1, Slide 15-16 共享 Action3)

**多个连续 Slide** 共享**同一个**数据文件夹，图片按 Slide 顺序**连续分配**。

```
TS_FCT_USS_18_Action1 (20 张: 10 PNG + 10 JPG):
  Slide 9  (9 张)  → 取 01.PNG ~ 05.PNG + IMG_2951.JPG ~ IMG_2955.JPG (前9张)
  Slide 10 (9 张)  → 取 06.PNG ~ 09.PNG + IMG_2956.JPG ~ IMG_2960.JPG (中间9张)
  Slide 11 (9 张)  → 取 10.PNG + IMG_2951.JPG ~ IMG_2955.JPG (最后2张，回绕复用)

  Slide 9 → Slide 10 → Slide 11 连续消耗数据文件夹中的图片

TS_FCT_USS_18_Action3 (16 张: 8 PNG + 8 JPG):
  Slide 15 (9 张)  → 取前 9 张
  Slide 16 (9 张)  → 取后 7 张（不足9张则有多少替换多少）

处理方式:
  1. 识别出所有指向同一文件夹的连续 Slide
  2. 将该文件夹的所有图片按文件名排序
  3. 按母版中每页的实际图片数，顺序分配
  4. 每页先分配 PNG，再分配 JPG（与母版中图片出现顺序一致）
```

**关键算法**：如何判断多个 Slide 共享同一数据文件夹？

```
对按 Slide 编号排序后的映射列表:
  如果连续两个 Slide 都指向同一文件夹 → 它们是 N:1 共享组
  
  示例:
    Slide 9  → TS_FCT_USS_18_Action1  ┐
    Slide 10 → TS_FCT_USS_18_Action1  ├─ 共享组: 连续3页
    Slide 11 → TS_FCT_USS_18_Action1  ┘
```

#### 类型 C：跨文件夹组合映射 (Slide 12, 14)

Slide 文本中提取到**两个**标识（用 `&` 连接），表示此页展示两个 Action 的**衔接数据**。

```
Slide 12: ["TS_FCT_USS_18_Action1", "TS_FCT_USS_18_Action2"]
  → Action1 的最后 N 张 + Action2 的前 M 张（N + M = 9，即为模板该页的图片数）
  → 分配规则: 从 Action1 的尾部取图 + 从 Action2 的头部取图

Slide 14: ["TS_FCT_USS_18_Action2", "TS_FCT_USS_18_Action3"]
  → Action2 的最后 N 张 + Action3 的前 M 张（N + M = 9）
  → 同上规则
```

**分配策略**：

```
1. 获取两个数据文件夹的图片列表（均已排序）
2. 获取此 Slide 在模板中的图片总数 Total
3. 计算分界点（默认按前后文件夹图片数量比例分配）:
   - count_A = floor(文件夹A图片数 / (文件夹A图片数 + 文件夹B图片数) × Total)
   - count_B = Total - count_A
4. 从文件夹 A 取最后 count_A 张，从文件夹 B 取前 count_B 张
5. 按序替换 Slide 中的图片

注意: 由于类型 B 已经消耗了一部分图片，组合页取图时应基于"已消耗后"的指针位置。
```

### 6.4 图片替换的执行顺序

```
图片替换必须按 PPT 中图片的原始出现顺序进行（即 shape 的 left→top 坐标排序）:

1. 对所有 Slide 按编号排序，建立映射关系
2. 识别共享组（类型 B）和组合组（类型 C）
3. 为每个数据文件夹计算"已消耗指针"（跨 Slide 共享状态）
4. 按 Slide 编号顺序逐一执行替换:
   - 获取该 Slide 的图片列表（按坐标排序）
   - 根据映射类型获取对应的源图片列表
   - 一一替换: 保持原位置/尺寸, 替换图片内容
5. 保存生成的 PPT

共享状态管理:
  class FolderImageCursor:
      folder_path: str
      all_images: list[str]  (已排序的完整图片列表)
      consumed: int = 0      (已消耗数量)
      
      def take(self, count: int) -> list[str]:
          '''取 count 张图片，返回路径列表，并推进指针'''
          
      def take_last(self, count: int) -> list[str]:
          '''从末尾取 count 张图片'''
```

### 6.5 非测试数据页处理

| Slide | 类型 | 处理方式 |
|-------|------|---------|
| 1 (封面) | 标题 + 作者 | 从 `find_project` 返回的 project_name 自动填充标题；作者信息从配置读取 |
| 2 (车辆配置) | 表格 | 保留模板原样，必要时手动编辑 |
| 18 (参数概览) | 图片 + 表格 | 如有对应图片则替换，表格保留原样 |

---

## 七、文件清单

| 文件 | 操作 | 说明 |
|------|------|------|
| `app/prompt/report.yaml` | **新建** | Report 相关 prompt (YAML格式) |
| `app/tool/ppt_report_tool.py` | **新建** | PPT 操作工具 |
| `app/prompt/manus.py` | **修改** | 从 report.yaml 加载报告相关 prompt |
| `app/agent/manus.py` | **修改** | 添加 PPTReportTool 到工具集 |
| `app/tool/__init__.py` | **修改** | 导出 PPTReportTool |
| `app/config.py` | **修改** | 添加 ReportSettings 配置类 |
| `config/config.toml` | **修改** | 添加 [report] 配置段 |
| `requirements.txt` | **修改** | 添加 python-pptx 依赖 |

> **不再需要** `generate_report.py`、`app/agent/report_agent.py`——用户统一通过 `python main.py` 使用。

---

## 八、开发顺序建议

| 优先级 | 任务 | 说明 |
|--------|------|------|
| P0 | `app/tool/ppt_report_tool.py` | 核心工具，包含 5 个操作 + 三种映射类型 + `FolderImageCursor` 共享状态管理 |
| P0 | `app/prompt/report.yaml` | 所有报告相关 prompt |
| P1 | `app/prompt/manus.py` 修改 | 加载 YAML prompt |
| P1 | `app/agent/manus.py` 修改 | 添加 PPTReportTool |
| P1 | `app/tool/__init__.py` 修改 | 导出新工具 |
| P2 | `app/config.py` 修改 | 添加 ReportSettings |
| P2 | `config/config.toml` 修改 | 添加 [report] 配置段 |

> 建议先在 `ppt_report_tool.py` 中完成**类型 A**（最简单的 1:1 映射）并用 Slide 3-8 验证，再实现**类型 B**（N:1 共享），最后实现**类型 C**（跨文件夹组合）。循序渐进可降低调试复杂度。

---

## 九、测试验证

```bash
# 1. 激活环境
conda activate open_manus

# 2. 安装新依赖
pip install python-pptx

# 3. 启动 Manus
python main.py

# 4. 输入需求
请输入你的提示: 帮我做 Q6 etron USSDB R4.1 Test 的测试报告
```

验证内容：
1. Agent 正确找到 USS Data 下的项目文件夹和模板（共 10 个数据文件夹）
2. 模板分析正确（18 页，16 页含 Driver Activity 标识）
3. Slide → 数据映射正确：
   - 类型 A（1:1）：Slide 3-8, 13, 17 映射正确，数量不足时正确处理
   - 类型 B（N:1）：Slide 9-11（共享 Action1）和 Slide 15-16（共享 Action3）按顺序分配图片
   - 类型 C（跨文件夹）：Slide 12（Action1+Action2）和 Slide 14（Action2+Action3）正确合并
4. 图片替换后位置、尺寸与原始模板一致
5. 非测试页（Slide 1, 2, 18）保留模板原样
6. 报告正确输出到 workspace 目录
7. 返回的摘要包含每种类型的处理统计
