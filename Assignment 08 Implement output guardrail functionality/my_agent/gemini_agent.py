from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from guardrial_function.guardrial_input_function import guardrial_input_fuction
from guardrial_function.guardrial_output_function import guardrial_output_function


gemini_assistant = Agent(
    name="🤖 Gemini Assistant",
    instructions="You are a helpful Gemini assistant, your name is Jack.",
    model=GEMINI_MODEL,
    input_guardrails=[guardrial_input_fuction],
    output_guardrails=[guardrial_output_function]
)

