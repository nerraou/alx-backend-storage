#!/usr/bin/env python3
"""
obtain the HTML content of a particular URL and return it
"""
import requests

import redis
from functools import wraps
from typing import Callable

redis_client = redis.Redis()


def track_url_access(method: Callable) -> Callable:
    """
    count how many times the url was accessed
    """
    @wraps(method)
    def wrapper(url: str):
        """
        Wrapper function.
        """
        count_key = "count:{}".format(url)
        content_key = "content:{}".format(url)

        redis_client.incr(count_key)

        cached_result = redis_client.get(content_key)
        if cached_result:
            return cached_result.decode("utf-8")

        html = method(url)
        redis_client.setex(content_key, 10, html)

        return html

    return wrapper


@track_url_access
def get_page(url: str) -> str:
    """
    obtain the HTML content of a particular URL and return it
    """
    return requests.get(url).text
