from agents import Runner, set_tracing_disabled, InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered
from my_agent.gemini_agent import gemini_assistant
from my_agent.guardrial_agents import guardrial_agent


set_tracing_disabled(True)

try:
    prompt =input("👤 User: ")
    res = Runner.run_sync(
        starting_agent=gemini_assistant,
        input=prompt
    )
    
    print("🤖 Bot:", res.final_output)

except InputGuardrailTripwireTriggered as e:
    print(f"Trip input \n {e}")
    
except OutputGuardrailTripwireTriggered as e:
    print(f"Trip output \n {e}")