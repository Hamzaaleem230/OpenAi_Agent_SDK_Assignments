from agents import Agent
from my_config.conf import MODEL



agent = Agent(
    name="Gemini Agent",
    instructions="You are a helpful asssistant.",
    model=MODEL
)