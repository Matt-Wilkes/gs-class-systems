from lib.todo_list import *
class Todo:
    def __init__(self, task):
        self.task = task
        self.complete = False
    def mark_complete(self):
        self.complete = True
        

# task1 = Todo("Do anything")
# task2 = Todo("Do something")
# tasks = [task1, task2]
# for task in tasks:
#     task.complete = True
#     print(task.complete)
    