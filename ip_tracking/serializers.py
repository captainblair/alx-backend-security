from rest_framework import serializers
from .models import RequestLog, BlockedIP, SuspiciousIP


class RequestLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestLog
        fields = '__all__'


class BlockedIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockedIP
        fields = '__all__'


class SuspiciousIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuspiciousIP
        fields = '__all__'