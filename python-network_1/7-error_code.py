#!/usr/bin/python3
"""Sends a request to a URL and prints body or error code."""

import sys
import requests


def fetch_url():
    """Fetches URL and prints response body or error code."""
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    fetch_url()

