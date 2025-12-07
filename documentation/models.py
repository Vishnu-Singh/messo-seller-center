from django.db import models
from django.utils import timezone

# Create your models here.

class APIEndpoint(models.Model):
    """Model to track API endpoints"""
    API_TYPE_CHOICES = [
        ('rest', 'REST API'),
        ('soap', 'SOAP API'),
    ]
    
    APP_CHOICES = [
        ('products', 'Products'),
        ('orders', 'Orders'),
        ('logistics', 'Logistics'),
        ('finance', 'Finance'),
        ('promotions', 'Promotions'),
        ('analytics', 'Analytics'),
    ]
    
    name = models.CharField(max_length=255, help_text="Endpoint name")
    app = models.CharField(max_length=50, choices=APP_CHOICES, help_text="Django app")
    api_type = models.CharField(max_length=10, choices=API_TYPE_CHOICES, help_text="API type")
    url_path = models.CharField(max_length=500, help_text="URL path")
    http_method = models.CharField(max_length=20, blank=True, help_text="HTTP method (for REST)")
    description = models.TextField(help_text="Endpoint description")
    request_example = models.TextField(blank=True, help_text="Example request")
    response_example = models.TextField(blank=True, help_text="Example response")
    is_active = models.BooleanField(default=True, help_text="Is endpoint active?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['app', 'api_type', 'name']
        verbose_name = "API Endpoint"
        verbose_name_plural = "API Endpoints"
    
    def __str__(self):
        return f"{self.app} - {self.name} ({self.api_type.upper()})"


class APIChangeLog(models.Model):
    """Model to track changes to API endpoints"""
    CHANGE_TYPE_CHOICES = [
        ('created', 'Created'),
        ('updated', 'Updated'),
        ('deprecated', 'Deprecated'),
        ('removed', 'Removed'),
    ]
    
    endpoint = models.ForeignKey(APIEndpoint, on_delete=models.CASCADE, related_name='changes', null=True, blank=True)
    change_type = models.CharField(max_length=20, choices=CHANGE_TYPE_CHOICES)
    version = models.CharField(max_length=50, help_text="Version number")
    description = models.TextField(help_text="Change description")
    breaking_change = models.BooleanField(default=False, help_text="Is this a breaking change?")
    changed_at = models.DateTimeField(default=timezone.now)
    changed_by = models.CharField(max_length=255, blank=True, help_text="Who made the change")
    
    class Meta:
        ordering = ['-changed_at']
        verbose_name = "API Change Log"
        verbose_name_plural = "API Change Logs"
    
    def __str__(self):
        endpoint_name = self.endpoint.name if self.endpoint else "General"
        return f"{endpoint_name} - {self.change_type} (v{self.version})"


class SetupGuide(models.Model):
    """Model for setup and installation guides"""
    GUIDE_TYPE_CHOICES = [
        ('installation', 'Installation'),
        ('configuration', 'Configuration'),
        ('deployment', 'Deployment'),
        ('troubleshooting', 'Troubleshooting'),
    ]
    
    title = models.CharField(max_length=255, help_text="Guide title")
    guide_type = models.CharField(max_length=50, choices=GUIDE_TYPE_CHOICES)
    content = models.TextField(help_text="Guide content (supports Markdown)")
    order = models.IntegerField(default=0, help_text="Display order")
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Setup Guide"
        verbose_name_plural = "Setup Guides"
    
    def __str__(self):
        return f"{self.title} ({self.guide_type})"


class FAQ(models.Model):
    """Frequently Asked Questions"""
    question = models.CharField(max_length=500)
    answer = models.TextField()
    category = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'question']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
    
    def __str__(self):
        return self.question
