"""Module with class to work with HTTP client"""

import requests


class HttpClient(object):
    """Class to work with HTTP requests."""

    def get_instruments(self):

        headers = {'Authorization': 'Basic ZmludGVjaDoxcTJ3M2Uh'}
        url = "https://fintech-trading-qa.tinkoff.ru/v1/md/exchanges/moex/instruments?request_id=1&system_code=2"

        response = requests.get(url, headers=headers)

        return response
