#!/usr/bin/python3
""" Module that gathers data from an API """
import csv
import json
import requests
import sys


def gather_data():
    """ Retrieves data from an API """
    user_id = sys.argv[1]
    employee_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    employee = requests.get(employee_url).json()
    todos = requests.get(todo_url).json()

    emp_name = employee.get("username")

    dict = {user_id: [{"task": todo["title"], "completed": todo["completed"],
                      "username": emp_name} for todo in todos]}
    with open(f'{user_id}.json', 'w') as f:
        json.dump(dict, f)


if __name__ == '__main__':
    gather_data()
