""" Redis with python
"""
import redis
from typing import Union, Callable, Optional, Any
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

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        get a value of the given key
        """
        response = self._redis.get(key)

        if fn is None:
            return response
        if not response:
            return response
        return fn(response)

    def get_int(self, key: str):
        """
        get value of key and convert it to int
        """
        return self.get(key, int)

    def get_str(self, key: str):
        """
        get value of key and convert it to int
        """
        return self.get(key, lambda data: data.decode("utf-8"))
