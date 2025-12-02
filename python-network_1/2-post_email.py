#!/usr/bin/python3
"""Sends a POST request to a URL with an email parameter and prints the response."""

import sys
from urllib import request, parse


def send_post_request():
    """Sends POST request with email and prints UTF-8 decoded response."""
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare POST data
    data = parse.urlencode({"email": email}).encode("utf-8")

    req = request.Request(url, data=data)

    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode("utf-8"))


if __name__ == "__main__":
    send_post_request()
