#!/usr/bin/env python3
"""
web cache and tracker
"""
import requests
import redis
from functools import wraps
from typing import Callable

store = redis.Redis()


def count_url_access(method: Callable[[str], str]) -> Callable[[str], str]:
    """Decorator counting how many times a URL is accessed."""
    @wraps(method)
    def wrapper(url: str) -> str:
        """Wrapper function for caching the output and tracking the count."""
        cached_key = "cached:" + url
        count_key = "count:" + url

        # Check if the URL is already cached
        cached_data = store.get(cached_key)
        if cached_data:
            print(f"Cache hit for {url}")
            return cached_data.decode("utf-8")

        # If not cached, fetch the URL and cache it
        html = method(url)
        store.incr(count_key)
        store.set(cached_key, html)
        store.expire(cached_key, 10)
        print(f"Cache miss for {url}, caching now")
        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """Returns HTML content of a URL."""
    res = requests.get(url)
    res.raise_for_status()  # Raise an error for bad status codes
    return res.text
