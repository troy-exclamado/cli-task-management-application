import argparse


class TaskView:
    def __init__(self, manager):
        self.manager = manager
        self.parser = argparse.ArgumentParser(description="Task Manager")
        self._setup()

    def _setup(self):
        sub = self.parser.add_subparsers(dest="command")

        add = sub.add_parser("add")
        add.add_argument("--title", required=True)
        add.add_argument("--description", default="")
        add.add_argument("--due-date")
        add.add_argument("--priority", choices=["Low", "Medium", "High"], default="Medium")

        list_cmd = sub.add_parser("list")
        list_cmd.add_argument("--status")
        list_cmd.add_argument("--priority")
        list_cmd.add_argument("--due-date")

        update = sub.add_parser("update")
        update.add_argument("id", type=int)
        update.add_argument("--title")
        update.add_argument("--description")
        update.add_argument("--due-date")
        update.add_argument("--priority")
        update.add_argument("--status")

        complete = sub.add_parser("complete")
        complete.add_argument("id", type=int)

        delete = sub.add_parser("delete")
        delete.add_argument("id", type=int)

    def run(self):
        args = vars(self.parser.parse_args())
        command = args.pop("command")

        if command == "add":
            task = self.manager.add_task(**args)
            print(f"Task added (ID: {task.id})")

        elif command == "list":
            tasks = self.manager.list_tasks(**{k: v for k, v in args.items() if v})
            for t in tasks:
                print(f"""
                    ID: {t.id}
                    Title: {t.title}
                    Description: {t.description}
                    Due Date: {t.due_date}
                    Priority: {t.priority}
                    Status: {t.status}
                    Created At: {t.created_at}
                    -------------------------
                    """)

        elif command == "update":
            task_id = args.pop("id")
            self.manager.update_task(task_id, **{k: v for k, v in args.items() if v})
            print("Task updated")

        elif command == "complete":
            self.manager.complete_task(args["id"])
            print("Task completed")

        elif command == "delete":
            self.manager.delete_task(args["id"])
            print("Task deleted")

        else:
            self.parser.print_help()
