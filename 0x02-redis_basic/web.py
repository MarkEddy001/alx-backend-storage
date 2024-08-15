#!/usr/bin/env python3
"""
web cache and tracker
"""
import requests
import redis
from functools import wraps

store = redis.Redis()

def count_url_access(method):
    """Decorator counting how many times a URL is accessed."""
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        
        # If cached data exists, return it
        if cached_data:
            return cached_data.decode("utf-8")

        # Fetch the HTML content if not cached
        html = method(url)

        # Increment the access count
        count_key = "count:" + url
        store.incr(count_key)

        # Cache the HTML content with an expiration time of 10 seconds
        store.set(cached_key, html)
        store.expire(cached_key, 10)

        return html
    return wrapper

@count_url_access
def get_page(url: str) -> str:
    """Returns HTML content of a URL."""
    res = requests.get(url)
    res.raise_for_status()  # Raise an error for bad status codes
    return res.text

# Test the function
if __name__ == "__main__":
    url = "http://www.example.com"
    print("First call:")
    print(get_page(url))  # First call, should take time
    print("Second call:")
    print(get_page(url))  # Second call, should be fast due to caching
