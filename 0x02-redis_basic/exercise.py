""" Redis with python
"""
import redis
from functools import wraps
from typing import Union, Callable, Optional, Any
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    '''
     function that increments the count for
       that key every time the method is called and returns
       the value returned by the original method.
    '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''
            Wrapper function.
        '''
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """
    This is cash class
    """
    def __init__(self) -> None:
        """
        Cache constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
