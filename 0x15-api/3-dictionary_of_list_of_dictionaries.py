#!/usr/bin/python3
"""export data in the JSON format
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    users_resp = requests.get(
        'https://jsonplaceholder.typicode.com/users')

    todos_resp = requests.get(
        'https://jsonplaceholder.typicode.com/todos')
    todos_data = todos_resp.json()
    # print(todos_data)

    user_data_dict = {}
    output_dict = {}

    for user in users_resp.json():
        user_data_lst = []
        for item in todos_data:
            if user.get('id') == item.get('userId'):
                user_data_dict = {"username": user.get('username'),
                                  "task": item.get('title'),
                                  "completed": item.get('completed')}
                user_data_lst.append(user_data_dict)
        output_dict[user.get('id')] = user_data_lst
        # output_dict = {"{}".format(user.get('id')): user_data_lst}

    with open("todo_all_employees.json", mode='w',
              encoding='utf-8') as fp:
        json.dump(output_dict, fp, indent=2)
