#!/usr/bin/python3
"""Sends a POST request with a letter and displays the JSON response."""

import sys
import requests


def search_user():
    """Sends POST request with variable q and handles JSON response."""
    url = "http://0.0.0.0:5000/search_user"

    # If no argument → q = ""
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    data = {"q": q}

    try:
        response = requests.post(url, data=data)
        json_data = response.json()  # may raise ValueError if JSON invalid

        if json_data:
            # Expected keys: id, name
            print(f"[{json_data.get('id')}] {json_data.get('name')}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    search_user()

