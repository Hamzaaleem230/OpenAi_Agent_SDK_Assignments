from my_agents.agent import agent
from agents import Runner, set_tracing_disabled


set_tracing_disabled(True)


res = Runner.run_sync(starting_agent=agent, input="hi")
print(res.final_output)
