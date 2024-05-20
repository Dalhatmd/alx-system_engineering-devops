#!/usr/bin/python3
""" Module that gathers data from an API """
import csv
import requests
import sys


def gather_data():
    """ Retrieves data from an API """
    user_id = sys.argv[1]
    employee_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    employee = requests.get(employee_url).json()
    todos = requests.get(todo_url).json()

    emp_name = employee.get("name")
    completed_tasks = [todo for todo in todos if todo.get('completed')]

    with open('{}.csv'.format(user_id), 'w') as file:
        for task in todos:
            file.write('"{}","{}","{}","{}"\n'
                       .format(user_id, emp_name, task.get('completed'),
                               task.get('title')))


if __name__ == '__main__':
    gather_data()
