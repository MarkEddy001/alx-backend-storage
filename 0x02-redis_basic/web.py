#!/usr/bin/env python3
"""
Web cache and tracker
"""
import logging
import requests
import redis
from functools import wraps

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

store = redis.Redis()

def count_url_access(method):
    """ Decorator counting how many times a URL is accessed """
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        if cached_data:
            logger.info("Cache hit for %s", url)
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        try:
            html = method(url)
        except requests.exceptions.RequestException as e:
            logger.error("Error fetching %s: %s", url, e)
            return "<h1>Error fetching content</h1>"

        store.incr(count_key)
        store.set(cached_key, html.encode())
        store.expire(cached_key, 10)
        return html
    return wrapper

@count_url_access
def get_page(url: str) -> str:
    """ Returns HTML content of a URL """
    logger.info("Fetching %s", url)
    res = requests.get(url, timeout=5)
    res.raise_for_status()
    return res.text

def main():
    url = "http://slowwly.robertomurray.co.uk/delay/3000/url/https://www.google.com"
    try:
        print(get_page(url))
    except requests.exceptions.RequestException as e:
        logger.error("Error: %s", e)
        print("Error fetching content")

if __name__ == "__main__":
    main()
