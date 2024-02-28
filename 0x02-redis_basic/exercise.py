#!/usr/bin/env python3
""" Redis with python
"""
import redis
from typing import Union
from uuid import uuid4


class Cache:
    """
    This is cash class
    """
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes,  int,  float]) -> str:
        """
        The method should generate a random key
        """
        key = str(uuid4())
        client = self._redis
        client.set(key, data)
        return key
