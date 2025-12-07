from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'documentation'

# REST API Router
router = DefaultRouter()
router.register(r'endpoints', views.APIEndpointViewSet, basename='api-endpoint')
router.register(r'changelog', views.ChangeLogViewSet, basename='changelog')

urlpatterns = [
    # Web-based documentation pages
    path('', views.DocumentationHomeView.as_view(), name='home'),
    path('setup/', views.SetupGuideView.as_view(), name='setup'),
    path('api/', views.APIDocumentationView.as_view(), name='api-docs'),
    path('api/<int:pk>/', views.APIEndpointDetailView.as_view(), name='api-detail'),
    path('changelog/', views.ChangeLogView.as_view(), name='changelog'),
    path('faq/', views.FAQView.as_view(), name='faq'),
    path('testing/', views.APITestingGuideView.as_view(), name='testing'),
    path('architecture/', views.ArchitectureView.as_view(), name='architecture'),
    
    # REST API endpoints for documentation data
    path('api-data/', include(router.urls)),
]
