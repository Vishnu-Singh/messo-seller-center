from rest_framework import serializers
from .models import APIEndpoint, APIChangeLog, SetupGuide, FAQ


class APIEndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIEndpoint
        fields = '__all__'


class ChangeLogSerializer(serializers.ModelSerializer):
    endpoint_name = serializers.CharField(source='endpoint.name', read_only=True)
    
    class Meta:
        model = APIChangeLog
        fields = '__all__'


class SetupGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = SetupGuide
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
