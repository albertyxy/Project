# USS Report Agent 开发计划

## 一、项目概述

基于 OpenManus-cy 框架，开发**PPT 报告自动生成功能**。用户通过 `python main.py` 启动后，直接说"帮我做 XXX 的测试报告"，Agent 自动找到对应数据并基于统一模板生成报告。

### 目录结构

```
USS Data/
├── USSDB Test Report Template.pptx              ← 统一模板（所有报告共用）
├── Q6 etron USSDB R4.1 Test/                    ← 某个测试项目的数据
│   ├── TS_FCT_USS_4/                             ← 与 Slide 3 对应
│   ├── TS_FCT_USS_7/                             ← 与 Slide 4 对应
│   ├── TS_FCT_USS_18_Action1/                    ← 与 Slide 9 对应
│   └── ...
└── NewTest Project/                              ← 另一个测试项目的数据
    └── ...
```

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

经过对模板 PPT 的结构化分析（18 页），总结如下：

| Slide | 类型 | 内容 |
|-------|------|------|
| 1 | 封面 | 标题 + 作者，无图片 |
| 2 | 车辆配置 | 仅有 Table，无图片 |
| 3-17 | **测试结果页** | TextBox（含 "Driver Activity: TS_FCT_USS_X"）+ Table + 多张图片 |
| 18 | 参数概览 | TextBox + Table + 1 张图片 |

### 关键发现

1. **每张测试结果页的 TextBox 中包含测试用例标识**，如：
   - `Driver Activity: TS_FCT_USS_4`
   - `Driver Activity: TS_FCT_USS_18  Action-1`

2. **图片分为两种类型**：
   - PNG 图片：图表/曲线图
   - JPEG 图片：现场照片（来自 IMG_XXXX.JPG）

3. **数据目录结构与测试用例一一对应**：
   ```
   USS Data/
   ├── USSDB Test Report Template.pptx            ← 统一模板（所有报告用这个）
   ├── Q6 etron USSDB R4.1 Test/                   ← 项目数据目录
   │   ├── TS_FCT_USS_4/                           ← 与 Slide 3 对应
   │   │   ├── 01.PNG, 02.PNG, 03.PNG, 04.PNG
   │   ├── TS_FCT_USS_7/                           ← 与 Slide 4 对应
   │   ├── TS_FCT_USS_18_Action1/                  ← 与 Slide 9-12 对应
   │   │   ├── 01.PNG ~ 10.PNG  (图表)
   │   │   └── IMG_2951.JPG ~ IMG_2960.JPG  (照片)
   │   └── ...
   └── NewTest Project/                            ← 其他测试项目
       └── ...
   ```

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
  与数据子文件夹名称，建立映射关系。

  ### Step 4: 生成报告
  使用 ppt_report 工具的 `generate_report` 操作，一键替换所有图片并生成报告。

  ### Step 5: 汇报结果
  用中文告知用户报告已生成，说明输出路径和替换的图片总数。

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
- 返回映射结果（不写文件，直接返回给 Agent）

##### `generate_report(template_path, data_dir, output_path=None) -> str`
- 内部调用 `build_mapping()` 获取映射
- 用 python-pptx 打开模板
- 遍历映射中的每对 (slide, data_folder)：
  - 收集 Slide 中所有图片 shape
  - 从 data_folder 按文件名排序读取新图片
  - 保持原位置/尺寸，替换图片内容
- 保存到 output_path（默认 `workspace/{project_name}_Report.pptx`）
- 返回操作结果摘要

#### 3.3 图片替换策略（关键）

```
对于 Slide 中的每张图片：
1. 记录原图片的位置 (left, top, width, height)
2. 从对应的 data 子文件夹中按文件名排序取图片
3. PNG 文件 → 替换 Slide 中的 PNG 图片
4. JPG 文件 → 替换 Slide 中的 JPEG 图片
5. 使用 PIL 打开新图片，必要时进行格式转换
6. 在相同位置插入新图片，保持原尺寸
7. 删除原图片 shape
8. 数量不匹配时按顺序对应，多余的跳过
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
  │   输出: 找到项目目录和模板文件              │
  │                                          │
  │ Step 2: ppt_report.analyze_template      │
  │   输入: template_path="..."               │
  │   输出: 18个Slide, 共X张图片              │
  │                                          │
  │ Step 3: ppt_report.build_mapping         │
  │   输入: template_path + data_dir          │
  │   输出: 10个测试用例映射成功               │
  │                                          │
  │ Step 4: ppt_report.generate_report       │
  │   输入: template_path + data_dir          │
  │   输出: 正在替换Slide 3/18...             │
  │                                          │
  │ Step 5: terminate                        │
  │   返回: "报告已生成到 workspace/xxx.pptx"  │
  └──────────────────────────────────────────┘

输出: workspace/Q6 etron USSDB R4.1 Test_Report.pptx
```

---

## 六、映射匹配逻辑（核心算法）

```
对于 PPT 模板中的每个 Slide:
  1. 遍历该 Slide 的所有 TextBox
  2. 用正则提取 TS_FCT_USS 测试用例标识
     - 正则: r"TS_FCT_USS_\d+(?:\s*[-&]?\s*Action\s*-?\d+)*"
     - "Driver Activity: TS_FCT_USS_4"               → "TS_FCT_USS_4"
     - "Driver Activity: TS_FCT_USS_18  Action-1"    → "TS_FCT_USS_18_Action1"
     - "Driver Activity: TS_FCT_USS_18  Action-2 & Action-3"
       → 多个匹配时取第一个 "TS_FCT_USS_18_Action2"

  3. 在 data_dir 下查找匹配的子文件夹:
     - 标准化名称后精确匹配
     - 如果找不到精确匹配，尝试模糊匹配

  4. 匹配成功后:
     - 收集 Slide 中所有图片 (按 left, top 坐标排序)
     - 收集 data 子文件夹中所有图片文件 (按文件名排序)
     - PNG 对 PNG, JPG 对 JPG 分组替换
```

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
| P0 | `app/tool/ppt_report_tool.py` | 核心工具，包含 find_project/analyze/build_mapping/generate_report |
| P0 | `app/prompt/report.yaml` | 所有报告相关 prompt |
| P1 | `app/prompt/manus.py` 修改 | 加载 YAML prompt |
| P1 | `app/agent/manus.py` 修改 | 添加 PPTReportTool |
| P1 | `app/tool/__init__.py` 修改 | 导出新工具 |
| P2 | `app/config.py` 修改 | 添加 ReportSettings |
| P2 | `config/config.toml` 修改 | 添加 [report] 配置段 |

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
1. Agent 正确找到 USS Data 下的项目文件夹和模板
2. 模板分析正确（18 页，每页测试用例标识识别正确）
3. Slide→数据映射正确
4. 图片替换后位置、尺寸与原始模板一致
5. 报告正确输出到 workspace 目录
