from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, DiscountViewSet, VoucherViewSet, ProductPromotionViewSet
from .soap_services import promotions_soap_service, promotions_wsdl

# REST API Router
router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet, basename='campaign')
router.register(r'discounts', DiscountViewSet, basename='discount')
router.register(r'vouchers', VoucherViewSet, basename='voucher')
router.register(r'product-promotions', ProductPromotionViewSet, basename='product-promotion')

urlpatterns = [
    # REST API endpoints
    path('api/', include(router.urls)),
    
    # SOAP endpoints
    path('soap/', promotions_soap_service, name='promotions-soap'),
    path('soap/wsdl/', promotions_wsdl, name='promotions-wsdl'),
]
