#!/usr/bin/python3
"""export data in the CSV format
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    resp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.
        format(argv[1]))
    user_name = resp.json().get('username')

    todos_resp = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.
        format(argv[1]))
    todos_data = todos_resp.json()

    with open('{}.csv'.format(argv[1]), mode='w',
              encoding='UTF8') as fp:
        csv_data = csv.writer(fp, quoting=csv.QUOTE_ALL)

        for item in todos_data:
            csv_data.writerow([
                argv[1],
                user_name,
                item.get('completed'),
                item.get('title')
            ])
