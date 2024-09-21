from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text
import os

# Initialize the console
console = Console()

class Task:
	def __init__(self, title):
		self.title = title
		self.completed = False

	def mark_completed(self):
		self.completed = True

	def __str__(self):
		return f"[{'x' if self.completed else ' '}] {self.title}"

# Add a new task to the list
def add_task(task_list, title):
	task = Task(title)
	task_list.append(task)
	console.print(f"[green]Task '{title}' added![/green]")


# List all tasks in a table with rich
def list_tasks(task_list):
	if not task_list:
		consele.print("[yellow]No tasks yet![/yellow]")
	else:
		table = Table(show_header=True, header_style="bold magenta")
		table.add_column("No.", style="dim", width=6)
		table.add_column("Task", style="cyan")
		table.add_column("Status", style="green")

		for idx, task in enumerate(task_list, 1):
			status = "Completed" if task.completed else "Pending"
			table.add_row(str(idx), task.title, status)

		console.print(table)


# Mark a task as completed
def complete_task(task_list, task_index):
	try:
		task_list[task_index - 1].mark_completed()
		console.print(f"[blue]Task {task_index} marked as completed![/blue]")
	except IndexError:
		console.print("[red]Invalid task index![/red]")


# Delete a task
def delete_task(task_list, task_index):
	try:
		task = task_list.pop(task_index - 1)
		console.print(f"[red]Task '{task.title}' deleted![/red]")
	except IndexError:
		console.print("[red]Invalid task index![/red]")


# Save task to a file
def save_tasks(task_list, filename="tasks.txt"):
	with open(filename, 'w') as file:
		for task in task_list:
			file.write(f"{task.title},{task.completed}\n")
	console.print("[green]Tasks saved![/green]")


# Load tasks from a file
def load_tasks(filename="tasks.txt"):
	task_list = []
	if os.path.exists(filename):
		with open(filename, 'r') as file:
			for line in file:
				title, completed = line.strip().split(',')
				task = Task(title)
				if completed == 'True':
					task.mark_completed()
				task_list.append(task)
	return task_list


# Main program loop with colored output using rich
def main():
	task_list = load_tasks()

	while True:
		console.print("\n[bold magenta]=== To-Do App ===[/bold magenta]")
		console.print("[blue]1.[/blue] Add Task")
		console.print("[blue]2.[/blue] List Task")
		console.print("[blue]3.[/blue] Complete Task")
		console.print("[blue]4.[/blue] Delete Task")
		console.print("[blue]5.[/blue] Save and Exit")

		choice = Prompt.ask("[yellow]Choos an option (1-5)[/yellow]")

		if choice == '1':
			title = Prompt.ask("[cyan]Enter task title[/cyan]")
			add_task(task_list, title)
		elif choice == '2':
			list_tasks(task_list)
		elif choice == '3':
			list_tasks(task_list)
			task_index = int(Prompt.ask("[cyan]Enter task number to complete[/cyan]"))
			complete_task(task_list, task_index)
		elif choice == '4':
			list_tasks(task_list)
			task_index = int(Prompt.ask("[cyan]Enter task number to delete[/cyan]"))
			delete_task(task_list, task_index)
		elif choice == '5':
			save_tasks(task_list)
			console.print("[bold green]Goodbye![/bold green]")
			break
		else:
			console.print("[red]Invalid choice. Please try again.[/red]")


if __name__ == "__main__":
	main()
