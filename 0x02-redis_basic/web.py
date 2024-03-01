"""
obtain the HTML content of a particular URL and return it
"""
import requests

import redis
from functools import wraps
from typing import Callable
from uuid import uuid4

redis_client = redis.Redis()


def track_url_access(method: Callable) -> Callable:
    """
    count how many times the url was accessed
    """
    @wraps(method)
    def wrapper(*args):
        """
        Wrapper function.
        """
        url = args[0]

        key = "count:{}".format(url)
        redis_client.incr(key)

        cached_result = redis_client.get("cached:{}".format(url))
        if cached_result:
            return cached_result.decode("utf-8")

        html = method(url)
        redis_client.setex("cached:{}".format(url), 10, html)

        return html

    return wrapper


@track_url_access
def get_page(url: str) -> str:
    """
    obtain the HTML content of a particular URL and return it
    """
    return requests.get(url).text
