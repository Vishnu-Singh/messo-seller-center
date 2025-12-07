from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import APIEndpoint, APIChangeLog, SetupGuide, FAQ
from .serializers import APIEndpointSerializer, ChangeLogSerializer
import os
import markdown

# Create your views here.

class DocumentationHomeView(TemplateView):
    """Main documentation homepage"""
    template_name = 'documentation/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Messo Seller Center Documentation'
        context['endpoint_count'] = APIEndpoint.objects.filter(is_active=True).count()
        context['recent_changes'] = APIChangeLog.objects.all()[:5]
        context['apps'] = ['products', 'orders', 'logistics', 'finance', 'promotions', 'analytics']
        return context


class SetupGuideView(ListView):
    """Setup and installation guides"""
    model = SetupGuide
    template_name = 'documentation/setup_guide.html'
    context_object_name = 'guides'
    
    def get_queryset(self):
        return SetupGuide.objects.filter(is_published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Setup Guide'
        
        # Load README content
        readme_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'README.md')
        if os.path.exists(readme_path):
            with open(readme_path, 'r') as f:
                context['readme_content'] = markdown.markdown(f.read())
        
        return context


class APIDocumentationView(ListView):
    """API documentation listing"""
    model = APIEndpoint
    template_name = 'documentation/api_docs.html'
    context_object_name = 'endpoints'
    
    def get_queryset(self):
        queryset = APIEndpoint.objects.filter(is_active=True)
        app = self.request.GET.get('app')
        api_type = self.request.GET.get('type')
        
        if app:
            queryset = queryset.filter(app=app)
        if api_type:
            queryset = queryset.filter(api_type=api_type)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'API Documentation'
        context['apps'] = ['products', 'orders', 'logistics', 'finance', 'promotions', 'analytics']
        context['selected_app'] = self.request.GET.get('app', '')
        context['selected_type'] = self.request.GET.get('type', '')
        return context


class APIEndpointDetailView(DetailView):
    """Detailed view of a specific API endpoint"""
    model = APIEndpoint
    template_name = 'documentation/api_detail.html'
    context_object_name = 'endpoint'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"{self.object.name} - API Documentation"
        context['changes'] = self.object.changes.all()[:10]
        return context


class ChangeLogView(ListView):
    """API changes and version history"""
    model = APIChangeLog
    template_name = 'documentation/changelog.html'
    context_object_name = 'changes'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = APIChangeLog.objects.all()
        version = self.request.GET.get('version')
        if version:
            queryset = queryset.filter(version=version)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'API Change Log'
        context['versions'] = APIChangeLog.objects.values_list('version', flat=True).distinct().order_by('-version')
        return context


class FAQView(ListView):
    """FAQ page"""
    model = FAQ
    template_name = 'documentation/faq.html'
    context_object_name = 'faqs'
    
    def get_queryset(self):
        return FAQ.objects.filter(is_published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Frequently Asked Questions'
        
        # Group FAQs by category
        categories = {}
        for faq in context['faqs']:
            category = faq.category or 'General'
            if category not in categories:
                categories[category] = []
            categories[category].append(faq)
        
        context['faq_categories'] = categories
        return context


class APITestingGuideView(TemplateView):
    """API testing guide"""
    template_name = 'documentation/api_testing.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'API Testing Guide'
        
        # Load API_TESTING.md content
        testing_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'API_TESTING.md')
        if os.path.exists(testing_path):
            with open(testing_path, 'r') as f:
                context['testing_content'] = markdown.markdown(f.read())
        
        return context


class ArchitectureView(TemplateView):
    """Architecture documentation"""
    template_name = 'documentation/architecture.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'System Architecture'
        
        # Load ARCHITECTURE.md content
        arch_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ARCHITECTURE.md')
        if os.path.exists(arch_path):
            with open(arch_path, 'r') as f:
                context['architecture_content'] = markdown.markdown(f.read())
        
        return context


# REST API ViewSets for documentation data

class APIEndpointViewSet(viewsets.ReadOnlyModelViewSet):
    """REST API to query documentation endpoints"""
    queryset = APIEndpoint.objects.filter(is_active=True)
    serializer_class = APIEndpointSerializer
    
    @action(detail=False, methods=['get'])
    def by_app(self, request):
        """Get endpoints by app"""
        app = request.query_params.get('app')
        if app:
            endpoints = self.queryset.filter(app=app)
            serializer = self.get_serializer(endpoints, many=True)
            return Response(serializer.data)
        return Response({"error": "app parameter required"}, status=400)


class ChangeLogViewSet(viewsets.ReadOnlyModelViewSet):
    """REST API to query change logs"""
    queryset = APIChangeLog.objects.all()
    serializer_class = ChangeLogSerializer
