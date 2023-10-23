#!/usr/bin/python3
"""using REST API for a given employee ID
returns information about his/her TODO list progress.
"""
import requests


def main(av):
    user_resp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(av[1]))
    json_resp = user_resp.json()
    employee_name = json_resp["name"]
    todos_resp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'
        .format(av[1])
    )
    done_tasks = 0
    total_tasks = 0
    for item in todos_resp.json():
        total_tasks += 1
        if item["completed"] is True:
            done_tasks += 1

    print('Employee {} is done with tasks({}/{}):'.format(
        employee_name,
        done_tasks,
        total_tasks
    ))


if __name__ == '__main__':
    import sys
    main(sys.argv)
