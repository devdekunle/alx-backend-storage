#!/usr/bin/env python3
"""
writing a string to redis
"""
import redis
from typing import Union, Callable
import uuid
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """
    function that create a function and returns how many times the function
    Cache methods have been called and also the value
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """
    a class that implements writing a string to redis
    """
    def __init__(self) -> None:
        """
        instantiate a Cache object
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    def store(self, data: Union[str, int, float, bytes]) -> str:
        """
        method that create writes a string to redis
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable=None) -> Union[str, float, int, bytes]:
        """
        takes a key string and a function and converts the data back
        to the desired format"""
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """retrieve a string value from  Redis and returns it
        """
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """takes a key and retrieves the value from the Redis
        database"""
        return self.get(key, lambda x: int(x.decode("utf-8")))
