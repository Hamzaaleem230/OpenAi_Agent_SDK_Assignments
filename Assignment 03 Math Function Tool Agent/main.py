from agents import Runner, set_tracing_disabled
from my_agents.gemini_agent import gemini_agent

set_tracing_disabled(True)





while True:
    
    user_input = input("Enter your prompt: ")
    
    if user_input == "exit":
        break
    
    res = Runner.run_sync(starting_agent=gemini_agent, input=user_input)
    print(res.final_output)