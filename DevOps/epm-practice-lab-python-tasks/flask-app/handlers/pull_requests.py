import requests
import os

TOKEN = os.getenv("TOKEN")
HEADERS = {'Authorization': f'Bearer {TOKEN}'}


def get_pull_requests(state):
    """
    Example of return:
    [
        {"title": "Add useful stuff", "num": 56, "link": "https://github.com/boto/boto3/pull/56"},
        {"title": "Fix something", "num": 57, "link": "https://github.com/boto/boto3/pull/57"},
    ]
    """

    # Write your code here
    url = "https://api.github.com/repos/boto/boto3/pulls"
    params = {
        'state': state,
        'per_page': 100
    }

    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status() # Raise exception for bad status codes
        pull_requests_data = response.json()
        pull_requests = []

        for pr in pull_requests_data:
            pull_requests.append({
                "title": pr['title'],
                "num": pr['number'],
                "link": pr['html_url']
            })
        return pull_requests
    except requests.exceptions.RequestException as e:
        print(f"Error fetching pull requests: {e}")
        return []
    except KeyError as e:
        print(f"Error parsing response data: {e}")
        return []
