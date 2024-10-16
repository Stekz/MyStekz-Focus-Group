#!/usr/bin/env python
import sys
from mystekz_focus_group.crew import MystekzFocusGroupCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'idea': 'For project management we have the following issue. When the business consultant finishes their work, it is a complete and detailed business process. For an IT project, we may choose to selectively implement parts of a process first. As currently you can only access the business model as is, it is hard to translate this. I have thought of the following feature to resolve this. We should incorporate a new concept called "stages". This would mean that you can create a variation of the business model in several stages. These stages are named by the user, e.g. "MVP" or "Phase 1".'
    }
    MystekzFocusGroupCrew().crew().kickoff(inputs=inputs)


# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "idea": "AI LLMs"
#     }
#     try:
#         MystekzFocusGroupCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
#
#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MystekzFocusGroupCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         MystekzFocusGroupCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)
#
#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")
