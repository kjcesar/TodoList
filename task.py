from datetime import datetime
from models import TaskModel


class Task:
    def __init__(self, title, due_date=None):
        self.title = title
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d") if due_date else None
        self.completed = False

    def mark_as_complete(self):
        self.completed = True

    def mark_as_imcomplete(self):
        self.completed = False

    def to_model(self):
        return TaskModel(
            title=self.title, due_date=self.due_date, completed=self.completed
        )

    @classmethod
    def from_model(cls, task_model):
        task = cls(title=task_model.title)
        task.completed = task_model.completed
        return task

    def __str__(self):
        status = "Completed" if self.completed else "Imcomplete"
        due_date_str = self.due_date.strftime("%Y-%m-%d") if self.due_date else "None"
        return f"Task: {self.title}\nDue Date: {due_date_str}\nStatus: {status}"
