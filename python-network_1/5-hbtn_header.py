#!/usr/bin/python3
"""Sends a request to a URL and prints the X-Request-Id header."""

import sys
import requests


def display_x_request_id():
    """Fetches URL and prints X-Request-Id value from response headers."""
    url = sys.argv[1]

    response = requests.get(url)

    print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    display_x_request_id()
