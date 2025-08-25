from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_tool.weather_tool import get_weather



weather_agent = Agent(
    name="Weather Agent",
    instructions="You are a weather agent.",
    model=GEMINI_MODEL,
    tools=[get_weather]
)