from agents import Runner, set_tracing_disabled
from my_agents.smart_agent import smart_agent

set_tracing_disabled(True)


while True:
    print("✨ Smart Agent activated! How can I help you today?")
    print("💡 Type 'exit' anytime to close the assistant.\n")
    prompt = input("👨🏻‍🦱 You: ")
    
    if prompt.lower() == "exit":
        print("🔒 Exiting Smart Agent... Session closed.")
        break

    
    res = Runner.run_sync(
        starting_agent=smart_agent,
        input=prompt
    )

    print("🤖 Bot:", res.final_output)