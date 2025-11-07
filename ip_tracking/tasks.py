from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from .models import RequestLog, SuspiciousIP


@shared_task
def detect_anomalies():
    """Hourly task to detect suspicious IP activity"""
    one_hour_ago = timezone.now() - timedelta(hours=1)
    
    # Flag IPs with >100 requests/hour
    high_volume_ips = RequestLog.objects.filter(
        timestamp__gte=one_hour_ago
    ).values('ip_address').annotate(
        request_count=Count('id')
    ).filter(request_count__gt=100)
    
    for ip_data in high_volume_ips:
        ip = ip_data['ip_address']
        count = ip_data['request_count']
        SuspiciousIP.objects.get_or_create(
            ip_address=ip,
            reason=f'High volume: {count} requests/hour',
            defaults={'timestamp': timezone.now()}
        )
    
    # Flag IPs accessing sensitive paths
    sensitive_paths = ['/admin', '/login']
    for path in sensitive_paths:
        sensitive_ips = RequestLog.objects.filter(
            timestamp__gte=one_hour_ago,
            path__startswith=path
        ).values_list('ip_address', flat=True).distinct()
        
        for ip in sensitive_ips:
            SuspiciousIP.objects.get_or_create(
                ip_address=ip,
                reason=f'Accessed sensitive path: {path}',
                defaults={'timestamp': timezone.now()}
            )
    
    return f"Anomaly detection completed at {timezone.now()}"