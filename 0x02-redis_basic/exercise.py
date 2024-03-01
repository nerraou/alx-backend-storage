#!/usr/bin/env python3
""" Redis with python
"""
import redis
from functools import wraps
from typing import Union, Callable, Optional, Any
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """
    function that increments the count for
    that key every time the method is called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function.
        """
        key = method.__qualname__
        self._redis.incr(key)

        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    function that store method inputs and output using
    RPUSH command
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function.
        """
        value = method(self, *args, **kwargs)

        inputs_key = "{}:inputs".format(method.__qualname__)
        outputs_key = "{}:outputs".format(method.__qualname__)
        self._redis.rpush(inputs_key, str(args))
        self._redis.rpush(outputs_key, str(value))

        return value

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
    @call_history
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


def replay(fn: Callable):
    """
    replay fn calls history
    """
    fn_name = fn.__qualname__
    inputs_key = "{}:inputs".format(fn_name)
    outputs_key = "{}:outputs".format(fn_name)
    redis_client = redis.Redis()

    inputs = redis_client.lrange(inputs_key, 0, -1)
    outputs = redis_client.lrange(outputs_key, 0, -1)
    for input, output in zip(inputs, outputs):
        decoded_input = input.decode("utf-8")
        print("{}(*{}) -> {}".format(fn_name, decoded_input, output))
