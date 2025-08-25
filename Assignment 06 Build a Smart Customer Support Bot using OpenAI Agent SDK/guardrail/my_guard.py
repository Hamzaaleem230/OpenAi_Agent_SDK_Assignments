from agents import Runner
from my_agent.HumanAgent import HumanAgent
import logging

logging.basicConfig(filename='logs/events.log', level=logging.INFO)

NEGATIVE_WORDS = [
    "stupid", "useless", "angry", "complaint", 
    "worst", "hate", "frustrated"
]

UNSUPPORTED_INTENTS = [
    "cancel", "refund"
]

def apply_guardrails(prompt, bot_response):
    """
    Guardrail function: 
    - Detects negative sentiment or unsupported intents
    - Escalates to HumanAgent if needed
    - Adds clear HumanAgent label in output
    """

    # 1) Check negative words
    if any(word in prompt.lower() for word in NEGATIVE_WORDS):
        logging.info(f"Handoff: HumanAgent triggered by negative sentiment ('{prompt}')")
        print("🤖 Bot: ⚠️ I sense frustration. Escalating to a Human Agent...")
        res = Runner.run_sync(
            starting_agent=HumanAgent,
            input=prompt,
        )
        
        res.final_output = f"🤖 Bot (Human Agent): {res.final_output}"
        return res

    # 2) Check unsupported intents
    if any(word in prompt.lower() for word in UNSUPPORTED_INTENTS):
        logging.info(f"Handoff: HumanAgent triggered by unsupported intent ('{prompt}')")
        print("🤖 Bot: 🤝 Handing you over to Human Agent...")
        res = Runner.run_sync(
            starting_agent=HumanAgent,
            input=prompt,
        )
        
        res.final_output = f"🤖 Bot (Human Agent): {res.final_output}"
        return res

    # 3) BotAgent requested escalation itself
    if bot_response.last_agent == "HumanAgent":
        logging.info(f"Handoff: HumanAgent triggered by BotAgent request ('{prompt}')")
        print("🤖 Bot: 🤝 Handing you over to Human Agent...")
        res = Runner.run_sync(
            starting_agent=HumanAgent,
            input=prompt,
        )
        res.final_output = f"🤖 Bot (Human Agent): {res.final_output}"
        return res

    # 4) Return Normal BotAgent response
    return bot_response