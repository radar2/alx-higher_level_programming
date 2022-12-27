#!/usr/bin/env python3
""" Fetch ALX intranet Status"""
import urllib.request


def fetch_status():
    """Fetches status"""
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))


if __name__ == "__main__":
    fetch_status()
