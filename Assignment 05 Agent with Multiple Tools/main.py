from agents import Runner, set_tracing_disabled
from my_agents.gemini_agent import smart_agent


set_tracing_disabled(True)


while True:
    prompt = input("Enter your prompt: ")
        
    if prompt == "exit":
        break

    response = Runner.run_sync(starting_agent=smart_agent, input=prompt)
    print(response.final_output)