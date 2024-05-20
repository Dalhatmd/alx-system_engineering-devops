#!/usr/bin/python3
""" module that gets all users from an API """
import json
import requests


def list_dict():
    """ records all tasks from all employees """
    employee_url = "https://jsonplaceholder.typicode.com/users"
    employee = requests.get(employee_url).json()

    dict = {}
    for emp in employee:
        user_id = emp.get("id")
        emp_name = emp.get("username")
        t_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        todos = requests.get(t_url).json()

        dict[user_id] = [{"username": emp_name, "task": todo["title"],
                          "completed": todo["completed"], } for todo in todos]

        with open('todo_all_employees.json', 'w') as f:
            json.dump(dict, f)


if __name__ == '__main__':
    list_dict()
