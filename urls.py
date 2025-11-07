from django.contrib import admin
from django.urls import path
from ip_tracking.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
]