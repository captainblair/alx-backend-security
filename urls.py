from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from ip_tracking.views import login_view, RequestLogViewSet, BlockedIPViewSet, SuspiciousIPViewSet, api_status

schema_view = get_schema_view(
   openapi.Info(
      title="ALX Backend Security API",
      default_version='v1',
      description="IP Tracking and Security API",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'request-logs', RequestLogViewSet)
router.register(r'blocked-ips', BlockedIPViewSet)
router.register(r'suspicious-ips', SuspiciousIPViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('api/', include(router.urls)),
    path('api/status/', api_status, name='api_status'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]