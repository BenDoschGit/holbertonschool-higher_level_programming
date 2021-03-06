#!/usr/bin/python3.4
"""Script that takes in a URL, sends a request to the URL and
displays the body of the response"""
import urllib.request
import urllib.error
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            body = body.decode("UTF-8")
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
