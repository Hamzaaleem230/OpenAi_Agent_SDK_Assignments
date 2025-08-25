from agents import Runner, set_tracing_disabled
from my_agent.BotAgent import BotAgent
from guardrail.my_guard import apply_guardrails

set_tracing_disabled(True)

while True:
    prompt = input("👨🏻‍🦱 You: ")

    if prompt.lower() in ["exit", "quit", "bye"]:
        print("🤖 Bot: 👋🏻 Goodbye!")
        break

    # Step 1: Run Agent
    res = Runner.run_sync(
        starting_agent=BotAgent,
        input=prompt,
    )

    # Step 2: Apply Guardrails
    res = apply_guardrails(prompt, res)

    # Step 3: Final output
    print(res.final_output)
