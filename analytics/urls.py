from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (SalesReportViewSet, ProductAnalyticsViewSet, 
                   CustomerInsightViewSet, PerformanceMetricViewSet)
from .soap_services import analytics_soap_service, analytics_wsdl

# REST API Router
router = DefaultRouter()
router.register(r'sales-reports', SalesReportViewSet, basename='sales-report')
router.register(r'product-analytics', ProductAnalyticsViewSet, basename='product-analytics')
router.register(r'customer-insights', CustomerInsightViewSet, basename='customer-insight')
router.register(r'performance-metrics', PerformanceMetricViewSet, basename='performance-metric')

urlpatterns = [
    # REST API endpoints
    path('api/', include(router.urls)),
    
    # SOAP endpoints
    path('soap/', analytics_soap_service, name='analytics-soap'),
    path('soap/wsdl/', analytics_wsdl, name='analytics-wsdl'),
]
