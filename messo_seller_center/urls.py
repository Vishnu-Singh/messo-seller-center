"""
URL configuration for messo_seller_center project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def api_root(request):
    """Root API endpoint with documentation"""
    return JsonResponse({
        "message": "Welcome to Messo Seller Center API",
        "version": "1.0",
        "documentation": {
            "products": {
                "rest_api": "/products/api/",
                "soap_api": "/products/soap/",
                "endpoints": ["products", "product-images", "inventory"]
            },
            "orders": {
                "rest_api": "/orders/api/",
                "soap_api": "/orders/soap/",
                "endpoints": ["orders", "order-items", "order-tracking"]
            },
            "logistics": {
                "rest_api": "/logistics/api/",
                "soap_api": "/logistics/soap/",
                "endpoints": ["shipments", "shipment-events", "warehouses"]
            },
            "finance": {
                "rest_api": "/finance/api/",
                "soap_api": "/finance/soap/",
                "endpoints": ["payments", "invoices", "settlements"]
            },
            "promotions": {
                "rest_api": "/promotions/api/",
                "soap_api": "/promotions/soap/",
                "endpoints": ["campaigns", "discounts", "vouchers", "product-promotions"]
            },
            "analytics": {
                "rest_api": "/analytics/api/",
                "soap_api": "/analytics/soap/",
                "endpoints": ["sales-reports", "product-analytics", "customer-insights", "performance-metrics"]
            }
        }
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'),
    
    # Documentation
    path('docs/', include('documentation.urls')),
    
    # App-specific URLs (REST and SOAP)
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('logistics/', include('logistics.urls')),
    path('finance/', include('finance.urls')),
    path('promotions/', include('promotions.urls')),
    path('analytics/', include('analytics.urls')),
]
