from agents import Runner, set_tracing_disabled
from my_agents.faq_agent import faq_agent

set_tracing_disabled(True)


while True:

    user_input = input("Enter your prompt: ")

    if user_input == "exit":
        break

    res = Runner.run_sync(
        starting_agent=faq_agent,
        input=user_input,
    )

    print(res.final_output)