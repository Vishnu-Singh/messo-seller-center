from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, OrderItemViewSet, OrderTrackingViewSet
from .soap_services import orders_soap_service, orders_wsdl

# REST API Router
router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'order-items', OrderItemViewSet, basename='order-item')
router.register(r'order-tracking', OrderTrackingViewSet, basename='order-tracking')

urlpatterns = [
    # REST API endpoints
    path('api/', include(router.urls)),
    
    # SOAP endpoints
    path('soap/', orders_soap_service, name='orders-soap'),
    path('soap/wsdl/', orders_wsdl, name='orders-wsdl'),
]
