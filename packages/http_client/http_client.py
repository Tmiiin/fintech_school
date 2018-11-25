# -*- coding: utf-8 -*-
"""Module with class to work with HTTP client"""
import requests
import json


class HttpClient(object):
    """Class to work with HTTP requests."""

    def __init__(self):
        self.base_url = "https://fintech-trading-qa.tinkoff.ru/v1/md/"
        self.headers = {'Authorization': 'Basic ZmludGVjaDoxcTJ3M2Uh'}

    def get_instruments(self, request_id, system_code):
        """Function allows to get instruments"""
        url = self.base_url + "exchanges/moex/instruments?request_id=" + request_id + "&system_code=" + system_code

        response = requests.get(url, headers=self.headers)

        return response

    def post_sub(self, request_id, system_code, instrument_id, sec_name, sec_type, price_alert, siebel_id):
        """Function allows to post subscription"""

        url = self.base_url + "contacts/" + siebel_id +"/subscriptions?request_id=" + request_id + "&system_code=" + system_code

        data = {json.dumps({"instrument_id": instrument_id, "sec_name": sec_name, "sec_type": sec_type, "price_alert": price_alert})}

        return requests.post(url, json=data, headers=self.headers)
