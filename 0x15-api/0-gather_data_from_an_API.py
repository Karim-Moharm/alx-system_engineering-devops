#!/usr/bin/python3
"""script that using REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == '__main__':
    resp = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(argv[1]))
    user_name = resp.json().get('name')

    todos_resp = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                              format(argv[1]))
    todos_data = todos_resp.json()

    done_tasks = 0
    total_tasks = 0
    for task in todos_data:
        total_tasks += 1
        if task.get('completed'):
            done_tasks += 1

    print('Employee {} is done with tasks({}/{}):'.
          format(user_name,
                 done_tasks,
                 total_tasks
                 ))
    for task in todos_data:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))
