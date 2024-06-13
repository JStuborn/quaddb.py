# utils.py

import requests

def handle_response(response: requests.Response):
    if response.status_code == 400:
        raise InvalidParameterError(response.json().get('error', 'Invalid parameter'))
    elif response.status_code == 404:
        raise NotFoundError(response.json().get('error', 'Not found'))
    elif response.status_code >= 500:
        raise ServerError(response.json().get('error', 'Server error'))
    response.raise_for_status()
    return response.json()
