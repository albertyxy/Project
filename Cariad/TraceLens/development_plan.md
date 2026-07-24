# TraceLens PPT 报告生成功能 - 开发计划

## 1. PPT 模板结构

**文件**: `data/Template/Test Template.pptx` | 20 页 | 13.3x7.5 英寸

### Slide 1 - ECU 配置页

```
标题: "02 ECU Configuration" (Rectangle 3)
副标题: "WBA functions related ECU status" (Title 7)
描述: "Test vehicle actual configuration" (Subtitle 6)
表格 Table 19 (8行x6列):
  r0: Configuration of relevant ECU
  r1: Vehicle: {车型}, VIN: {VIN}           ← 从 XML 填充
  r2: Main-SG | Software-TNR. | Software-Version | ZDC/DS-version | Hardware-TNR. | Hardware-Version
  r3-r7: {ECU名} | {SWTeilenummer} | {SWVersion} | {ZdcName}[{ZdcVersion}] | {HWTeilenummer} | {HWVersion}
```

### Slide 2-20 - 场景分析页（19 页）

**每页统一布局:**
| 位置 | Shape | 说明 |
|------|-------|------|
| 顶部标题栏 | Rectangle 3 (13.3x0.7in) | "05 Trace Analysis" |
| 左侧文本框 | 文本框 2 (5.7x5.3in) | Scenario/Result/Trace 信息 |
| **8 张图片** | 见下节 | 按从左到右、从上到下排列 |

### 图片映射（8 张图通用规则）

每个场景 slide 有 8 个图片 shape，其 Shape Name 随 slide 不同而变化（如 Picture 16 / Picture 7 / Picture 18 等）。图片替换**不应硬编码 shape name**，而是按 shape 位置排序后 1:1 对应：

```
算法:
1. 获取 slide 上所有带 image 的 shape
2. 按 Y 坐标分行（Y 容差 0.4in 内视为同一行）
3. 每行内按 X 坐标从左到右排序
4. 按行序展开为列表 shapes[0..7]
5. 替换: 1.PNG -> shapes[0], 2.PNG -> shapes[1], ..., 8.PNG -> shapes[7]
```

以 Slide 2 (CPLA-25_Night_20kph) 为例，排序后的映射：
| 序号 | 视觉位置 | 典型 Shape Name |
|------|---------|----------------|
| 1.PNG | 左上大图 | Picture 16 |
| 2.PNG | 左上小图 | Picture 6 |
| 3.PNG | 左中上图 | Picture 23 |
| 4.PNG | 右侧 Run1 大图 | Picture 30 |
| 5.PNG | 左中下图 | Picture 26 |
| 6.PNG | 右侧 Run2 大图 | Picture 34 |
| 7.PNG | 左下大图 | Picture 19 |
| 8.PNG | 右侧 Run3 大图 | Picture 8 |

图片不存在时，对应 shape 替换为空（空白）。

### 场景表格结构

每个场景 slide 模板中均自带表格。表格的列结构因场景而异，由 `pptx_agent/table_mapping.yaml` 按场景名定义。填表时查 YAML 获取列定义，更新模板表格数据即可。

**已明确列结构的场景:**

| 场景 | 列结构 |
|------|--------|
| CPLA-25_Night_20/40kph | Case \| Result \| Radar Confirm TTC (s) \| Confirm as pedestrian TTC (s) \| **Brake** Activated TTC (s) |
| CPLA-25_Night_60/80kph | Case \| Result \| Radar Confirm TTC (s) \| Confirm as pedestrian TTC (s) \| **VW** Activated TTC (s) |
| CPTA-LN/CPTA-LF (all) | Case \| Result \| V_impact (km/h) |
| CPNCO/CBNAO/C2C SCP | 待补充 (YAML 中已预留占位) |

> CPTA 的 V_impact 值从 Trace Record.xlsx `Vimpact (km/h)` 列读取。

### 左侧文本框内容

模板原始格式:
```
Scenario
{场景名}

Trace
Run1: {MF4文件名}
Run2: {MF4文件名}
Run3: {MF4文件名}
```

需更新为:
```
Scenario
{场景名}

Result
Run1: {Pass/Collision/Failed}[ - V_impact = {值} kph]
Run2: {Pass/Collision/Failed}[ - V_impact = {值} kph]
Run3: {Pass/Collision/Failed}[ - V_impact = {值} kph]

Trace
Run1: {MF4文件名}
Run2: {MF4文件名}
Run3: {MF4文件名}
```

**V_impact 追加规则:**
- 仅当 Result = `Collision` 时，在该 Run 行末尾追加 ` - V_impact = {值} kph`
- V_impact 值从 Trace Record.xlsx `Vimpact (km/h)` 列读取（保留原始精度）
- Pass 或 Failed 不追加

**Result 颜色规则:**
| Result 值 | 字体颜色 |
|-----------|---------|
| Pass | 绿色 |
| Collision | 橙色 (不含后面 ` - V_impact = ...`) |
| Failed | 红色 |
| (空/无数据) | 灰色 "/" |

**Run 数量处理:**
- Trace Record 中某个场景有 >3 个 run → 只取前 3 个
- Trace Record 中某个场景有 <3 个 run → 有几个写几个（多余的 Run 行留空）

### 场景->幻灯片映射

| Slide | 场景文件夹 |
|-------|-----------|
| 2 | CPLA-25_Night_20kph |
| 3 | CPLA-25_Night_40kph |
| 4 | CPLA-25_Night_60kph |
| 5 | CPLA-25_Night_80kph |
| 6 | CPNCO-25_20kph |
| 7 | CPNCO-25_40kph |
| 8 | CBNAO-50_20kph |
| 9 | CBNAO-50_40kph |
| 10 | CBNAO-50_60kph |
| 11 | CPTA-LN-50_10kph |
| 12 | CPTA-LN-50_20kph |
| 13 | CPTA-LN-50_30kph |
| 14 | CPTA-LF-50_10kph |
| 15 | CPTA-LF-50_20kph |
| 16 | CPTA-LF-50_30kph |
| 17 | C2C SCP_30kph |
| 18 | C2C SCP_40kph |
| 19 | C2C SCP_50kph |
| 20 | C2C SCP_60kph |

---

## 2. Trace Record 数据结构

**文件**: `data/{项目名}/Trace Record.xlsx` | Sheet: "A5L"

**关键列 (B-L):**
| 列 | 名称 | 说明 |
|----|------|------|
| B | Scenario | 测试场景名 |
| C | Function | AEB / FCW |
| D | VVUT | 测试速度 (km/h) |
| F | Overlap | 重叠率 |
| G | Runs | run1/run2/run3(/run4) |
| H | Pass/No | Pass / Collision / Failed / (空=未测试) |
| I | CANape Trace | MF4 文件名 |
| K | FCW_TTC (s) | TTC 值 |
| L | Vimpact (km/h) | 碰撞速度 |

**文件夹名构造规则:**
```
文件夹名 = Scenario.replace('\n', '_') + "_" + VVUT + "kph"
例如: "CPLA-25\nNight" + "_" + "20" + "kph" → "CPLA-25_Night_20kph"
```

> 注：Scenario 列中原始数据可能包含换行符（如 `CPLA-25\nNight`），读取后需 `replace('\n', '_')` 处理。

---

## 3. Trace 匹配流程

**核心逻辑：数据文件夹是地面真相。**

```
1. 扫描 data/{项目名}/ 下所有场景文件夹
2. 对每个场景文件夹：
   a. 根据文件夹名匹配 PPT 中对应 Slide（通过文本框 Scenario 名）
   b. 去 Trace Record.xlsx 找 Scenario 列匹配 + VVUT 匹配的行（Scenario+VVUT 是充分条件，忽略 Function）
   c. 读取 Run1/2/3 的 CANape Trace 名、Pass/No 状态、Vimpact 值
   d. 在 data/{项目名}/ 下查找对应的 MF4 文件
   e. 如果 MF4 存在 → 提取信号数据填表
   f. 如果 MF4 不存在 → 表格填 "/"
3. 没有对应数据文件夹的 Slide → 删除该页（python-pptx 需通过操作 slide XML 删除）
```

**MF4 文件位置**: 所有 MF4 统一存放在 `data/{项目名}/` 目录下（非场景子文件夹）。

**Run 数量处理:**
- Excel 中某场景有 run4 → 忽略，只取 run1/run2/run3
- Excel 中某场景只有 run1/run2 → 只填 2 行，Run3 留空
- PPT 模板始终显示 3 个 Run 标签

---

## 4. XML -> Slide 1 ECU 配置映射

**XML 文件**: `data/{项目名}/*.xml`

| XML 字段 | PPT 用途 |
|----------|---------|
| `Fahrgestellnummer` | Slide 1 VIN |
| `UserProjekt` | Slide 1 车型名 |
| `WegStrecke` + `EinheitWegStrecke` | Slide 1 里程 |

**ECU 映射（通过 XML `Systembezeichnung` 字段匹配）:**

| PPT 行 | PPT ECU 名 | XML Systembezeichnung | XML 字段来源 |
|--------|-----------|----------------------|-------------|
| r3 | LRR | "WBA Bosch PPE" | SWTeilenummer, SWVersion, ZdcName, ZdcVersion, HWTeilenummer, HWVersion |
| r4 | MFK | "MFK5" | 同上 |
| r5 | HCP1 | "HCP1 BOSCH EP" | 同上 |
| r6 | NR | "Nanoradar 1" | 同上 |
| r7 | ESC | "ABS" | 同上 |

**填充格式:**
```
Software-TNR.: {SWTeilenummer}
Software-Version: {SWVersion}
ZDC/DS-version: {ZdcName}[{ZdcVersion}]
Hardware-TNR.: {HWTeilenummer}
Hardware-Version: {HWVersion}
```

---

## 5. 表格信号映射（YAML 配置）

信号->表格列的映射写在 `pptx_agent/table_mapping.yaml`，**按场景名组织**，不同场景的表格结构不同。

### YAML 结构设计

```yaml
# pptx_agent/table_mapping.yaml
# 按场景名组织，每个场景独立定义表格结构

scenarios:
  "CPLA-25_Night_20kph":
    table:
      rows: 4       # 表头 + 3个Run
      cols: 5
    columns:
      - col_index: 0
        header: "Case"
        source: fixed
      - col_index: 1
        header: "Result"
        source: trace_record   # 从 Trace Record Pass/No 列读取
      - col_index: 2
        header: "Radar Confirm TTC (s)"
        description: "雷达+摄像头均确认目标时的TTC"
        extract:
          method: cross_reference
          target: "_g_Common_VAG_Function_SafetyFunctions_SfRunnableMainProc_SfRunnableMainProc_m_portMainProc_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem.MainProcSfBase._._m_targetObjList._m_memory._m_values._0_._m_objectData._m_ttc._m_value"
          triggers:
            - signal: "_g_Common_VAG_Function_SafetyFunctions_SfRunnableMainProc_SfRunnableMainProc_m_portMainProc_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem.MainProcSfBase._._m_targetObjList._m_memory._m_values._0_._m_objectData._m_camConfirmation"
              condition: equals
              value: 1
            - signal: "_g_Common_VAG_Function_SafetyFunctions_SfRunnableMainProc_SfRunnableMainProc_m_portMainProc_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem.MainProcSfBase._._m_targetObjList._m_memory._m_values._0_._m_objectData._m_radarConfirmation"
              condition: equals
              value: 1
          format: ".2f"
      - col_index: 3
        header: "Confirm as pedestrian TTC (s)"
        description: "确认为行人时的TTC"
        extract:
          method: cross_reference
          target: "_g_Common_VAG_Function_SafetyFunctions_SfRunnableMainProc_SfRunnableMainProc_m_portMainProc_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem.MainProcSfBase._._m_targetObjList._m_memory._m_values._0_._m_objectData._m_ttc._m_value"
          triggers:
            - signal: "_g_Common_VAG_Function_SafetyFunctions_SfRunnableMainProc_SfRunnableMainProc_m_portMainProc_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem.MainProcSfBase._._m_targetObjList._m_memory._m_values._0_._m_objectData._m_camConfirmation"
              condition: equals
              value: 1
            - signal: "_g_Common_VAG_Function_SafetyFunctions_SfRunnableMainProc_SfRunnableMainProc_m_portMainProc_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem.MainProcSfBase._._m_targetObjList._m_memory._m_values._0_._m_objectData._m_radarConfirmation"
              condition: equals
              value: 1
            - signal: "_g_Common_VAG_Function_SafetyFunctions_SfRunnableMainProc_SfRunnableMainProc_m_portMainProc_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem.MainProcSfBase._._m_targetObjList._m_memory._m_values._0_._m_objectData._m_targetObjType"
              condition: equals
              value: "pedestrian"
          format: ".2f"
      - col_index: 4
        header: "Brake Activated TTC (s)"
        description: "制动激活时的TTC"
        extract:
          method: cross_reference
          target: "_g_Common_VAG_Function_SafetyFunctions_SfRunnableMainProc_SfRunnableMainProc_m_portMainProc_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem.MainProcSfBase._._m_targetObjList._m_memory._m_values._0_._m_objectData._m_ttc._m_value"
          triggers:
            - signal: "_g_Common_VAG_Function_SafetyFunctions_SfRunnablePostProc_SfRunnablePostProc_m_portWBA05_out_local.TChangeableMemPool._._._m_arrayPool._1_._elem._m_DE_SG_WBA_05_st._WBA_Status_dAB"
              condition: becomes
              value: 4
          format: ".2f"

  "CPLA-25_Night_40kph":
    # 与 20kph 相同结构，使用 Brake Activated TTC
    $ref: "CPLA-25_Night_20kph"

  "CPLA-25_Night_60kph":
    table:
      rows: 4
      cols: 5
    columns:
      - col_index: 0
        header: "Case"
        source: fixed
      - col_index: 1
        header: "Result"
        source: trace_record
      - col_index: 2
        header: "Radar Confirm TTC (s)"
        description: "雷达+摄像头均确认目标时的TTC"
        extract:
          method: cross_reference
          target: "_g_Common_VAG_Function_SafetyFunctions_SfRunnableMainProc_SfRunnableMainProc_m_portMainProc_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem.MainProcSfBase._._m_targetObjList._m_memory._m_values._0_._m_objectData._m_ttc._m_value"
          triggers:
            - signal: "_g_Common_VAG_Function_SafetyFunctions_SfRunnableMainProc_SfRunnableMainProc_m_portMainProc_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem.MainProcSfBase._._m_targetObjList._m_memory._m_values._0_._m_objectData._m_camConfirmation"
              condition: equals
              value: 1
            - signal: "_g_Common_VAG_Function_SafetyFunctions_SfRunnableMainProc_SfRunnableMainProc_m_portMainProc_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem.MainProcSfBase._._m_targetObjList._m_memory._m_values._0_._m_objectData._m_radarConfirmation"
              condition: equals
              value: 1
          format: ".2f"
      - col_index: 3
        header: "Confirm as pedestrian TTC (s)"
        description: "确认为行人时的TTC"
        extract:
          method: cross_reference
          target: "_g_Common_VAG_Function_SafetyFunctions_SfRunnableMainProc_SfRunnableMainProc_m_portMainProc_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem.MainProcSfBase._._m_targetObjList._m_memory._m_values._0_._m_objectData._m_ttc._m_value"
          triggers:
            - signal: "_g_Common_VAG_Function_SafetyFunctions_SfRunnableMainProc_SfRunnableMainProc_m_portMainProc_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem.MainProcSfBase._._m_targetObjList._m_memory._m_values._0_._m_objectData._m_camConfirmation"
              condition: equals
              value: 1
            - signal: "_g_Common_VAG_Function_SafetyFunctions_SfRunnableMainProc_SfRunnableMainProc_m_portMainProc_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem.MainProcSfBase._._m_targetObjList._m_memory._m_values._0_._m_objectData._m_radarConfirmation"
              condition: equals
              value: 1
            - signal: "_g_Common_VAG_Function_SafetyFunctions_SfRunnableMainProc_SfRunnableMainProc_m_portMainProc_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem.MainProcSfBase._._m_targetObjList._m_memory._m_values._0_._m_objectData._m_targetObjType"
              condition: equals
              value: "pedestrian"
          format: ".2f"
      - col_index: 4
        header: "VW Activated TTC (s)"
        description: "VW激活时的TTC"
        extract:
          method: cross_reference
          target: "_g_Common_VAG_Function_SafetyFunctions_SfRunnableMainProc_SfRunnableMainProc_m_portMainProc_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem.MainProcSfBase._._m_targetObjList._m_memory._m_values._0_._m_objectData._m_ttc._m_value"
          triggers:
            - signal: "_g_Common_VAG_Function_SafetyFunctions_SfRunnablePostProc_SfRunnablePostProc_m_portWBA05_out_local.TChangeableMemPool._._._m_arrayPool._1_._elem._m_DE_SG_WBA_05_st._WBA_Status_VW"
              condition: becomes
              value: 4
          format: ".2f"

  "CPLA-25_Night_80kph":
    $ref: "CPLA-25_Night_60kph"

  "CPTA-LN-50_10kph":
    table:
      rows: 4
      cols: 3
    columns:
      - col_index: 0
        header: "Case"
        source: fixed
      - col_index: 1
        header: "Result"
        source: trace_record
      - col_index: 2
        header: "V_impact (km/h)"
        source: trace_record    # 从 Trace Record Vimpact 列读取
        format: ".3f"

  "CPTA-LN-50_20kph":
    $ref: "CPTA-LN-50_10kph"

  "CPTA-LN-50_30kph":
    $ref: "CPTA-LN-50_10kph"

  "CPTA-LF-50_10kph":
    $ref: "CPTA-LN-50_10kph"

  "CPTA-LF-50_20kph":
    $ref: "CPTA-LN-50_10kph"

  "CPTA-LF-50_30kph":
    $ref: "CPTA-LN-50_10kph"

  # -- 以下场景表格结构待补充，预留占位 --
  "CPNCO-25_20kph":
    # TODO: 列结构待确认
    table:
      rows: 4
      cols: 0   # 待补充
    columns: []

  "CPNCO-25_40kph":
    $ref: "CPNCO-25_20kph"

  "CBNAO-50_20kph":
    # TODO: 列结构待确认
    table:
      rows: 4
      cols: 0
    columns: []

  "CBNAO-50_40kph":
    $ref: "CBNAO-50_20kph"

  "CBNAO-50_60kph":
    $ref: "CBNAO-50_20kph"

  "C2C SCP_30kph":
    # TODO: 列结构待确认
    table:
      rows: 4
      cols: 0
    columns: []

  "C2C SCP_40kph":
    $ref: "C2C SCP_30kph"

  "C2C SCP_50kph":
    $ref: "C2C SCP_30kph"

  "C2C SCP_60kph":
    $ref: "C2C SCP_30kph"
```

> 每个信号使用其独立完整路径，无需统一 slot 编号。

### cross_reference() 参数映射

YAML 中 `extract` 字段与 `cross_reference()` 参数一一对应，`fill_scenario_table()` 直接转换调用：

```python
result = cross_reference(
    file_path=mf4_path,
    target_signals=[col["extract"]["target"]],   # YAML 单值 -> 列表
    triggers=col["extract"]["triggers"],          # 直接透传
    max_points=1,
)
# 返回值: [{"timestamp": ..., "targets": {target信号全名: 值}}]
cell_value = format(result[0]["targets"][col["extract"]["target"]], col["extract"]["format"])
```

无 MF4 或 `cross_reference()` 返回空列表时，填 `"/"`。

### 填表流程

```
1. 根据场景名查 table_mapping.yaml 获取列定义
2. 找到模板表格，按列定义更新数据
3. 每列的 source 字段决定数据来源:
   - fixed: 固定值 (如 "Run1")
   - trace_record: 从 Trace Record.xlsx 读取
   - cross_reference: 按上方参数映射调用 cross_reference()
4. cross_reference 类型的列仅在 MF4 文件存在时执行，否则填 "/"
```

---

## 6. 架构设计

```
pptx_agent/                       # 新建模块
  __init__.py
  table_mapping.yaml              # 信号->表格列映射配置 (按场景组织)
  ppt_report_tool.py              # PPT 报告生成工具
    read_trace_record()           # 读取 Trace Record.xlsx，清洗数据
    match_traces()                # 匹配 MF4 文件 -> 场景 -> Slide
    delete_unused_slides()        # 删除无对应数据文件夹的 slide
    populate_slide1()             # 填 Slide 1 (XML 元数据 + ECU 表)
    replace_scenario_images()     # 替换场景图片 (1-8.PNG，按位置排序)
    fill_scenario_table()         # 填场景表格 (MF4 信号提取或 Trace Record)
    fill_scenario_text()          # 填场景文本框 (Scenario/Result/Trace, Collision加V_impact)
    generate_report()             # 主流程入口
  template_config.json            # 模板路径和场景->Slide 映射
```

**generate_report() 执行顺序:**

```
read_trace_record()
  → match_traces()
  → delete_unused_slides()       # 删除无数据文件夹的 slide
  → populate_slide1()            # 填 ECU 配置页
  → for 每个有数据的场景 slide:
      replace_scenario_images()  # 替换 8 张图
      fill_scenario_text()       # 填 Scenario/Result/Trace
      fill_scenario_table()      # 填表格
  → prs.save(output_path)
```

---

## 7. 实施步骤

### Step 1: 验证基础环境 [x]
- [x] `python-pptx`, `openpyxl`, `Pillow`, `asammdf` 在 conda `project` 环境可用
- [x] PPT 模板结构已分析 (20页，8 图片/slide)
- [x] Trace Record.xlsx 结构已分析
- [x] XML ECU 字段映射已验证
- [x] MF4 信号路径已验证（实际路径与 YAML 需精确对应）

### Step 2: 创建 pptx_agent 模块框架 [ ]
- [ ] 创建 `pptx_agent/` 目录和 `__init__.py`
- [ ] 创建 `table_mapping.yaml`（按场景组织，信号路径按上述 YAML 示例写入）
- [ ] 实现 `read_trace_record()`:
  - 读取 Excel，处理 Scenario 换行符 (`\n` -> `_`)
  - 归一化 Pass/No 值 (Pass/Collision/Failed)
  - 构造 `{文件夹名: {run1: {trace, result, vimpact}, run2: {...}, run3: {...}}}` 字典
- [ ] 实现 `match_traces()`:
  - 扫描场景文件夹 -> 匹配 Trace Record -> 查找 MF4 文件
  - MF4 查找路径: `data/{项目名}/*.MF4`
- [ ] 实现 `delete_unused_slides()`:
  - 遍历 Slide 2-20，无对应数据文件夹的 slide 删除（python-pptx 需操作 XML）

### Step 3: 图片替换 [ ]
- [ ] 实现 `replace_scenario_images()`:
  - 对每个场景 slide，获取所有图片 shape
  - 按 Y 分行 (容差 0.4in)，行内按 X 排序 -> 得到 8 个 shape 的有序列表
  - 1:1 替换: `{场景文件夹}/i.PNG` -> shapes[i-1]
  - PNG 不存在时置空对应 shape

### Step 4: 表格数据填充 [ ]
- [ ] 加载 `table_mapping.yaml` 配置
- [ ] 实现 `fill_scenario_table()`:
  - 查 YAML 获取该场景的列定义
  - 更新模板表格数据
  - 根据每列 `source` 字段分流数据来源
- [ ] Trace Record 来源列: 填 Result (带颜色)、V_impact
- [ ] cross_reference 来源列: 仅在 MF4 存在时执行提取，否则填 "/"
- [ ] Result 列颜色: Pass=绿色, Collision=橙色, Failed=红色

### Step 5: Slide 1 元数据 [ ]
- [ ] 解析 XML 提取 VIN、车型、里程
- [ ] 根据 ECU `Systembezeichnung` 匹配并填充 5 行 ECU 配置

### Step 6: 场景文本框填充 [ ]
- [ ] 实现 `fill_scenario_text()`:
  - 更新 Scenario 名、Result (3 run)、Trace (3 run)
  - Result 值带颜色: Pass=绿, Collision=橙色, Failed=红
  - Collision 行追加 ` - V_impact = {值} kph` (值来源 Trace Record)
  - 不足 3 个 run -> 有几个填几个

### Step 7: 端到端测试 [ ]
- [ ] 用 A5L 99C WBA LRR Y653 数据生成报告
- [ ] 验证图片替换正确 (按位置排序)
- [ ] 验证表格 TTC 值与 CANape 一致 (有 MF4 的 Run)
- [ ] 验证文本框颜色正确

---

## 8. 关键设计决策

| 决策点 | 方案 | 理由 |
|--------|------|------|
| 架构定位 | 独立 `pptx_agent/` 模块 | 报告生成是确定性流程，无需 LLM |
| 图片映射 | 按 shape 位置排序，不硬编码 shape name | 不同 slide 用不同 shape name，位置排序通用 |
| 场景选择 | 数据文件夹存在 -> 做该页 PPT | 文件夹是地面真相 |
| YAML 结构 | **按场景名组织**，每场景独立定义列 | 不同场景表格结构不同 (CPLA 5列, CPTA 3列) |
| 表格填充 | 更新模板表格，按 YAML 列定义填充 | 所有 slide 模板均有表格 |
| 信号映射 | YAML 完整路径，每列独立配置 | 换信号只需改配置 |
| MF4 查找 | `data/{项目名}/` 目录下统一查找 | MF4 不在场景子文件夹 |
| Run 数量 | >3取前3，<3有几个填几个 | PPT 模板固定 3 个 Run |
| Result 颜色 | 代码中根据值自动着色 | Pass=绿, Collision=橙色, Failed=红 |
