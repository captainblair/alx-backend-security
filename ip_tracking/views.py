from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django_ratelimit.decorators import ratelimit
import json


def get_rate_for_user(group, request):
    if request.user.is_authenticated:
        return '10/m'  # 10 requests per minute for authenticated users
    return '5/m'  # 5 requests per minute for anonymous users


@csrf_exempt
@require_http_methods(["POST"])
@ratelimit(key='ip', rate=get_rate_for_user, method='POST', block=True)
def login_view(request):
    """Rate-limited login view: 10 req/min for authenticated, 5 req/min for anonymous"""
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return JsonResponse({'error': 'Username and password required'}, status=400)
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({'success': 'Login successful'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)