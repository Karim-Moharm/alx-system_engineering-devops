#!/usr/bin/python3
"""using REST API for a given employee ID
returns information about his/her TODO list progress.
"""
import requests
import sys


def main(av):
    """main function of script
    """
    user_resp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(av[1]))
    json_resp = user_resp.json()
    employee_name = json_resp.get('name')
    todos_resp = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(av[1])
    )
    done_tasks = 0
    total_tasks = 0
    for item in todos_resp.json():
        total_tasks += 1
        if item.get('completed') is True:
            done_tasks += 1

    print('Employee {} is done with tasks({}/{}):'.format(
        employee_name,
        done_tasks,
        total_tasks
    ))

    for item in todos_resp.json():
        if item.get('completed') is True:
            print('\t {}'.format(item.get('title')))


if __name__ == '__main__':
    main(sys.argv)
