#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """return number of subscribers for subreddit
    """
    user_agent = 'MyAPI/0.0.1 (by /u/karim-moharm)'
    headers = {
        'User-Agent': user_agent,
    }
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    nums_of_subs = response.json().get('data').get('subscribers')
    return nums_of_subs
