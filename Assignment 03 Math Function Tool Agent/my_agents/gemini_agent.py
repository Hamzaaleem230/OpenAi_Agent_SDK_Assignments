from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_tools.tool import add, subtract, multiply, divide



gemini_agent = Agent(
    name="Math Function Tool Agent",
    instructions="You are a math function tool agent.",
    model=GEMINI_MODEL,
    tools=[add, subtract, multiply, divide]
)