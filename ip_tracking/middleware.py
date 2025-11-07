import requests
from django.http import HttpResponseForbidden
from django.core.cache import cache
from .models import RequestLog, BlockedIP


class IPTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def get_geolocation(self, ip):
        # Check cache first (24 hours = 86400 seconds)
        cache_key = f'geo_{ip}'
        cached_data = cache.get(cache_key)
        if cached_data:
            return cached_data

        # Skip geolocation for local/private IPs
        if ip in ['127.0.0.1', 'localhost'] or ip.startswith('192.168.') or ip.startswith('10.') or ip.startswith('172.'):
            return {'country': 'Local', 'city': 'Local'}

        try:
            response = requests.get(f'http://ip-api.com/json/{ip}', timeout=5)
            if response.status_code == 200:
                data = response.json()
                geo_data = {
                    'country': data.get('country', ''),
                    'city': data.get('city', '')
                }
                # Cache for 24 hours
                cache.set(cache_key, geo_data, 86400)
                return geo_data
        except:
            pass
        
        return {'country': '', 'city': ''}

    def __call__(self, request):
        # Get client IP address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')

        # Check if IP is blocked
        if BlockedIP.objects.filter(ip_address=ip).exists():
            return HttpResponseForbidden()

        # Get geolocation data
        geo_data = self.get_geolocation(ip)

        # Log the request with geolocation
        RequestLog.objects.create(
            ip_address=ip,
            path=request.path,
            country=geo_data['country'],
            city=geo_data['city']
        )

        response = self.get_response(request)
        return response