#!/usr/bin/python3
""" returns a list of articles of a given subreddit """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ recursively gets all hot articles in subreddit """
    if not isinstance(subreddit, str) or subreddit is None:
        return None
    user = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=user, params=params)
        if response.status_code == 404:
            return None

        if response.status_code == 200:
            data = response.json().get('data', {})
            after = data.get('after', None)
            children = data.get('children', [])

            for child in children:
                hot_list.append(child['data']['title'])

            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException as e:
        return None
