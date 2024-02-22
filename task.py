from datetime import datetime


class Task:
    def __init__(self, task_description, due_date=None):
        self.task_description = task_description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d") if due_date else None
        self.completed = False

    def mark_as_complete(self):
        self.completed = True

    def mark_as_imcomplete(self):
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Imcomplete"
        due_date_str = self.due_date.strftime("%Y-%m-%d") if self.due_date else "None"
        return (
            f"Task: {self.task_description}\nDue Date: {due_date_str}\nStatus: {status}"
        )
