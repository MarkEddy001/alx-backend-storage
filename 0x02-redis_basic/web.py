#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import redis
import requests
from functools import wraps
from typing import Callable


# Initialize the Redis client
redis_store = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    '''Caches the output of fetched data and tracks the access count.
    '''
    @wraps(method)
    def invoker(url: str) -> str:
        '''The wrapper function for caching the output and tracking the count.
        '''
        # Increment the count for the URL
        redis_store.incr(f'count:{url}')
        
        # Check if the result is already cached
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        
        # Fetch the result and cache it with an expiration time of 10 seconds
        result = method(url)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''Returns the content of a URL after caching the request's response,
    and tracking the request.
    '''
    return requests.get(url).text


# Test the function
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.com"
    print(get_page(url))  # First call, should take time
    print(get_page(url))  # Second call, should be fast due to caching
