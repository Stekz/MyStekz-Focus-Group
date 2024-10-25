#!/usr/bin/env python
import os
import chainlit
import chainlit.cli
import chainlit.config
from crewai.crew import CrewOutput
from mystekz_focus_group.crew import focus_group_crew

@chainlit.set_starters
async def set_starters(_: chainlit.User | None):
    return [
        chainlit.Starter(
            label="Present the 'Stages' idea.",
            message="""
                A business consultant normally maps the current state of the business. After that, the next step is ofthen identifying areas of improvement. In our current application you can only model the business once and update that model. However, we're thinking about adding a concept called 'stages' so you can model different versions of the businenss in parallel to each other. That way you can more easily model an improved or digitized version of the business.
            """,
        ),
        chainlit.Starter(
            label="How should stages be defined?",
            message="""
                In MyStekz, we will add the modeling of several stages of the business. Users can add stages themselves and give them a name like Current or MVP. In MyStekz you model your business using Domains, Products and Processes in this hierarchy. Should each stage include everything? Or should they be modeled completely separate? Or should they use a subset of the main stage defined?
            """
        ),
    ]

@chainlit.on_message
async def on_message(message: chainlit.Message):
    try:
        crew_output = await focus_group(inputs={
            "idea": message.content,
        })

        # Send the message and wait for it to complete
        await chainlit.Message(
            content=crew_output.raw,
        ).send()

        # Log additional information
        print("===========================")
        print("Message sent successfully")
        print("Tasks output:")
        print(crew_output.tasks_output)
        print("===========================")
        print(f"Token Usage: {crew_output.token_usage}")
    except Exception as e:
        print(f"Error in on_message: {str(e)}")
        # Send an error message to the user
        await chainlit.Message(
            content=f"An error occurred: {str(e)}",
        ).send()

@chainlit.step(name="MyStekz focus group", type="tool")
async def focus_group(inputs: dict) -> CrewOutput:
    """Runs the focus group with given inputs."""
    return await focus_group_crew.kickoff_async(inputs)


file_ = os.path.realpath(__file__)

def chat():
    """Run the Chainlit app."""
    chainlit.cli.run_chainlit(file_)

def chat_watch():
    """Run the Chainlit app with watch enabled."""
    chainlit.config.config.run.watch = True
    chainlit.cli.run_chainlit(file_)
