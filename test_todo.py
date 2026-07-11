import json
import tempfile
import unittest
from pathlib import Path

from todo import TaskManager, format_task


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.db = Path(self.tmp) / "todos.json"
        self.mgr = TaskManager(self.db)

    def tearDown(self):
        if self.db.exists():
            self.db.unlink()
        Path(self.tmp).rmdir()

    def test_add_returns_task_with_id_and_description(self):
        task = self.mgr.add("buy milk")
        self.assertEqual(task["description"], "buy milk")
        self.assertEqual(task["id"], 1)
        self.assertFalse(task["done"])

    def test_add_increments_id(self):
        t1 = self.mgr.add("first")
        t2 = self.mgr.add("second")
        self.assertEqual(t1["id"], 1)
        self.assertEqual(t2["id"], 2)

    def test_list_returns_all_tasks(self):
        self.mgr.add("a")
        self.mgr.add("b")
        self.assertEqual(len(self.mgr.list()), 2)

    def test_list_filter_done(self):
        self.mgr.add("a")
        self.mgr.add("b")
        self.mgr.done(1)
        self.assertEqual(len(self.mgr.list(done=True)), 1)
        self.assertEqual(len(self.mgr.list(done=False)), 1)

    def test_done_marks_task(self):
        self.mgr.add("a")
        task = self.mgr.done(1)
        self.assertTrue(task["done"])

    def test_done_nonexistent_returns_none(self):
        result = self.mgr.done(999)
        self.assertIsNone(result)

    def test_clear_removes_done_tasks(self):
        self.mgr.add("a")
        self.mgr.add("b")
        self.mgr.done(1)
        self.mgr.clear()
        self.assertEqual(len(self.mgr.list()), 1)
        self.assertEqual(self.mgr.list()[0]["id"], 2)

    def test_persistence(self):
        self.mgr.add("persist me")
        mgr2 = TaskManager(self.db)
        self.assertEqual(len(mgr2.list()), 1)
        self.assertEqual(mgr2.list()[0]["description"], "persist me")

    def test_format_task_undone(self):
        task = {"id": 1, "description": "test", "done": False, "priority": "medium"}
        self.assertEqual(format_task(task), "  1 [ ]  !  test")

    def test_format_task_done(self):
        task = {"id": 42, "description": "done thing", "done": True, "priority": "medium"}
        self.assertEqual(format_task(task), " 42 [x]  !  done thing")

    def test_add_default_priority(self):
        task = self.mgr.add("default")
        self.assertEqual(task["priority"], "medium")

    def test_add_explicit_priority(self):
        task = self.mgr.add("high prio", priority="high")
        self.assertEqual(task["priority"], "high")

    def test_format_task_shows_priority(self):
        task = {"id": 1, "description": "urgent", "done": False, "priority": "high"}
        self.assertEqual(format_task(task), "  1 [ ] !!! urgent")

    def test_clear_with_no_done_tasks(self):
        self.mgr.add("a")
        self.mgr.add("b")
        self.mgr.clear()
        self.assertEqual(len(self.mgr.list()), 2)


if __name__ == "__main__":
    unittest.main()
