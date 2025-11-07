from django.contrib import admin
from .models import RequestLog, BlockedIP, SuspiciousIP


@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'country', 'city', 'path', 'timestamp')
    list_filter = ('timestamp', 'country')
    readonly_fields = ('ip_address', 'path', 'timestamp', 'country', 'city')
    search_fields = ('ip_address', 'country', 'city')


@admin.register(BlockedIP)
class BlockedIPAdmin(admin.ModelAdmin):
    list_display = ('ip_address',)
    search_fields = ('ip_address',)


@admin.register(SuspiciousIP)
class SuspiciousIPAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'reason', 'timestamp')
    list_filter = ('timestamp', 'reason')
    readonly_fields = ('ip_address', 'reason', 'timestamp')
    search_fields = ('ip_address', 'reason')