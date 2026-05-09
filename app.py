import requests


def get_status_code(url: str) -> int:
    """Return the HTTP status code for a given URL."""
    response = requests.get(url, timeout=5)
    return response.status_code


def is_successful_status(status_code: int) -> bool:
    """Return True if the status code is in the 2xx success range."""
    return 200 <= status_code < 300
