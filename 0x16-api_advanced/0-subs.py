#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers
"""
import requests

user_agent = 'MyAPI/0.0.1 (by /u/karim-moharm)'

headers = {
    'User-Agent': user_agent,
}
response = requests.get(
    "https://www.reddit.com/r/programming/about.json", headers=headers)
print(response.json()["data"]["subscribers"])
# print(len(response.json()))

# keys = []
# for key in response.json().values():
#     keys.append(key)

# print(len(keys))
