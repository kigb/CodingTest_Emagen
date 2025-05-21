# Agent Framework 面试项目

## 项目结构

```
.
├── agent/
│   └── base.py          # Agent基础框架
├── workflows/
│   └── simple_workflow.py  # 需要实现的Workflow
├── tools/
│   └── example_tools.py    # 示例工具
├── main.py              # 主程序
└── requirements.txt     # 项目依赖
```

## 任务说明
### 任务一 实现workflow的执行（25分）
需要实现 `workflows/simple_workflow.py` 中的 `Workflow.execute()` 方法。该方法需要：

1. 按照tools列表中的顺序依次执行工具
2. 每个工具的执行结果作为下一个工具的输入
3. 处理可能的错误情况
4. 返回最终的执行结果

### 任务2：实现 Workflow.text2workflow() （25分）
面试者需要实现 `workflows/simple_workflow.py` 中的 `Workflow.text2workflow()` 方法。该方法需要：

1. 使用LLM分析文本描述，理解用户意图
2. 根据可用的工具列表，选择合适的工具组合
3. 按照合理的顺序组织工具
4. 返回配置好的workflow实例

示例：
```python
description = "计算5和3的和，然后乘以2，最后查询北京的天气"
workflow = Workflow.text2workflow(agent, description)
# workflow.tools 应该包含 ["add", "multiply", "weather"]
```

## 运行方式

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 设置环境变量：
创建 `config.py` 文件并添加OPENAI_API_KEY和OPENAI_BASE_URL


3. 运行程序：
```bash
python main.py
```


