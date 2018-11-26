"""Module with fixtures and hooks for Investment API"""

import pytest
from packages.http_client.http_client import HttpClient


@pytest.fixture(scope= "function")
def http_client():
    """Client to work with HTTP requests"""
    return HttpClient()
