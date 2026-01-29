from controllers.task_management_controller import TaskManager
from repository.task_repository import TaskRepository
from views.view import TaskView
from database import DB_CONFIG

if __name__ == "__main__":
    repo = TaskRepository(DB_CONFIG)
    manager = TaskManager(repo)
    TaskView(manager).run()