#!/usr/bin/python3
""" Module that gather data from an API """
import requests
import json
import sys


def gather_data():
    """ retrieves data from an API """
    employee_url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId\
            ={sys.argv[1]}"
    employee = requests.get(employee_url).json()
    todos = requests.get(todo_url).json()
    employee_name = employee.get("name")
    completed = sum(1 for todo in todos if todo.get("completed"))
    total = len(todos)
    print(f"Employee {employee_name} is done with tasks({completed}/{total}):")
    for todo in todos:
        if todo.get('completed'):
            print(f'\t{todo["title"]}')
    dict = {"USER_ID": [{"task": todo["title"], "cpmpleted": todo["completed"],
                        "username": employee_name} for todo in todos]}
    with open('USER_ID.json', 'w') as f:
        json.dump(dict, f)


if __name__ == '__main__':
    gather_data()
