#!/usr/bin/python3
""" Module that gathers data from an API """
import requests
import sys


def gather_data():
    """ Retrieves data from an API """
    user_id = sys.argv[1]
    employee_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    employee = requests.get(employee_url).json()
    todos = requests.get(todo_url).json()

    employee_name = employee.get("name")
    completed_tasks = [todo for todo in todos if todo.get('completed')]

    total = len(todos)
    completed = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({completed}/{total}):")
    for task in completed_tasks:
        print(f'\t {task["title"]}')


if __name__ == '__main__':
    gather_data()
