from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from mystekz_focus_group.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class MystekzFocusGroupCrew():
    """MystekzFocusGroup crew"""

    @agent
    def business_consultant(self) -> Agent:
        return Agent(
            config=self.agents_config['business_consultant'],
            # tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
            verbose=True
        )

    @agent
    def project_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['project_manager'],
            verbose=True
        )

    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer'],
            verbose=True
        )

    @task
    def respond_to_idea_business_consultant(self) -> Task:
        return Task(
            config=self.tasks_config['respond_to_idea_business_consultant'],
            output_file="business_consultant_response.md",
        )

    @task
    def respond_to_idea_project_manager(self) -> Task:
        return Task(
            config=self.tasks_config['respond_to_idea_project_manager'],
            input_file="business_consultant_response.md",
            output_file="project_manager_response.md",
        )

    @task
    def summarize(self) -> Task:
        return Task(
            config=self.tasks_config['summarize'],
            output_file="summary.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MystekzFocusGroup crew."""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=[
                self.respond_to_idea_business_consultant(),
                self.respond_to_idea_project_manager(),
                self.summarize()
            ],
            process=Process.sequential,
            verbose=True,
        )
