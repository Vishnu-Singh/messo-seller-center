from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShipmentViewSet, ShipmentEventViewSet, WarehouseViewSet
from .soap_services import logistics_soap_service, logistics_wsdl

# REST API Router
router = DefaultRouter()
router.register(r'shipments', ShipmentViewSet, basename='shipment')
router.register(r'shipment-events', ShipmentEventViewSet, basename='shipment-event')
router.register(r'warehouses', WarehouseViewSet, basename='warehouse')

urlpatterns = [
    # REST API endpoints
    path('api/', include(router.urls)),
    
    # SOAP endpoints
    path('soap/', logistics_soap_service, name='logistics-soap'),
    path('soap/wsdl/', logistics_wsdl, name='logistics-wsdl'),
]
