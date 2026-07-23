# TraceLens PPT 报告生成功能 - 开发计划

## 1. PPT 模板结构（已分析）

**文件**: `data/Template/Test Template.pptx` | 20 页 | 13.3×7.5 英寸

### Slide 1 - ECU 配置页
```
标题: "WBA functions related ECU status"
副标题: "Test vehicle actual configuration"
表格 (8行×6列):
  r0: Configuration of relevant ECU
  r1: Vehicle: A5L TF156, VIN: LFV3A2FUXR389  ← 从 XML 填充
  r2: Main-SG | Software-TNR. | Software-Version | ZDC/DS-version | Hardware-TNR. | Hardware-Version
  r3: LRR   | 85E907567AM   | Y653             | 4B3909885CF    | 85E907567A    | H02
  r4: MFK   | 85E907217AE   | X930             | 8B3000466CA    | 85E907217A    | H19
  r5: HCP1  | 0Z7907479CQ   | 1662             | 8BG909586AC    | 0Z7907479K    | H30
  r6: NR    | 95C907541AN   | X756             | 8BG909410BB    | 95C907541     | H07
  r7: ESC   | 8BG909059F    | X555             | 8BG000504K     | 8BG909059B    | X06
```

### Slide 2-20 - 场景分析页（20 页）

**每页统一布局:**
| 位置 | Shape | 尺寸 | 内容 |
|------|-------|------|------|
| 顶部标题栏 | Rectangle 3 | 13.3×0.7in | "05 Trace Analysis" |
| 左侧文本区 | Text Box | 5.7×5.3in | Scenario名 + Trace文件名(3 run) |
| 左侧顶部小图 | Picture 6 | 1.0×1.6in | 对应 1.PNG |
| 左侧顶部大图 | Picture 16/18/7 | 2.2-3.0×1.1-1.5in | 对应 2.PNG |
| 左侧底部三小图 | Picture 26/23/19 | 1.9×1.1in | 对应 3-5.PNG |
| 右侧 Run 标签 | 矩形 22 (×3) | 0.3×1.5in | "Run1"/"Run2"/"Run3" |
| 右侧 Run 大图 | Picture 30/34/8 | 5.3×1.5in | 对应 6-8.PNG |
| 右侧表格 (仅CPLA) | Table 65 | 7.6×1.0in, 4r×5c | TTC 信号数据 |

**场景→幻灯片映射:**
| Slide | 场景文件夹 | 有表格 | 有文本 |
|-------|-----------|--------|--------|
| 2 | CPLA-25_Night_20kph | ✓ | ✓ |
| 3 | CPLA-25_Night_40kph | ✓ | ✓ |
| 4 | CPLA-25_Night_60kph | ✓ | ✓ |
| 5 | CPLA-25_Night_80kph | ✓ | ✓ |
| 6 | CPNCO-25_20kph | - | ✓ |
| 7 | CPNCO-25_40kph | - | ✗ |
| 8 | CBNAO-50_20kph | - | ✓ |
| 9 | CBNAO-50_40kph | - | ✓ |
| 10 | CBNAO-50_60kph | - | ✗ |
| 11 | CPTA-LN-50_10kph | - | ✓ |
| 12 | CPTA-LN-50_20kph | - | ✓ |
| 13 | CPTA-LN-50_30kph | - | ✓ |
| 14 | CPTA-LF-50_10kph | - | ✓ |
| 15 | CPTA-LF-50_20kph | - | ✓ |
| 16 | CPTA-LF-50_30kph | - | ✓ |
| 17 | C2C SCP_30kph | - | ✓ |
| 18 | C2C SCP_40kph | - | ✓ |
| 19 | C2C SCP_50kph | - | ✓ |
| 20 | C2C SCP_60kph | - | ✓ |

**图片→PNG 映射（每场景 8 张图）:**
| PNG | PPT Shape | 位置 |
|-----|-----------|------|
| 1.PNG | Picture 6 (1.0×1.6) | 左列第1 |
| 2.PNG | Picture 16/18/7 (变) | 左列第2 |
| 3.PNG | Picture 26 (1.9×1.1) | 左下列1 |
| 4.PNG | Picture 23 (1.9×1.1) | 左下列2 |
| 5.PNG | Picture 19 (1.9×1.1) | 左下列3 |
| 6.PNG | Picture 30 (5.3×1.5) | Run1 大图 |
| 7.PNG | Picture 34 (5.3×1.5) | Run2 大图 |
| 8.PNG | Picture 8 (5.3×1.5) | Run3 大图 |

### CPLA 表格结构（只有 Slide 2-5 有）
```
4行 × 5列:
r0: Case | Result | Radar Confirm TTC (s) | Confirm as pedestrian TTC (s) | Brake/VW Activated TTC (s)
r1: Run1 | Pass   | [MF4提取值]            | [MF4提取值]                   | [MF4提取值]
r2: Run2 | Pass   | [MF4提取值]            | [MF4提取值]                   | [MF4提取值]
r3: Run3 | Pass   | [MF4提取值]            | [MF4提取值]                   | [MF4提取值]
```
注：Slide 2-3 列4标题为 "Brake Activated TTC"，Slide 4-5 为 "VW Activated TTC"

## 2. Trace Record 数据结构

**文件**: `data/A5L 99C WBA LRR Y653/Trace Record.xlsx` | Sheet: "A5L" | 67 行 × 12 列

**关键列:**
| 列 | 名称 | 说明 |
|----|------|------|
| A | Scenario | 测试场景名（如 CPNCO-25, CPTA-LN-50, CPLA-25 Night）|
| B | Function | AEB / FCW |
| C | VVUT | 测试速度 (km/h) |
| E | Overlap | 重叠率 |
| F | Runs | run1/run2/run3 |
| G | Pass/No | Pass / Collision / (空=未测试) |
| H | CANape Trace | MF4 文件名 |
| J | FCW_TTC (s) | TTC 值 |
| K | Vimpact (km/h) | 碰撞速度 |

**场景→文件夹名称映射:**
```
文件夹名 = Scenario + "_" + VVUT + "kph"
例如: CPLA-25 Night + "_" + 20 + "kph" → CPLA-25_Night_20kph
```

## 3. Trace 匹配流程

**核心逻辑：数据文件夹是地面真相**

```
1. 读取 data/{项目名}/ 下所有场景文件夹
2. 对每个场景文件夹：
   a. 根据文件夹名匹配 PPT 中对应 Slide（通过文本框 Scenario 名）
   b. 去 Trace Record.xlsx 找 Scenario 列匹配 + VVUT 匹配的行
   c. 读取 Run1/2/3 的 CANape Trace 名、Pass/Fail 状态
   d. 在 data/{项目名}/ 下查找对应的 MF4 文件
   e. 如果 MF4 存在 → 提取信号数据填表
   f. 如果 MF4 不存在 → 表格保留模板占位或填"/"
3. 没有对应数据文件夹的 Slide → 保留模板不动
```

**当前状态**: 只有 1 个 MF4（Gen5_2026-06-30_20-39_Y653_RC1__0067），可填 CPLA-25_Night_20kph 的 Run1

## 4. XML → Slide 1 ECU 配置映射

**XML 文件**: `data/{项目名}/*.xml`

**关键 XML 字段:**
| XML 字段 | PPT 用途 |
|----------|---------|
| `Fahrgestellnummer` | Slide 1 VIN |
| `UserProjekt` | Slide 1 车型名 |
| `WegStrecke` + `EinheitWegStrecke` | Slide 1 里程 |

**ECU 映射（XML Systembezeichnung → PPT 表行）:**
| PPT 行 | PPT 名称 | XML Systembezeichnung 匹配 |
|--------|---------|--------------------------|
| r3 | LRR | "008B - Distance regulation 2" |
| r4 | MFK | "00A5 - Front sensor for driver assistance systems" |
| r5 | HCP1 | "HCP1 BOSCH EP" |
| r6 | NR | "Nanoradar 1" |
| r7 | ESC | "ABS" |

## 5. 表格信号映射（YAML 配置）

信号→表格列的映射写在 `pptx_agent/table_mapping.yaml`。

### 映射配置

每个信号使用完整路径，不区分端口/前缀。

```yaml
# pptx_agent/table_mapping.yaml

columns:
  - col_index: 2
    header: "Radar Confirm TTC (s)"
    description: "雷达+摄像头均确认目标为行人时的TTC"
    extract:
      method: cross_reference
      target: "_g_Common_VAG_..._m_values._0_._m_objectData._m_ttc._m_value"
      triggers:
        - signal: "_g_Common_VAG_..._m_values._0_._m_objectData._m_camConfirmation"
          condition: equals
          value: 1
        - signal: "_g_Common_VAG_..._m_values._0_._m_objectData._m_radarConfirmation"
          condition: equals
          value: 1
        - signal: "_g_Common_VAG_..._m_values._0_._m_objectData._m_targetObjType"
          condition: equals
          value: "pedestrian"
    format: ".2f"

  - col_index: 3
    header: "Confirm as pedestrian TTC (s)"
    description: "确认为行人时的TTC"
    extract:
      method: cross_reference
      target: "_g_Common_VAG_..._m_values._0_._m_objectData._m_ttc._m_value"
      triggers:
        - signal: "_g_Common_VAG_..._m_values._0_._m_objectData._m_targetObjType"
          condition: equals
          value: "pedestrian"
    format: ".2f"

  - col_index: 4
    header: "Brake Activated TTC (s)"
    description: "制动激活(dAB=4)时的TTC"
    extract:
      method: cross_reference
      target: "_g_Common_VAG_..._m_values._0_._m_objectData._m_ttc._m_value"
      triggers:
        - signal: "_g_Common_VAG_..._WBA_Status_dAB"
          condition: becomes
          value: 4
    format: ".2f"

  - col_index: 4
    header: "VW Activated TTC (s)"
    description: "VW激活(VW=4)时的TTC"
    extract:
      method: cross_reference
      target: "_g_Common_VAG_..._m_values._0_._m_objectData._m_ttc._m_value"
      triggers:
        - signal: "_g_Common_VAG_..._WBA_Status_VW"
          condition: becomes
          value: 4
    format: ".2f"

result_source: Trace_Record
```

注：每个 Scenario 信号路径可能略有不同，在配置中按场景调整。

## 6. 架构设计

```
pptx_agent/                       # 新建模块
├── __init__.py
├── table_mapping.yaml            # 信号→表格列映射配置
├── ppt_report_tool.py            # PPT 报告生成工具
│   ├── analyze_template()        # 分析 PPT 结构
│   ├── read_trace_record()       # 读取 Trace Record.xlsx
│   ├── match_traces()            # 匹配 MF4 文件 → 场景
│   ├── populate_slide1()         # 填 Slide 1（XML 元数据 + ECU 表）
│   ├── replace_scenario_images() # 替换场景图片（1-8.PNG）
│   ├── fill_cpla_table()         # 填 CPLA 表格（MF4 信号提取）
│   └── generate_report()         # 主流程
└── template_config.json          # 模板映射配置
```

## 7. 实施步骤

### Step 1: 基础环境 [x]
- [x] `python-pptx`, `openpyxl`, `Pillow` 已安装
- [x] PPT 模板结构已分析 (20页)
- [x] Trace Record.xlsx 结构已分析

### Step 2: 创建 pptx_agent 模块 [ ]
- [ ] 创建 `pptx_agent/` 目录
- [ ] 创建 `table_mapping.yaml` 信号映射配置
- [ ] 实现 `read_trace_record()`: 读取 Excel，返回场景→trace映射
- [ ] 实现 `match_traces()`: 对比 Trace Record 和实际 MF4 文件

### Step 3: 图片替换 [ ]
- [ ] 建立 PNG→Shape 映射表
- [ ] 实现 `replace_scenario_images()`: 遍历场景文件夹，1:1 替换 8 张图片
- [ ] 处理 Slide 7, 10 缺少文本框的问题

### Step 4: 表格数据填充 [ ]
- [ ] 加载 `table_mapping.yaml` 配置
- [ ] 复用 `cross_reference()` 提取 TTC 值（保留两位小数）
- [ ] 实现 `fill_cpla_table()`: 填充 Slide 2-5 的 TTC 表格
- [ ] 读取 Trace Record 填 Result 列

### Step 5: Slide 1 元数据 [ ]
- [ ] 解析 XML 提取 VIN、ECU 信息
- [ ] 根据 ECU 名称映射填充 ECU 配置表

### Step 6: 端到端测试 [ ]
- [ ] 用 A5L 99C WBA LRR Y653 数据生成报告
- [ ] 验证图片替换正确
- [ ] 验证表格 TTC 值与 CANape 一致

## 8. 关键设计决策

| 决策点 | 方案 | 理由 |
|--------|------|------|
| 架构定位 | 独立 `pptx_agent/` 模块 | 报告生成是确定性流程，无需 LLM |
| 场景选择 | 数据文件夹存在 → 做该页PPT | 文件夹是地面真相 |
| 信号映射 | YAML 配置文件 | 换模板/换信号只需改配置 |
| 图片替换 | 按 Shape name 定位 + 1:1 PNG 序号 | 模板 layout 固定 |
| 表格填充 | `cross_reference()` + MF4 信号提取 | 复用现有工具 |
| 信号映射 | YAML 完整路径，每列独立配置 | 换信号只需改配置，每个信号独立完整路径 |
