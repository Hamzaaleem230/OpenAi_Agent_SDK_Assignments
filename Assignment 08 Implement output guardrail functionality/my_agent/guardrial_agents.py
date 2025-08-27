from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from data_schema.math_homework_output import MathHomeworkOutput

guardrial_agent = Agent(
    name="Guardrial Agent",
    instructions="""
    You must strictly analyze the input/output.\n
      - If the query is math related, set is_math_homework_query=True.\n
      - If the query is not math (general, political, etc.), set is_math_homework_query=False.\n
      - If the query or output contains political topics or references, set  is_avoid_political_topics_and_reference_query=True, else False.\n"
      - Always provide a short reasoning.
      """,
    model=GEMINI_MODEL,
    output_type=MathHomeworkOutput
)