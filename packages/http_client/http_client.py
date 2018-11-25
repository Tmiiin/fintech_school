"""Module with class to work with HTTP client"""

import requests


class HttpClient(object):
    """Class to work with HTTP requests."""

    def __init__(self):
        self.base_url = "https://fintech-trading-qa.tinkoff.ru/v1/md/"
        self.headers = {'Authorization': 'Basic ZmludGVjaDoxcTJ3M2Uh'}

    def get_instruments(self):

        url = self.base_url + 'exchanges/moex/instruments?request_id=1&system_code=2'

        response = requests.get(url, headers=self.headers)

        return response
