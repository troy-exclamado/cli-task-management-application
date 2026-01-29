from datetime import datetime

class Task:
    def __init__(
        self,
        title,
        description="",
        due_date=None,
        priority="Medium",
        status="Pending",
        task_id=None,
        created_at=None
    ):
        self.id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.created_at = created_at or datetime.now()