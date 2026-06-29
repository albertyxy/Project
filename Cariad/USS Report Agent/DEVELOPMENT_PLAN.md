# USS Report Agent 开发计划

## 一、项目概述

基于 OpenManus-cy 框架，开发**PPT 报告自动生成功能**。用户通过 `python main.py` 启动后，直接说"帮我做 XXX 的测试报告"，Agent 自动找到对应数据并基于统一模板生成报告。

### 目录结构

```
USS Data/
├── USSDB Test Report Template.pptx              ← 统一模板（所有报告共用，~50MB）
├── E6L USSDB R4.1 Test/                         ← 测试项目数据（示例）
│   ├── HAUN3BGG0S5200119_*.xml                   ← iDEX 诊断报告（Slide 1/2 元数据来源）
│   ├── HAUN3BGG0S5200119_*.html                  ← 诊断报告 HTML 版
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
│   ├── TS_FCT_USS_18_Action1/                    ← 与 Slide 9-11 对应（3页共享）
│   │   ├── Action1_01.PNG ~ Action1_10.PNG (图表)
│   │   └── IMG_2915.JPG ~ IMG_2924.JPG (照片)
│   ├── TS_FCT_USS_18_Action2/                    ← 与 Slide 12-14 关联
│   │   ├── Action2_01.PNG ~ Action2_06.PNG (图表)
│   │   └── IMG_2925.JPG ~ IMG_2930.JPG (照片)
│   ├── TS_FCT_USS_18_Action3/                    ← 与 Slide 14-16 关联（2页共享）
│   │   ├── Action3_01.PNG ~ Action3_08.PNG (图表)
│   │   └── IMG_2931.JPG ~ IMG_2938.JPG (照片)
│   └── TS_FCT_USS_18_Action4/                    ← 与 Slide 17 对应
│       ├── Action4_01.PNG ~ Action4_02.PNG (图表)
│       └── IMG_2939.JPG ~ IMG_2940.JPG (照片)
```

> **关于 .mf4 文件**：原始测量数据文件（ASAM MDF 格式），报告生成不使用。
>
> **关于 .xml 文件**：iDEX 诊断报告，用于自动填充 Slide 1 标题和 Slide 2 表格（Vehicle/VIN/HCP1/EPS）。
>
> **关于 .html 文件**：诊断报告 HTML 版本，程序不使用。

### 核心场景

```
用户: "帮我做 E6L USSDB R4.1 Test 的测试报告"

Agent 自动:
  1. find_project 扫描 USS Data/ 定位项目文件夹
  2. 解析 .xml 提取 Vehicle/VIN/HCP1/EPS → 填充 Slide 1/2
  3. 分析模板 Slide 结构，匹配数据子文件夹中的图片
  4. 按列模式替换 Slide 图片，生成报告到 workspace/
  
输出: workspace/E6L USSDB R4.1 Test_Report.pptx (~60MB)
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

### 关键发现（详见第六节核心算法）

1. TestBox 中 `Driver Activity: TS_FCT_USS_X` 标识 → 正则提取 → 匹配数据文件夹
2. TS_FCT_USS_18 Slide（9-17）：三列布局（Example / Test / Test Result），按列替换
3. 非 TS_FCT_USS_18 Slide（3-8）：简单 1:1 全部替换
4. Slide 1/2：从 XML 填充标题和表格数据（详见 6.6 节）

---

## 三、架构设计

### 3.1 整体架构

```
USS Report Agent/
├── app/
│   ├── agent/
│   │   └── manus.py              ← [修改] 添加 PPTReportTool 到工具集
│   ├── tool/
│   │   └── ppt_report_tool.py    ← [新建] PPT 报告工具（通用，配置驱动）
│   ├── prompt/
│   │   └── report.yaml           ← [新建] Report 相关 prompt (YAML格式)
│   └── config.py                 ← [修改] 添加 USS Data 路径配置
├── config/
│   └── config.toml               ← [修改] 添加 report 配置段
├── USS Data/
│   ├── template_config.json      ← [新建] 模板配置文件（换模板只改此文件）
│   └── USSDB Test Report Template.pptx
└── DEVELOPMENT_PLAN.md            ← [本文件]
```

### 3.2 设计原则

- **不新建独立 Agent**：复用 Manus Agent，将 PPTReportTool 加入其工具集即可
- **不新建入口脚本**：用户统一通过 `python main.py` 交互
- **Prompt 用 YAML**：所有提示词写在 `app/prompt/report.yaml` 中，与其他 prompt 风格统一
- **配置驱动**：模板结构、字段映射、列布局等通过 `template_config.json` 描述，换模板不改代码
- **自动发现**：Agent 根据用户描述的项目名，自动在 `USS Data/` 下搜索匹配的目录

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
  1. 根据用户提到的项目名称，使用 ppt_report 工具在 USS Data 目录下定位项目
  2. 模板固定为 USS Data 目录下的 USSDB Test Report Template.pptx，find_project 会自动返回
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
- 分析模板 + 扫描数据目录 → 建立 Slide↔文件夹映射
- 自动识别三种映射类型（详见第六节 6.3）

##### `generate_report(template_path, data_dir, output_path=None) -> str`
- 一键完成：XML 元数据填充 → 列模式预分配 → 按 Slide 顺序替换图片 → 保存
- 内部自动处理所有映射类型和列分类（详见第六节 6.4、6.5）

#### 3.3 图片替换策略

详见第六节核心算法。要点：
- **简单模式**（Slide 3-8）：1:1 替换全部图片
- **列模式**（Slide 9-17）：left 坐标聚类识别三列，Example 保留、Test→JPG、Test Result→PNG
- **格式兼容**：MPO（iPhone 照片）转 JPEG(q=85)，限制 1920px，输出 ~60MB

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
  请输入你的提示: 帮我做 E6L USSDB R4.1 Test 的测试报告

Agent 自动执行:
  ┌──────────────────────────────────────────┐
  │ Step 1: ppt_report.find_project          │
  │   输入: project_name="E6L USSDB..."       │
  │   输出: 找到项目目录 + 模板路径             │
  │                                          │
  │ Step 2: ppt_report.generate_report       │
  │   内部自动完成:                            │
  │   - 解析 XML → 填充 Slide 1/2 元数据      │
  │   - analyze_template → 18页, 98张图片     │
  │   - build_mapping → 简单模式6页 + 列模式9页│
  │     · 类型B (N:1): 2组 (Action1/3)        │
  │     · 类型C (跨文件夹): 2组 (Slide 12,14)  │
  │   - 图片替换: 简单模式19张 + 列模式52张    │
  │     (Test列26 JPG + Test Result列26 PNG)  │
  │     Example列模板图片全部保留              │
  │   输出: ~60MB                             │
  │                                          │
  │ Step 3: terminate                        │
  │   返回: "报告已生成到 workspace/xxx.pptx"  │
  └──────────────────────────────────────────┘

输出: workspace/E6L USSDB R4.1 Test_Report.pptx
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
TS_FCT_USS_18_Action1 (10 JPG + 10 PNG):
  JPG 通道 (Test 列): Slide 9→IMG[0:3], Slide 10→IMG[3:6], Slide 11→IMG[6:9]
  PNG 通道 (Test Result 列): Slide 9→PNG[0:3], Slide 10→PNG[3:6], Slide 11→PNG[6:9]
  每页各 3 张 JPG + 3 张 PNG = 6 张替换 (Example 列 3 张保留)

TS_FCT_USS_18_Action3 (8 JPG + 8 PNG):
  JPG: Slide 15→IMG[0:3], Slide 16→IMG[3:6] (Slide 14 先用掉 2 张头部)
  PNG: Slide 15→PNG[0:3], Slide 16→PNG[3:6]

处理方式:
  1. 识别出所有指向同一文件夹的连续 Slide
  2. JPG 和 PNG 各自独立排序，各自维护消耗指针
  3. 按 Slide 顺序，每页取 test_count 张 JPG + test_result_count 张 PNG
  4. 所有列模式 Slide 严格按编号顺序分配（Type C 在 Type B 前消耗）
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

### 6.4 列分类算法

TS_FCT_USS_18 系列 Slide 需要通过 left 坐标聚类来识别三列：

```
算法: 列聚类 (COLUMN_TOLERANCE_EMU = 150000, ~0.16 inch)

1. 收集 Slide 中所有图片 shape
2. 按 left 坐标升序排序
3. 相邻 left 值差值 <= 容差 → 归入同一列
4. 差值 > 容差 → 新开一列
5. 按各列的 left 均值升序排列
6. 映射: 最左 → Example, 中间 → Test, 最右 → Test Result

示例 (Slide 9):
  图片 left: [1.2, 1.2, 1.2, 3.7, 3.7, 3.7, 6.3, 6.4, 6.4] (inch)
  聚类结果: [[0,1,2]=Example, [3,4,5]=Test, [6,7,8]=Test Result]
```

### 6.5 图片替换的执行顺序

```
整体流程:
1. 对所有 Slide 按编号排序，建立映射关系
2. 识别 TS_FCT_USS_18 系列 → column_mode = True
3. 识别共享组（类型 B）和组合组（类型 C）
4. 为每个数据文件夹创建 FolderImageCursor（JPG/PNG 独立指针）

简单模式 (非 TS_FCT_USS_18):
  收集 Slide 所有图片 → 从文件夹按序取图 → 1:1 替换

列模式 (TS_FCT_USS_18):
  1. 用列聚类算法分类每张图片为 Example / Test / Test Result
  2. Example 列 → 跳过（保留模板图片不动）
  3. Test 列 → 从 JPG 通道按序取图替换
  4. Test Result 列 → 从 PNG 通道按序取图替换
  5. 类型 B 共享组：JPG/PNG 指针跨 Slide 连续消耗
  6. 类型 C 组合页：取前一文件夹尾部 + 后一文件夹头部

共享状态管理:
  class FolderImageCursor:
      folder_path: str
      jpg_images: list[str]    # JPG 文件（已排序）
      png_images: list[str]    # PNG 文件（已排序）
      jpg_consumed: int = 0    # JPG 已消耗数量
      png_consumed: int = 0    # PNG 已消耗数量
      
      def take_jpg(count) -> list[str]   # 从头部取 JPG
      def take_png(count) -> list[str]   # 从头部取 PNG
      def take_last_jpg(count) -> list[str]  # 从尾部取 JPG（类型 C）
      def take_last_png(count) -> list[str]  # 从尾部取 PNG（类型 C）
```

### 6.6 Slide 1/2 元数据填充（XML）

数据来源：项目目录下的 iDEX XML（`{VIN}_*.xml`），使用 `xml.etree.ElementTree` 解析。

**Slide 1 标题**：`UserProjekt`（如 `AU511/x E6 Limo China`）→ 正则提取车型 → `E6L USSDB R4.1 Test Report`

**Slide 2 表格**：

| 行 | ECU 匹配 | 各列 XML 来源 |
|----|---------|-------------|
| Row 1 | -- | Vehicle: `UserProjekt`, VIN: `Fahrgestellnummer` |
| Row 3 (HCP1) | `Systembezeichnung` 含 `HCP1` | `SWTeilenummer`, `SWVersion`, `ZdcName [ZdcVersion]`, `HWTeilenummer`, `HWVersion` |
| Row 4 (EPS) | `Systembezeichnung` 含 `EPS` | 同上 |

> 通过修改 `run.text` 保持原有字体样式；无 XML 时降级跳过。`_generate_report` 自动调用。

---

## 七、文件清单

| 文件 | 操作 | 说明 |
|------|------|------|
| `app/prompt/report.yaml` | **新建** | Report 相关 prompt (YAML格式) |
| `app/tool/ppt_report_tool.py` | **新建** | PPT 操作工具（通用逻辑，配置驱动） |
| `USS Data/template_config.json` | **新建** | 模板配置文件（换模板只改此文件） |
| `app/prompt/manus.py` | **修改** | 从 report.yaml 加载报告相关 prompt |
| `app/agent/manus.py` | **修改** | 添加 PPTReportTool 到工具集 |
| `app/tool/__init__.py` | **修改** | 导出 PPTReportTool |
| `app/config.py` | **修改** | 添加 ReportSettings 配置类 |
| `config/config.toml` | **修改** | 添加 [report] 配置段 |
| `requirements.txt` | **修改** | 添加 python-pptx 依赖 |

> XML 解析使用 Python 标准库 `xml.etree.ElementTree`，无需额外依赖。
>
> **不再需要** `generate_report.py`、`app/agent/report_agent.py`——用户统一通过 `python main.py` 使用。

---

## 八、开发顺序建议

| 优先级 | 任务 | 说明 |
|--------|------|------|
| P0 | `app/tool/ppt_report_tool.py` | 核心工具，包含 5 个 actions + 列聚类 + JPG/PNG 独立指针 + XML 元数据填充 |
| P0 | `app/prompt/report.yaml` | 所有报告相关 prompt |
| P1 | `app/prompt/manus.py` 修改 | 加载 YAML prompt |
| P1 | `app/agent/manus.py` 修改 | 添加 PPTReportTool |
| P1 | `app/tool/__init__.py` 修改 | 导出新工具 |
| P2 | `app/config.py` 修改 | 添加 ReportSettings |
| P2 | `config/config.toml` 修改 | 添加 [report] 配置段 |

> 所有路径基于 `PROJECT_ROOT`（由 `config.py` 从 `__file__` 计算），不依赖 cwd，任何人 clone 后直接可用。

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
请输入你的提示: 帮我做 E6L USSDB R4.1 Test 的测试报告
```

验证内容：
1. Agent 正确找到 USS Data 下的项目文件夹，模板路径指向 USS Data 根目录
2. XML 解析正确提取 Vehicle/VIN/HCP1/EPS 数据
3. Slide 1 标题替换为正确的车型名（保持原有字体样式）
4. Slide 2 表格数据从 XML 正确填充（保持原有字体样式）
5. 模板分析正确（18 页，15 页含 Driver Activity 标识）
6. Slide → 数据映射正确（类型 A/B/C）
7. TS_FCT_USS_18 列模式：Example 保留、Test→JPG、Test Result→PNG
8. 图片分配顺序正确（Type C Slide 14 在 Type B Slide 15-16 前消耗）
9. 生成文件约 60MB（接近模板 50MB，优化 MPO→JPEG + 1920px 限制）
10. 报告正确输出到 workspace 目录
