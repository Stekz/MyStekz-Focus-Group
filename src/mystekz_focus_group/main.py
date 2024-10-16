#!/usr/bin/env python
import os
import chainlit
import chainlit.cli
import chainlit.config
from crewai.crew import CrewOutput
from mystekz_focus_group.crew import MystekzFocusGroupCrew

@chainlit.set_starters
async def set_starters():
    return [
        chainlit.Starter(
            label="Present the 'Stages' idea.",
            message="""
                A business consultant normally maps the current state of the business. After that, the next step is ofthen identifying areas of improvement. In our current application you can only model the business once and update that model. However, we're thinking about adding a concept called 'stages' so you can model different versions of the businenss in parallel to each other. That way you can more easily model an improved or digitized version of the business.
            """,
        ),
    ]

@chainlit.on_message
async def on_message(message):
    crew_output = await focus_group(inputs={
        "idea": message.content,
    })
    await chainlit.Message(
        content=crew_output.raw,
    ).send()
    print("===========================")
    print("Tasks output:")
    print(crew_output.tasks_output)
    print("===========================")
    print(f"Token Usage: {crew_output.token_usage}")

@chainlit.step(name="MyStekz focus group", type="tool")
async def focus_group(inputs: dict) -> CrewOutput:
    """Runs the focus group with given inputs."""
    return MystekzFocusGroupCrew().crew().kickoff(inputs)


file_ = os.path.realpath(__file__)

def chat():
    """Run the Chainlit app."""
    chainlit.cli.run_chainlit(file_)

def chat_watch():
    """Run the Chainlit app with watch enabled."""
    chainlit.config.config.run.watch = True
    chainlit.cli.run_chainlit(file_)
