"""
task09: Task Manager (AI-Assisted Debugged implementation)
Fixed mutable default argument list issue.
"""

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title: str, tags: list = None) -> dict:
        assigned_tags = list(tags) if tags is not None else []
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "tags": assigned_tags
        }
        self.tasks.append(task)
        return task
