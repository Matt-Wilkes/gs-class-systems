from lib.todo_list import *
from lib.todo import *
import pytest 

'''
Given a task is added
todos should contain the task object
'''
def test_add_task_is_in_todos():
    todo_list = TodoList()
    task1 = Todo("Do anything")
    todo_list.add(task1)
    assert todo_list.todos == [task1]
    
'''
Given multiple tasks are added
todos should contain all the task objects
'''
def test_add_multiple_tasks_to_todos_returns_tasks():
    todo_list = TodoList()
    task1 = Todo("Do anything")
    task2 = Todo("Do something")
    todo_list.add(task1)
    todo_list.add(task2)
    assert todo_list.todos == [task1, task2]
    
'''
Given an empty string
#add should return an error "Task is empty"
And todos list shouldn't be populated
'''
def test_add_empty_string_returns_error():
    todo_list = TodoList()
    task1 = Todo("")
    with pytest.raises(Exception) as err:
        todo_list.add(task1)
    error_message = str(err.value)
    assert error_message == "Task is empty"
    
'''
# Given task is not a string
# init should return an error "Only strings can be added"
# '''
def test_wrong_type_added_to_task():
    todo_list = TodoList()
    task1 = Todo(123)
    with pytest.raises(Exception) as err:
        todo_list.add(task1)
    error_message = str(err.value)
    assert error_message == "Only strings can be added"
    
'''
Given todos contains three incomplete tasks
#incomplete should return the three incomplete tasks
'''
def test_todos_contains_three_incomplete_tasks():
    todo_list = TodoList()
    task1 = Todo("Do anything")
    task2 = Todo("Do something")
    task3 = Todo("Do something else")
    todo_list.add(task1)
    todo_list.add(task2)
    todo_list.add(task3)
    assert todo_list.incomplete() == [task1, task2, task3]
    
'''
Given a task 
#mark_complete should set the #complete property to True
'''
def test_mark_complete_completes_task():
    todo_list = TodoList()
    task1 = Todo("Do anything") #new instance
    todo_list.add(task1)
    task1.mark_complete() 
    assert task1.complete == True
    

'''
Given todos list has two completed tasks
#complete should return the two completed tasks
'''
def test_complete_returns_completed_tasks():
    todo_list = TodoList()
    task1 = Todo("Do anything")
    task2 = Todo("Do something")
    task3 = Todo("Do something else")
    todo_list.add(task1)
    todo_list.add(task2)
    todo_list.add(task3)
    task1.mark_complete()
    task2.mark_complete()
    assert todo_list.complete() == [task1, task2]

    '''
Given tasks contains three incomplete items
#give_up should mark the tasks as complete
#complete should contain all of the tasks
#incomplete should be empty
'''
def test_give_up_sets_all_tasks_to_completed():
    todo_list = TodoList()
    task1 = Todo("Do anything")
    task2 = Todo("Do something")
    task3 = Todo("Do something else")
    todo_list.add(task1)
    todo_list.add(task2)
    todo_list.add(task3)
    todo_list.give_up() 
    assert todo_list.complete() == [task1,task2,task3]
    assert todo_list.incomplete() == []
