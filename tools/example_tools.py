from agent.base import Tool
from typing import List, Dict, Any
import random
import json
from datetime import datetime

# 基础数学运算
def add_numbers(a: int, b: int) -> int:
    return a + b

def multiply_numbers(a: int, b: int) -> int:
    return a * b

def divide_numbers(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("除数不能为0")
    return a / b

# 天气相关
def get_weather(city: str) -> str:
    # 模拟天气查询
    weather_types = ["Sunny", "Rainy", "Cloudy", "Snowy"]
    temperatures = range(15, 35)
    return f"Weather in {city}: {random.choice(weather_types)}, {random.choice(temperatures)}°C"

def get_air_quality(city: str) -> str:
    # 模拟空气质量查询
    aqi = random.randint(0, 500)
    quality = "Good" if aqi < 100 else "Moderate" if aqi < 200 else "Poor"
    return f"Air quality in {city}: {quality} (AQI: {aqi})"

# 文本处理
def count_words(text: str) -> int:
    return len(text.split())

def extract_keywords(text: str) -> List[str]:
    # 简单的关键词提取（这里只是示例，实际应该使用更复杂的算法）
    words = text.lower().split()
    return list(set([w for w in words if len(w) > 3]))

def translate_text(text: str, target_language: str) -> str:
    # 模拟翻译
    return f"[{target_language}] {text}"

# 数据处理
def filter_list(items: List[Any], condition: str) -> List[Any]:
    # 简单的列表过滤
    if condition == "even":
        return [x for x in items if isinstance(x, int) and x % 2 == 0]
    elif condition == "odd":
        return [x for x in items if isinstance(x, int) and x % 2 == 1]
    elif condition == "positive":
        return [x for x in items if isinstance(x, (int, float)) and x > 0]
    else:
        raise ValueError(f"Unsupported condition: {condition}")

def sort_list(items: List[Any], order: str = "asc") -> List[Any]:
    # 列表排序
    if order not in ["asc", "desc"]:
        raise ValueError("Order must be 'asc' or 'desc'")
    return sorted(items, reverse=(order == "desc"))

# 时间处理
def get_current_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def calculate_time_difference(time1: str, time2: str) -> str:
    # 计算两个时间字符串之间的差异
    try:
        t1 = datetime.strptime(time1, "%Y-%m-%d %H:%M:%S")
        t2 = datetime.strptime(time2, "%Y-%m-%d %H:%M:%S")
        diff = abs((t2 - t1).total_seconds())
        return f"Time difference: {diff:.2f} seconds"
    except ValueError:
        raise ValueError("Invalid time format. Use YYYY-MM-DD HH:MM:SS")

# 创建工具实例
add_tool = Tool(
    name="add",
    description="Add two numbers together",
    function=add_numbers
)

multiply_tool = Tool(
    name="multiply",
    description="Multiply two numbers together",
    function=multiply_numbers
)

divide_tool = Tool(
    name="divide",
    description="Divide first number by second number",
    function=divide_numbers
)

weather_tool = Tool(
    name="weather",
    description="Get weather information for a city",
    function=get_weather
)

air_quality_tool = Tool(
    name="air_quality",
    description="Get air quality information for a city",
    function=get_air_quality
)

count_words_tool = Tool(
    name="count_words",
    description="Count the number of words in a text",
    function=count_words
)

extract_keywords_tool = Tool(
    name="extract_keywords",
    description="Extract keywords from a text",
    function=extract_keywords
)

translate_tool = Tool(
    name="translate",
    description="Translate text to target language",
    function=translate_text
)

filter_list_tool = Tool(
    name="filter_list",
    description="Filter a list based on condition (even/odd/positive)",
    function=filter_list
)

sort_list_tool = Tool(
    name="sort_list",
    description="Sort a list in ascending or descending order",
    function=sort_list
)

current_time_tool = Tool(
    name="current_time",
    description="Get current time",
    function=get_current_time
)

time_diff_tool = Tool(
    name="time_difference",
    description="Calculate time difference between two timestamps",
    function=calculate_time_difference
) 