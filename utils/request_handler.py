import requests
from utils.logger import get_logger

logger = get_logger()

def send_request(method, url, **kwargs):
    logger.info(f"Sending {method} request to URL: {url} with params {kwargs}")
    response = requests.request(method, url, **kwargs)
    logger.info(f"Received response: {response.status_code} - {response.text}")
    return response