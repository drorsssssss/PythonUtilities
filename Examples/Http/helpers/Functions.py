import requests


def get_request(url,symbol,timeout=999):
    return requests.get(url+symbol,timeout=timeout).json()


