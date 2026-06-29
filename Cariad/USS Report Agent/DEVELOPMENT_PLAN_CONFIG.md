# 配置化重构计划 -- 通用 Agent + 多套模板配置

## 一、目标

将当前 `PPTReportTool` 中**硬编码的模板相关逻辑**抽离到 JSON 配置文件中，实现：

- 新增报告模板 → 只需新增/修改 JSON 配置，不改 Python 代码
- 同一套 Agent 逻辑支持多种模板（Q6、E6L、Q4 等）
- 模板描述文件独立于代码，非开发人员也可维护

## 二、需要新增的配置文件

```
USS Data/
├── template_config.json        ← 模板描述（Slide 结构、列布局、字段映射）
└── USSDB Test Report Template.pptx
```

> 新增模板 = 新增一个 `template_config.json`（或按模板命名如 `template_q6.json`）

## 三、template_config.json 结构设计

```jsonc
{
  "_comment": "USSDB Test Report 模板配置",

  // === 模板基本信息 ===
  "template_name": "USSDB Test Report",
  "template_file": "USSDB Test Report Template.pptx",

  // === Slide 1: 标题页 ===
  "title_slide": {
    "slide_index": 1,
    "title_shape_detection": "text contains 'USSDB' and 'Test Report'",
    "fields": {
      "vehicle_model": {
        "source": "xml",
        "xml_path": "UserProjekt",
        "transform": "extract_vehicle_model",
        "transform_rule": "regex: \\b(E\\d+)\\s*(L)?"
      }
    }
  },

  // === Slide 2: 车辆配置表格 ===
  "config_slide": {
    "slide_index": 2,
    "table_detection": "first table on slide",
    "rows": {
      "vehicle_vin": {
        "row_index": 1,
        "col_index": 0,
        "template": "Vehicle: {vehicle_model},  VIN: {vin}",
        "fields": {
          "vehicle_model": { "source": "xml", "xml_path": "UserProjekt", "transform": "extract_vehicle_model" },
          "vin": { "source": "xml", "xml_path": "Fahrgestellnummer" }
        }
      },
      "ecu_hcp1": {
        "row_index": 3,
        "ecu_match": { "field": "Systembezeichnung", "pattern": "HCP1" },
        "columns": {
          "1": { "label": "Software-TNR", "xml_field": "SWTeilenummer" },
          "2": { "label": "Software-Version", "xml_field": "SWVersion" },
          "3": { "label": "ZDC/DS-version", "xml_field": "ZdcName", "suffix_field": "ZdcVersion", "format": "{value} [{suffix}]" },
          "4": { "label": "Hardware-TNR", "xml_field": "HWTeilenummer" },
          "5": { "label": "Hardware-Version", "xml_field": "HWVersion" }
        }
      },
      "ecu_eps": {
        "row_index": 4,
        "ecu_match": { "field": "Systembezeichnung", "pattern": "EPS" },
        "columns": {
          "1": { "xml_field": "SWTeilenummer" },
          "2": { "xml_field": "SWVersion" },
          "3": { "xml_field": "ZdcName", "suffix_field": "ZdcVersion", "format": "{value} [{suffix}]" },
          "4": { "xml_field": "HWTeilenummer" },
          "5": { "xml_field": "HWVersion" }
        }
      }
    }
  },

  // === 数据来源 ===
  "data_sources": {
    "xml": {
      "file_pattern": "*.xml",
      "root_element": "Protokoll",
      "ecu_container": "Diagnosebloecke",
      "ecu_element": "Diagnoseblock"
    },
    "images": {
      "folder_pattern": "TS_FCT_USS_*",
      "file_types": {
        "chart": { "extensions": [".png"], "role": "test_result" },
        "photo": { "extensions": [".jpg", ".jpeg"], "role": "test" }
      }
    }
  },

  // === Driver Activity 标识提取 ===
  "driver_activity": {
    "regex": "Driver Activity:\\s*TS_FCT_USS_\\d+(?:\\s*[-&]?\\s*Action\\s*-?\\d+)*",
    "normalize": {
      "remove_spaces": true,
      "action_hyphen": "remove",
      "separator": " & "
    }
  },

  // === Slide 布局模式 ===
  "slide_layouts": {
    "default": {
      "strategy": "simple",
      "description": "全部图片 1:1 按序替换"
    },
    "ts_fct_uss_18": {
      "detection": "driver_activity contains 'TS_FCT_USS_18'",
      "strategy": "column_mode",
      "column_clustering": {
        "tolerance_emu": 150000,
        "columns": [
          { "position_order": 0, "name": "example", "role": "keep" },
          { "position_order": 1, "name": "test", "role": "replace", "image_role": "photo" },
          { "position_order": 2, "name": "test_result", "role": "replace", "image_role": "chart" }
        ]
      }
    }
  },

  // === 映射类型 ===
  "mapping_strategies": {
    "type_a": { "description": "1:1, Slide 独立对应一个文件夹", "allocation": "per_slide" },
    "type_b": { "description": "N:1, 连续多 Slide 共享文件夹", "allocation": "sequential_shared" },
    "type_c": { "description": "跨文件夹, & 分隔符", "allocation": "tail_head_combined" }
  },

  // === 图片处理 ===
  "image_processing": {
    "max_dimension": 1920,
    "format_conversion": {
      "MPO": { "target": "JPEG", "quality": 85 }
    }
  }
}
```

## 四、代码改动范围

| 文件 | 改动 |
|------|------|
| `app/tool/ppt_report_tool.py` | 构造函数接收 `config_path`；用配置替代硬编码常量 |
| `USS Data/template_config.json` | **新建** |
| 其他文件 | **不改** |

### 关键重构点

```
当前（硬编码）:
  _classify_image_columns()  → 假设3列，固定 Example/Test/Test Result
  _populate_metadata()       → 固定行号 1/3/4
  _parse_xml_metadata()      → 固定匹配 HCP1/EPS
  USS_DATA_ROOT              → 类常量

重构后（配置驱动）:
  _classify_image_columns()  → 从 config.slide_layouts 读取列定义
  _populate_metadata()       → 从 config.config_slide 读取行/列映射
  _parse_xml_metadata()      → 从 config.config_slide.rows 读取 ECU 匹配规则
  USS_DATA_ROOT              → 仍可用，但模板路径从 config 读取
```

## 五、兼容性

- 有 `template_config.json` → 按配置执行
- 无配置文件 → 降级使用当前硬编码逻辑（向后兼容）

## 六、后续扩展示例

新增一个 Q4 模板只需：

```jsonc
// USS Data/template_q4.json
{
  "template_name": "Q4 USSDB R4.2 Report",
  "template_file": "Q4_USSDB_Template.pptx",
  "title_slide": { ... },           // 可能结构不同
  "config_slide": { 
    "rows": {
      "ecu_hcp1": { "row_index": 3, ... },  // 行号可能不同
      "ecu_eps":  { "row_index": 4, ... },
      "ecu_new":  { "row_index": 5, ... }   // 新增 ECU
    }
  },
  "slide_layouts": {
    "ts_fct_uss_18": { ... },       // 列布局可能不同
    "custom_layout": { ... }        // 新增自定义布局
  }
}
```

Agent 代码一行不改。
