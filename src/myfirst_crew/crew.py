from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class MyFirstCrew():
    """Fitness Crew for Personalized Wellness Plans"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def intake_agent(self) -> Agent:
        return Agent(config=self.agents_config['intake_agent'], verbose=True)

    @agent
    def body_analyzer(self) -> Agent:
        return Agent(config=self.agents_config['body_analyzer'], verbose=True)

    @agent
    def therapist(self) -> Agent:
        return Agent(config=self.agents_config['therapist'], verbose=True)

    @agent
    def personal_trainer(self) -> Agent:
        return Agent(config=self.agents_config['personal_trainer'], verbose=True)

    @agent
    def nutritionist(self) -> Agent:
        return Agent(config=self.agents_config['nutritionist'], verbose=True)

    @agent
    def marketing_expert(self) -> Agent:
        return Agent(config=self.agents_config['marketing_expert'], verbose=True)

    @task
    def intake_task(self) -> Task:
        return Task(config=self.tasks_config['intake_task'])

    @task
    def body_analysis_task(self) -> Task:
        return Task(config=self.tasks_config['body_analysis_task'])

    @task
    def therapist_task(self) -> Task:
        return Task(config=self.tasks_config['therapist_task'])

    @task
    def trainer_task(self) -> Task:
        return Task(config=self.tasks_config['trainer_task'])

    @task
    def nutritionist_task(self) -> Task:
        return Task(config=self.tasks_config['nutritionist_task'])

    @task
    def marketing_task(self) -> Task:
        return Task(
            config=self.tasks_config['marketing_task'],
            output_file='wellness_plan.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the FitnessCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
