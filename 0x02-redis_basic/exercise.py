#!/usr/bin/env python3
"""
writing a string to redis
"""
import redis
from typing import List, Union
import uuid


class Cache:
    """
    a class that implements writing a string to redis
    """
    def __init__(self):
        """
        instantiate a Cache object
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]) -> str:
        """
        method that create writes a string to redis
        """
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key

