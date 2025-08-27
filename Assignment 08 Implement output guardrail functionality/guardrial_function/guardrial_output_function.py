from agents import GuardrailFunctionOutput, output_guardrail, RunContextWrapper, Runner, Agent
from my_agent.guardrial_agents import guardrial_agent

@output_guardrail
async def guardrial_output_function(ctx: RunContextWrapper, agent: Agent, output):
    result = await Runner.run(guardrial_agent, input=output, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_avoid_political_topics_and_reference_query
    )