import json

import requests


class RequestException(Exception):
    pass


class AwairRequest:
    headers = {
        'Content-Type': 'application/json',
    }

    def __init__(self, auth_token=None):
        if auth_token:
            self.headers['Authorization'] = 'Bearer {}'.format(auth_token)

    def get(self, url, data=None):
        response = self.validate(requests.get(url, params=data, headers=self.headers))
        return response.json()

    def post(self, url, json_data=None):
        response = self.validate(requests.post(url, json=json_data, headers=self.headers))
        return response.json()

    def validate(self, response):
        if response.status_code != 200:
            raise RequestException('Server response with error message: {}'.format(response.text))
        return response
