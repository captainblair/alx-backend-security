from django.contrib import admin
from .models import RequestLog, BlockedIP


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