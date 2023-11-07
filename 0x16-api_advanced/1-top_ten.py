#!/usr/bin/python3
"""module for making get request for reddit API
"""
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
    """
    user_agent = 'MyAPI/0.0.1 (by /u/Karim Moharm)'
    headers = {
        'User-Agent': user_agent
    }
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    resp = requests.get(url, headers=headers)
    lst_of_data = (resp.json().get('data').get('children'))

    all_titles = []
    for i in lst_of_data:
        all_titles.append(i.get('data').get('title'))

    count = 0
    for title in all_titles:
        print(title)
        count += 1
        if count == 10:
            break


# if __name__ == '__main__':
#     top_ten('programming')
