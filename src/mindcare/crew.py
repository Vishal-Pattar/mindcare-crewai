from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class Mindcare():
	"""Mindcare crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	
	@agent
	def intent_recognition_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['intent_recognition_agent'],
			verbose=True
		)

	@agent
	def compliance_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['compliance_agent'],
			verbose=True
		)
	
	@agent
	def correction_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['correction_agent'],
			verbose=True
		)
	
	@agent
	def memory_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['memory_agent'],
			verbose=True
		)
	
	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	
	@task
	def intent_classification_task(self) -> Task:
		return Task(
			config=self.tasks_config['intent_classification_task'],
		)

	@task
	def compliance_task(self) -> Task:
		return Task(
			config=self.tasks_config['compliance_task'],
			output_file='report.md'
		)
	
	@task
	def correction_task(self) -> Task:
		return Task(
			config=self.tasks_config['correction_task'],
			output_file='report.md'
		)
	
	@task
	def memory_task(self) -> Task:
		return Task(
			config=self.tasks_config['memory_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Mindcare crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
