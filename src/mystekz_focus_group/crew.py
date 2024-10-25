from crewai import Crew, Process, Task

from .agents import facilitator, project_manager, business_analyst

def main_point_str(agent: str):
    return f"{agent}'s main point: [Add the main point of {agent} here]"

def discuss_idea() -> Task:
    agents = [
        business_analyst,
        project_manager,
    ]
    agent_strs = [main_point_str(a.role) for a in agents]

    return Task(
        output_file="../../output/discussion.md",
        description=f"""
            Discuss the following idea regarding our application MyStekz with all participants: {[a.role for a in agents]}. Make sure you convey the whole idea to each participant and that they focus on the idea itself. They should not give feedback on MyStekz overall or how the idea will be implemented.
            The idea to discuss is: {{idea}}.
        """,
        expected_output=f"""
            List the output for each agent like so:
            {"\n".join(agent_strs)}

            Then show the discussion in which all participants agree to the outcome.
        """,
    )

focus_group_crew = Crew(
    agents=[
        business_analyst,
        project_manager,
    ],
    tasks=[
        discuss_idea(),
    ],
    manager_agent=facilitator,
    process=Process.hierarchical,
    verbose=True,
    share_crew=False,
    memory=True,
    planning=True,
)
