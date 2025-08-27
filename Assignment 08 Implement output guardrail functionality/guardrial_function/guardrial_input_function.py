from agents import RunContextWrapper, GuardrailFunctionOutput, input_guardrail, Runner, Agent, TResponseInputItem
from my_agent.guardrial_agents import guardrial_agent


@input_guardrail
async def guardrial_input_fuction(ctx: RunContextWrapper, agent: Agent,
input: str | list[TResponseInputItem])-> GuardrailFunctionOutput:
    response = await Runner.run(guardrial_agent, input=input, context=ctx.context)
    print(agent.name)
    return GuardrailFunctionOutput(
        output_info=response.final_output,
        tripwire_triggered=not response.final_output.is_math_homework_query
    )

    
