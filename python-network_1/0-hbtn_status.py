#!/usr/bin/python3
"""Fetches the status from intranet.hbtn.io using urllib."""

from urllib import request


def fetch_status():
    """Fetches https://intranet.hbtn.io/status and prints formatted output."""
    url = "https://intranet.hbtn.io/status"

    headers = {
        "cfclearance": "true"
    }

    req = request.Request(url, headers=headers)

    with request.urlopen(req) as response:
        body = response.read()

        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")


if __name__ == "__main__":
    fetch_status()
