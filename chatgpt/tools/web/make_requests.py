from retrying import retry
import requests
from loguru import logger


# 添加每次方法执行之间的等待时间
# @retry(stop_max_attempt_number=15, wait_fixed=3000)
def make_requests_with_retry(url, headers=None):
    if headers is None:
        response = requests.get(url, timeout=3)
    else:
        logger.info(url)
        logger.info(headers)
        response = requests.get(url, headers={}, timeout=3)
    return response
