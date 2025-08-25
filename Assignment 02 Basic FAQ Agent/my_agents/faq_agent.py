from agents import Agent
from my_config.gemini_config import GEMINI_MODEL



faq_agent = Agent(
    name="FAQ Agent",
    instructions="You are a helpful FAQ bot.",
    model=GEMINI_MODEL
)