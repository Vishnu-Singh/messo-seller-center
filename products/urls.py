from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductImageViewSet, InventoryViewSet
from .soap_services import products_soap_service, products_wsdl

# REST API Router
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'product-images', ProductImageViewSet, basename='product-image')
router.register(r'inventory', InventoryViewSet, basename='inventory')

urlpatterns = [
    # REST API endpoints
    path('api/', include(router.urls)),
    
    # SOAP endpoints
    path('soap/', products_soap_service, name='products-soap'),
    path('soap/wsdl/', products_wsdl, name='products-wsdl'),
]
