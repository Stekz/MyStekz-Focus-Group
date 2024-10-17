from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
# from .tools.ask_human import AskHuman

def main_point_str(agent: str):
    return f"{agent}'s main point: [Add the main point of {agent} here]"


@CrewBase
class MystekzFocusGroupCrew():
    """MystekzFocusGroup crew"""

    @agent
    def business_consultant(self) -> Agent:
        return Agent(
            config=self.agents_config['business_consultant'],
            verbose=True,
            # tools=[AskHuman()],
        )

    @agent
    def project_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['project_manager'],
            verbose=True,
            # tools=[AskHuman()],
        )

    @agent
    def facilitator(self) -> Agent:
        return Agent(
            config=self.agents_config['facilitator'],
            verbose=True,
        )

    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer'],
            verbose=True,
            allow_delegation=False,
        )

    # @agent
    # def discussion_moderator(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['discussion_moderator'],
    #         verbose=True,
    #     )

    @task
    def discuss_idea(self) -> Task:
        agents = [
            self.business_consultant(),
            self.project_manager(),
        ]

        return Task(
            config=self.tasks_config['discuss_idea'],
            output_file="output/discussion.md",
            description=f"""
                Discuss the following idea regarding our application MyStekz with all participants: {[a.role for a in agents]}. Make sure you convey the whole idea to each participant and that they focus on the idea itself. They should not give feedback on MyStekz overall or how the idea will be implemented.
                The idea to discuss is: {{idea}}.
            """,
            expected_output="""A discussion in which all participants agree to the outcome.""",
        )


    @task
    def respond_to_idea_business_consultant(self) -> Task:
        return Task(
            config=self.tasks_config['respond_to_idea_business_consultant'],
            output_file="output/business_consultant_response.md",
        )

    @task
    def respond_to_idea_project_manager(self) -> Task:
        return Task(
            config=self.tasks_config['respond_to_idea_project_manager'],
            output_file="output/project_manager_response.md",
        )

    @task
    def summarize(self) -> Task:
        agents = [
            self.business_consultant(),
            self.project_manager(),
        ]
        agent_strs = [main_point_str(a.role) for a in agents]

        # agent_strs = map(lambda agent: main_point_str(agent.role), [
        #     self.business_consultant,
        #     self.project_manager,
        # ])
        return Task(
            config=self.tasks_config['summarize'],
            expected_output=f"""
                List the output for each agent like so:
                {"\n".join(agent_strs)}

                Then list the key points of agreement.
                Then list the key points of disagreement.
            """,
            output_file="output/summary.md",
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[
                self.business_consultant(),
                self.project_manager(),
                # self.summarizer(),
            ],
            # tasks=[
            #     self.respond_to_idea_business_consultant(),
            #     self.respond_to_idea_project_manager(),
            # ],
            tasks=[
                self.discuss_idea(),
                # self.summarize(),
            ],
            # tools=[ask_human],
            manager_agent=self.facilitator(),
            process=Process.hierarchical,
            verbose=True,
            share_crew=False,
            memory=True,
            planning=True,
        )
