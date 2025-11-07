#!/usr/bin/env python
import os
import django
import requests
import time

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

def test_rate_limit():
    """Test rate limiting functionality"""
    url = 'http://127.0.0.1:8000/login/'
    data = {'username': 'test', 'password': 'test'}
    
    print("Testing rate limiting...")
    print("Making 6 requests quickly (should hit 5/min limit for anonymous users)")
    
    for i in range(6):
        try:
            response = requests.post(url, json=data, timeout=2)
            print(f"Request {i+1}: Status {response.status_code}")
            if response.status_code == 429:
                print("Rate limit hit!")
                break
        except requests.exceptions.RequestException as e:
            print(f"Request {i+1}: Connection error (server not running)")
            break
        time.sleep(0.1)

if __name__ == '__main__':
    test_rate_limit()