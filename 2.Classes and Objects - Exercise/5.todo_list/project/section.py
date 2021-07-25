class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        try:
            filter_task = [tsk for tsk in self.tasks if tsk.name == task_name][0]
            filter_task.completed = True
            return f"Completed task {filter_task.name}"
        except IndexError:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        uncompleted_tasks = [t for t in self.tasks if not t.completed]
        difference = len(self.tasks) - len(uncompleted_tasks)
        self.tasks = uncompleted_tasks
        return f"Cleared {difference} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        for t in self.tasks:
            result += f"{t.details()}\n"
        return result
