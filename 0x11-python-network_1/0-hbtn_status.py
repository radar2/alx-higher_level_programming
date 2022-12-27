#!/usr/bin/python3
""" Fetch ALX intranet Status"""
import urllib.request


def fetch_status():
    """Fetches status"""
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}\n".format(html.decode("utf-8")))


if __name__ == "__main__":
    fetch_status()