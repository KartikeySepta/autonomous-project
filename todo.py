#!/usr/bin/env python3
import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path


DATA_FILE = Path.home() / ".todos.json"


class TaskManager:
    def __init__(self, path=None):
        self.path = path or DATA_FILE
        self.tasks = self._load()

    def _load(self):
        if not self.path.exists():
            return []
        with open(self.path) as f:
            return json.load(f)

    def _save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.path, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def _next_id(self):
        if not self.tasks:
            return 1
        return max(t["id"] for t in self.tasks) + 1

    def add(self, description):
        task = {
            "id": self._next_id(),
            "description": description,
            "done": False,
            "created_at": datetime.now().isoformat(),
        }
        self.tasks.append(task)
        self._save()
        return task

    def list(self, done=None):
        if done is None:
            return list(self.tasks)
        return [t for t in self.tasks if t["done"] == done]

    def done(self, task_id):
        for t in self.tasks:
            if t["id"] == task_id:
                t["done"] = True
                self._save()
                return t
        return None

    def clear(self):
        self.tasks = [t for t in self.tasks if not t["done"]]
        self._save()


def format_task(task):
    status = "[x]" if task["done"] else "[ ]"
    return f"{task['id']:>3} {status} {task['description']}"


def main():
    parser = argparse.ArgumentParser(prog="todo", description="Simple CLI task manager")
    sub = parser.add_subparsers(dest="command")

    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("description", nargs="+")

    sub.add_parser("list", help="List all tasks")

    p_done = sub.add_parser("done", help="Mark a task as done")
    p_done.add_argument("id", type=int)

    sub.add_parser("clear", help="Remove all done tasks")

    args = parser.parse_args()
    mgr = TaskManager()

    if args.command == "add":
        desc = " ".join(args.description)
        task = mgr.add(desc)
        print(f"Added task {task['id']}: {task['description']}")

    elif args.command == "list":
        tasks = mgr.list()
        if not tasks:
            print("No tasks.")
            return
        for t in tasks:
            print(format_task(t))

    elif args.command == "done":
        task = mgr.done(args.id)
        if task is None:
            print(f"No task with id {args.id}")
            sys.exit(1)
        print(f"Done task {task['id']}: {task['description']}")

    elif args.command == "clear":
        mgr.clear()
        print("Cleared done tasks.")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
