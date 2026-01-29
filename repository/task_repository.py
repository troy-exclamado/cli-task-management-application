import mysql.connector
from datetime import datetime
from models.task import Task


class TaskRepository:
    def __init__(self, config):
        self.config = config

    def _connect(self):
        return mysql.connector.connect(**self.config)

    def add_task(self, **kwargs):
        conn = self._connect()
        cursor = conn.cursor()

        task = Task(
            title=kwargs.get("title"),
            description=kwargs.get("description"),
            due_date=kwargs.get("due_date"),
            priority=kwargs.get("priority"),
            status=kwargs.get("status", "Pending"),
            created_at=kwargs.get("created_at", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )

        cursor.execute("""
            INSERT INTO tasks (title, description, due_date, priority, status, created_at)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            task.title,
            task.description,
            task.due_date,
            task.priority,
            task.status,
            task.created_at
        ))

        conn.commit()
        task.id = cursor.lastrowid
        cursor.close()
        conn.close()
        return task

    def list(self, filters=None):
        filters = filters or {}
        query = "SELECT * FROM tasks WHERE 1=1"
        params = []

        for key, value in filters.items():
            query += f" AND {key} = %s"
            params.append(value)

        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        return [
            Task(
                task_id=row[0],
                title=row[1],
                description=row[2],
                due_date=row[3],
                priority=row[4],
                status=row[5],
                created_at=row[6]
            )
            for row in rows
        ]

    def update(self, task_id, updates: dict):
        fields = ", ".join(f"{k}=%s" for k in updates)
        values = list(updates.values()) + [task_id]

        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE tasks SET {fields} WHERE id=%s",
            values
        )
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self, task_id):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
        conn.commit()
        cursor.close()
        conn.close()
