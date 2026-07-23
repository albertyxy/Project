# TraceLens

用自然语言分析 MF4 信号数据。输入一句话，自动提取信号、检测边沿、统计摘要、查找时间窗口、跨信号关联查询、生成可视化图片。

## 安装

```bash
pip install -r requirements.txt
```

## 配置

在项目根目录的 `.env` 文件中填入 LLM API 信息（OpenAI 兼容接口即可）：

```env
PLANNER_API_KEY=your_api_key
PLANNER_API_BASE=https://api.openai.com/v1
PLANNER_MODEL=qwen3.7-plus

CODER_API_KEY=your_api_key
CODER_API_BASE=https://api.openai.com/v1
CODER_MODEL=deepseek-v4-pro
```

## 使用

### Web 界面

```bash
streamlit run web/app.py
```

1. 侧边栏选择 MF4 文件
2. 底部输入框描述需求，例如：
   - `绘制 EPS_StgTq.Val 从 10s 到 30s 的波形`
   - `分析 USS_DALatHODInterpretation_en.Val 到 strong_grip_4 的跳变`
   - `统计 EPS_StgTq.Val 在 10s 到 30s 内的均值、最值和标准差`
   - `找出 EPS_StgTq.Val 大于 2.0 的所有时间窗口`
   - `当 WBA_Status_AWU 变到 1 时，WBA_CritObj_TTC 是多少`
3. 如需多信号对比：`绘制 EPS_StgTq.Val 和 LWI_AgStgWhl.Val 的波形`
4. 如果需求描述不够清楚，Agent 会追问你补充信息

