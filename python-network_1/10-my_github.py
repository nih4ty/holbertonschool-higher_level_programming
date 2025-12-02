#!/usr/bin/python3
"""Uses GitHub API with Basic Auth to display the user id."""

import sys
import requests


def get_github_id():
    """Fetches GitHub user ID using username and personal access token."""
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    # Basic Auth → (username, token)
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        json_data = response.json()
        print(json_data.get("id"))
    else:
        print("None")


if __name__ == "__main__":
    get_github_id()
