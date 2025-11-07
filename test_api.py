#!/usr/bin/env python
import os
import django
import requests

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

def test_api_endpoints():
    """Test API endpoints"""
    base_url = 'http://127.0.0.1:8000'
    
    endpoints = [
        '/api/status/',
        '/api/request-logs/',
        '/api/blocked-ips/',
        '/api/suspicious-ips/',
        '/swagger/',
    ]
    
    print("Testing API endpoints...")
    for endpoint in endpoints:
        try:
            response = requests.get(f"{base_url}{endpoint}", timeout=5)
            print(f"{endpoint}: Status {response.status_code}")
        except requests.exceptions.RequestException:
            print(f"{endpoint}: Server not running")

if __name__ == '__main__':
    test_api_endpoints()