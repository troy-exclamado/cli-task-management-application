class TaskManager:
    def __init__(self, repository):
        self.repo = repository

    def add_task(self, **kwargs):
        return self.repo.add_task(**kwargs)

    def list_tasks(self, **filters):
        return self.repo.list(filters)

    def update_task(self, task_id, **updates):
        self.repo.update(task_id, updates)

    def complete_task(self, task_id):
        self.repo.update(task_id, {"status": "Completed"})

    def delete_task(self, task_id):
        self.repo.delete(task_id)
