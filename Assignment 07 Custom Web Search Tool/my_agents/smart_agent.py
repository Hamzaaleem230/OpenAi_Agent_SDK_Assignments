from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_tool.web_search_tool import web_search_tool



smart_agent = Agent(
    name="🤖 Smart Agent",
    instructions="""
    You are Smart Agent.  
    Your task is to answer user questions.  
    If the information is already in your knowledge, respond directly.  
    If the information is not available, use the Tavily Search Tool to fetch it from the web and provide a summarized answer.  
    Always give helpful, clear, and concise responses.
    """,
    model=GEMINI_MODEL,
    tools=[web_search_tool]
)
