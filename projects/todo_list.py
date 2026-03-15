# Simple TODO List Manager
class TodoList:
    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add(self, title):
        task = {"id": self._next_id, "title": title, "done": False}
        self.tasks.append(task)
        self._next_id += 1
        return task

    def complete(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                return True
        return False

    def delete(self, task_id):
        self.tasks = [t for t in self.tasks if t["id"] != task_id]

    def pending(self):
        return [t for t in self.tasks if not t["done"]]

    def display(self):
        for t in self.tasks:
            status = "x" if t["done"] else "o"
            print(f"[{status}] {t['id']}. {t['title']}")

todo = TodoList()
todo.add("Learn Python")
todo.add("Study algorithms")
todo.add("Build a project")
todo.complete(1)
todo.display()
print("Pending:", len(todo.pending()))
