# File: lib/todo_list.py
```python
class TodoList:
    def __init__(self):
        pass

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        pass

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        pass

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass

```

# File: lib/todo.py
```python
class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass

```

```python
# We need to add task todo list 
# we need to store the todos in a list within Todo List
# we need to mark task as 'complete' - initially incomplete todos[complete] = False
# return complete tasks
# return incomplete tasks
# mark a task as complete todos[complete] = True
# mark all tasks as complete
# 



'''
Initially TodoList contains no tasks
'''
todo_list = TodoList()
todo_list.todos #= []

'''
Given a task
#task property should be set to task
'''
task1 = Todo("Do anything")
task1.task == "Do anything"

'''
Given a task
#complete property should be set to False
'''
task1 = Todo("Do anything")
task1.complete #== False

'''
Given a task is added
todos should contain the task object
'''
todo_list = TodoList()
task1 = Todo("Do anything")
todo_list.add(task1)
todo_list.todos #== [task1]

'''
Given multiple tasks are added
todos should contain all the task objects
'''
todo_list = TodoList()
task1 = Todo("Do anything")
task2 = Todo("Do something")
todo_list.add(task1)
todo_list.add(task2)
todo_list.todos #== [task1, task2]

'''
Given an empty string
#add should return an error "Task is empty"
And todos list shouldn't be populated
'''
todo_list = TodoList()
task1 = Todo("")
todo_list.add(task1)
error_message #== "Task is empty"

'''
Given the wrong type
#add should return an error "Only strings can be added"
'''
todo_list = TodoList()
task1 = Todo(123)
todo_list.add(task1)
error_message #== "Only strings can be added"

'''
Given todos contains three incomplete tasks
#incomplete should return the three incomplete tasks
'''
todo_list = TodoList()
task1 = Todo("Do anything")
task2 = Todo("Do something")
task3 = Todo("Do something else")
todo_list.add(task1)
todo_list.add(task2)
todo_list.add(task3)
todo_list.incomplete() #== [task1, task2, task3]

'''
Given a task 
#mark_complete should set the #complete property to True
'''
todo_list = TodoList()
task1 = Todo("Do anything")
todo_list.add(task1)
task1.mark_complete() 
todo_list.complete #== [task1]

'''
Given todos contains four tasks
And two are marked complete
#complete should return two tasks
'''
todo_list = TodoList()
task1 = Todo("Do anything")
task2 = Todo("Do something")
task3 = Todo("Do something else")
todo_list.add(task1)
todo_list.add(task2)
todo_list.add(task3)
task1.mark_complete()
task2.mark_complete()
todo_list.complete #== [task1, task2]

'''
Given tasks contains three incomplete items
#give_up should mark the tasks as complete
#complete should contain all of the tasks
#incomplete should be empty
'''
todo_list = TodoList()
task1 = Todo("Do anything")
task2 = Todo("Do something")
task3 = Todo("Do something else")
todo_list.add(task1)
todo_list.add(task2)
todo_list.add(task3)
todo_list.give_up() 
todo_list.complete #== [task1,task2,task3]
todo_list.incomplete #== []


```