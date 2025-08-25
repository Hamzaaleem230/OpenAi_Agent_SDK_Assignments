from agents import Agent, ModelSettings
from my_config.gemini_config import GEMINI_MODEL
from my_tool.get_order import get_order_status


BotAgent = Agent(
    name="🤖 Bot",
    instructions="""
    You are a professional and polite customer support assistant for an online store. 
    Your responsibilities are:
        - Answer FAQs about products, delivery, returns, and warranty.
        - If a user asks for order status, always use the get_order_status_by_id tool.
        - IMPORTANT: Never rephrase or change the tool’s output.
        - Always return the tool’s response exactly as it is, preserving emojis, arrows, and formatting.
        - If multiple orders are fetched, simply combine their outputs line by line.
        - Do not add bold text, do not reformat, do not summarize.
    """,
    model=GEMINI_MODEL,
    
    # Model settings used
    model_settings=ModelSettings(
        tool_choice="auto",
    ),
    
    # Tool call functions
    tools=[get_order_status],
    
)