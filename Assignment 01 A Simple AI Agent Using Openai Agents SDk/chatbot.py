import chainlit as cl
from agents import Runner
from my_agents.agent import agent


@cl.on_message
async def main(message: cl.Message):
    prompt = message.content
    print("Thinking: " + prompt)
    
    result = Runner.run_sync(agent,input=prompt)
      
    await cl.Message(
        content=result.final_output
    ).send()