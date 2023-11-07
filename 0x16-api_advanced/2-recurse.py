#!/usr/bin/python3
"""module for making get request for reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """queries the Reddit API and prints the titles of
    all hot articles for a given subreddit.
    """
    user_agent = 'MyAPI/0.0.1 (by /u/Karim Moharm)'
    headers = {
        'User-Agent': user_agent
    }
    # using after parameter to handle pagination
    params = {'after': after}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    resp = requests.get(url, headers=headers, params=params)
    # print(resp.status_code)
    if resp.status_code == 200:
        data = resp.json().get('data')
        lst_of_data = data.get('children')
        after = data.get('after')
        # print(after)

        for i in lst_of_data:
            hot_list.append(i.get('data').get('title'))

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return 'None'
