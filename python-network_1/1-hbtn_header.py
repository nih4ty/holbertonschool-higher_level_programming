#!/usr/bin/python3
"""Takes a URL, sends a request, and prints the X-Request-Id header."""

import sys
from urllib import request


def display_header():
    """Sends request to the given URL and prints the X-Request-Id header."""
    url = sys.argv[1]

    req = request.Request(url)

    with request.urlopen(req) as response:
        headers = response.headers
        print(headers.get("X-Request-Id"))


if __name__ == "__main__":
    display_header()

