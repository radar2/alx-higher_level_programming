#!/usr/bin/python3
"""
sha + author commits history
"""
import requests
from sys import argv


def list_commit():
    name = argv[2]
    repo = argv[1]
    params = {'per_page': 10}
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(name, repo), params=params)
    r = r.json()
    for arg in r:
        print("{}: {}".format(arg.get('sha'),
                              arg.get('commit').get('author').get('name')))


if __name__ == '__main__':
    list_commit()

