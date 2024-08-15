#!/usr/bin/env python3
"""
Implement an expiring web cache and tracker
"""
import redis
import requests
from functools import wraps

r = redis.Redis()

def cache(func):
    """
    Decorator to cache the result of a function call
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        url = args[0]
        # Check if the result is cached
        result = r.get(f"cache:{url}")
        if result:
            return result.decode('utf-8')  # Return cached response
        else:
            # Call the original function to fetch the content
            response = func(*args, **kwargs)
            # Cache the response with an expiration time of 10 seconds
            r.setex(f"cache:{url}", 10, response)
            # Increment the access count for this URL
            r.incr(f"count:{url}")
            return response  # Return the fetched response
    return wrapper

@cache
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a URL
    """
    response = requests.get(url)
    return response.text
