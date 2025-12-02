#!/usr/bin/python3
"""Sends a request to a URL and prints the body or the HTTP error code."""

import sys
from urllib import request, error


def fetch_url():
    """Fetches URL and handles HTTPError, printing the response or error code."""
    url = sys.argv[1]

    req = request.Request(url)

    try:
        with request.urlopen(req) as response:
            body = response.read()
            print(body.decode("utf-8"))

    except error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    fetch_url()
