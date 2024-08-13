#!/usr/bin/python3
""" Prints the top ten hot posts in a given subreddit """
import json
import requests


def top_ten(subreddit):
    """ gets the top ten hot posts of a subreddit """
    header = {"User-agent": "Google Chrome Version 81.0.4044.129"}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 10, 't': 'all'}

    try:
        response = requests.get(url, headers=header, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            posts = response.json()['data']['children']
            for post in posts:
                print(post.get('data').get('title'))

        else:
            print('None')
    except requests.exceptions.RequestException as e:
        print('None')
