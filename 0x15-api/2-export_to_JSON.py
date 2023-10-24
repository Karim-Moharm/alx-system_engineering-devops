#!/usr/bin/python3
"""export data in the JSON format
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    resp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.
        format(argv[1]))

    user_name = resp.json().get('username')
    # print(user_name)

    todos_resp = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.
        format(argv[1]))
    todos_data = todos_resp.json()
    # print(todos_data)

    """ DISPLAY ON THAT FORMAT
    { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
                    "username": "USERNAME"},
                {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
                    "username": "USERNAME"},
                ... ]}
    """

    user_data_lst = []
    user_data_dict = {}

    for item in todos_data:
        # print(item)
        # print(" ")
        user_data_dict = ({
            "task": item.get('title'),
            "completed": item.get('completed'),
            "username": user_name
        })
        user_data_lst.append(user_data_dict)
    # print(user_data_lst)
    output_dict = {"{}".format(argv[1]): user_data_lst}
    # print(output_dict)

    with open("{}.json".format(argv[1]), mode='w',
              encoding='utf-8') as fp:
        json.dump(output_dict, fp)
