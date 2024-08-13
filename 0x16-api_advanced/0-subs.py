#!/usr/bin/python3 
""" module that gets number of active users in a subreddit using the reddit API"""
import requests
import json

def number_of_subscribers(subreddit):
    header = {'User-Agent': 'Alx-Student'}

    url = f'https://www.reddit.com/r/{subreddit}/about.json'


    try:
        response = requests.get(url, headers=header, allow_redirects = False)

        if response.status_code == 200:
            data = response.json()
            return data['data'] ['subscribers']

        else:
            return 0
    except requests.exceptions.RequestException as e:
        return 0

