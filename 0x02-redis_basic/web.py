"""
obtain the HTML content of a particular URL and return it
"""
import requests

import redis
from functools import wraps
from typing import Callable
from uuid import uuid4


def track_url_access(method: Callable) -> Callable:
    """
    count how many times the url was accessed
    """
    @wraps(method)
    def wrapper(*args):
        """
        Wrapper function.
        """
        key = "count:{}".format(args[0])
        redis_client = redis.Redis()
        redis_client.incr(key)

        return method(*args)

    return wrapper


@track_url_access
def get_page(url: str) -> str:
    """
    obtain the HTML content of a particular URL and return it
    """
    return requests.get(url)
