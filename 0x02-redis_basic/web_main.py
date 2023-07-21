#!/usr/bin/python3
"""
Test web.py
"""
get_page = __import__('web').get_page
import redis
import time

url = "http://slowwly.robertomurray.co.uk"
content1 = get_page(url)
print("Content1:", content1)

time.sleep(12)

content2 = get_page(url)
print("Content2:", content2)

time.sleep(5)

content3 = get_page(url)
print("Content3:", content3)

url_count_key = f"count:{url}"
access_count = redis_client.get(url_count_key)
print(f"URL '{url}' was accessed {int(access_count) if access_count else 0} times")



