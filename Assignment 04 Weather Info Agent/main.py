from agents import Runner, set_tracing_disabled
from my_agents.weather_agent import weather_agent



set_tracing_disabled(True)


while True:
    
    prompt = input("Enter your prompt: ")
    
    if prompt == "exit":
        break
    
    res = Runner.run_sync(
        starting_agent=weather_agent,
        input=prompt
    )
    print(res.final_output)