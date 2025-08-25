from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_tool.smart_tool import add, subtract, multiply, divide, get_weather



smart_agent = Agent(
    name="Smart Agent",
    instructions="You are a helpful agent.",
    model=GEMINI_MODEL,
    tools=[add, subtract, multiply, divide, get_weather]
)