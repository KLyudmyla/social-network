import requests

from bot import config
import logging

logger = logging.getLogger(__name__)


def request(resource: str, method: str, token: str = None, data: str = None):
    headers = {'Content-Type': 'application/json'}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    if method == "POST":
        result = requests.post(f"{config.ROOT_URL}{resource}", data=data, headers=headers)
    elif method == "GET":
        result = requests.get(f"{config.ROOT_URL}{resource}", data=data, headers=headers)
    else:
        logger.error(f'Method {method} is not allowed')
        raise Exception
    return result
