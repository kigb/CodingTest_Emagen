from agent.base import Agent
from workflows.simple_workflow import Workflow
from tools.example_tools import (
    add_tool, multiply_tool, divide_tool,
    weather_tool, air_quality_tool,
    count_words_tool, extract_keywords_tool, translate_tool,
    filter_list_tool, sort_list_tool,
    current_time_tool, time_diff_tool
)

def main():
    # 创建agent实例
    agent = Agent()
    
    # 注册所有工具
    tools = [
        add_tool, multiply_tool, divide_tool,
        weather_tool, air_quality_tool,
        count_words_tool, extract_keywords_tool, translate_tool,
        filter_list_tool, sort_list_tool,
        current_time_tool, time_diff_tool
    ]
    
    for tool in tools:
        agent.register_tool(tool)
    
    # 示例1：数学运算workflow
    print("示例1：数学运算workflow")
    workflow1 = Workflow(agent)
    workflow1.add_tool("add")
    workflow1.add_tool("multiply")
    workflow1.add_tool("divide")
    
    result1 = workflow1.execute({
        "a": 10,
        "b": 5
    })
    print("Workflow1 result:", result1)
    
    # 示例2：天气信息workflow
    print("\n示例2：天气信息workflow")
    workflow2 = Workflow(agent)
    workflow2.add_tool("weather")
    workflow2.add_tool("air_quality")
    
    result2 = workflow2.execute({
        "city": "Beijing"
    })
    print("Workflow2 result:", result2)
    
    # 示例3：文本处理workflow
    print("\n示例3：文本处理workflow")
    workflow3 = Workflow(agent)
    workflow3.add_tool("count_words")
    workflow3.add_tool("extract_keywords")
    workflow3.add_tool("translate")
    
    result3 = workflow3.execute({
        "text": "This is a sample text for demonstration",
        "target_language": "Chinese"
    })
    print("Workflow3 result:", result3)
    
    # # 示例4：使用text2workflow自动创建workflow
    # print("\n示例4：使用text2workflow自动创建workflow")
    # description = "计算10和5的和，然后乘以2，最后查询北京的天气和空气质量"
    # workflow4 = Workflow.text2workflow(agent, description)
    
    # result4 = workflow4.execute({
    #     "a": 10,
    #     "b": 5,
    #     "city": "Beijing"
    # })
    # print("Workflow4 result:", result4)

if __name__ == "__main__":
    main() 