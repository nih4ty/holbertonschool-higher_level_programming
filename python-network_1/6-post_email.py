#!/usr/bin/python3
"""Sends a POST request with an email and prints the response body."""

import sys
import requests


def send_post():
    """Sends POST request with email parameter and prints server response."""
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}

    response = requests.post(url, data=data)

    print(response.text)


if __name__ == "__main__":
    send_post()
