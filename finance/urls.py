from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, InvoiceViewSet, SettlementViewSet
from .soap_services import finance_soap_service, finance_wsdl

# REST API Router
router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'invoices', InvoiceViewSet, basename='invoice')
router.register(r'settlements', SettlementViewSet, basename='settlement')

urlpatterns = [
    # REST API endpoints
    path('api/', include(router.urls)),
    
    # SOAP endpoints
    path('soap/', finance_soap_service, name='finance-soap'),
    path('soap/wsdl/', finance_wsdl, name='finance-wsdl'),
]
