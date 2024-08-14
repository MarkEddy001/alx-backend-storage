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
        print(f"Accessing URL: {url}")
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        if cached_data:
            print(f"Cache hit for {url}")
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        try:
            html = method(url)
            store.incr(count_key)
            store.set(cached_key, html)
            store.expire(cached_key, 10)
            print(f"Cache miss for {url}, caching now")
            return html
        except requests.RequestException as e:
            print(f"Error fetching URL: {e}")
            return ""
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """Returns HTML content of a URL."""
    print(f"Fetching URL: {url}")
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
