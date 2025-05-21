from typing import Dict, List, Any, Callable
from pydantic import BaseModel
from openai import OpenAI
import config

class Tool(BaseModel):
    name: str
    description: str
    function: Callable

class LLM:
    def __init__(self):
        self.client = OpenAI(
            api_key=config.OPENAI_API_KEY,
            base_url=config.OPENAI_BASE_URL
        )
    
    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            stream=False,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

class Agent:
    def __init__(self):
        self.llm = LLM()
        # 验证是否成功注册llm
        print(self.llm.generate("你好"))
        self.tools: Dict[str, Tool] = {}
    
    def register_tool(self, tool: Tool):
        self.tools[tool.name] = tool
    
    def get_tool(self, name: str) -> Tool:
        return self.tools.get(name)
    
    def list_tools(self) -> List[str]:
        return list(self.tools.keys()) 