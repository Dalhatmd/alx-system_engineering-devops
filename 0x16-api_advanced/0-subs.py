#!/usr/bin/python3
""" module that gets number of subscribers in a subreddit"""
import requests
import json


def number_of_subscribers(subreddit):
    """ returns the number of subscribers in subreddit """

    if type(subreddit) != str or subreddit is None:
        return 0
    header = {'User-Agent':  'Google Chrome Version 81.0.4044.129'}

    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = requests.get(url, headers=header, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']

        else:
            return 0
    except requests.exceptions.RequestException as e:
        return 0
