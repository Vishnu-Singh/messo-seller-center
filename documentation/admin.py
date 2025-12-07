from django.contrib import admin
from .models import APIEndpoint, APIChangeLog, SetupGuide, FAQ

# Register your models here.

@admin.register(APIEndpoint)
class APIEndpointAdmin(admin.ModelAdmin):
    list_display = ['name', 'app', 'api_type', 'url_path', 'http_method', 'is_active', 'updated_at']
    list_filter = ['app', 'api_type', 'is_active', 'created_at']
    search_fields = ['name', 'url_path', 'description']
    ordering = ['app', 'name']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'app', 'api_type', 'url_path', 'http_method', 'is_active')
        }),
        ('Documentation', {
            'fields': ('description', 'request_example', 'response_example')
        }),
    )


@admin.register(APIChangeLog)
class APIChangeLogAdmin(admin.ModelAdmin):
    list_display = ['endpoint', 'change_type', 'version', 'breaking_change', 'changed_at', 'changed_by']
    list_filter = ['change_type', 'breaking_change', 'version', 'changed_at']
    search_fields = ['description', 'version', 'changed_by']
    ordering = ['-changed_at']
    date_hierarchy = 'changed_at'
    
    fieldsets = (
        ('Change Information', {
            'fields': ('endpoint', 'change_type', 'version', 'breaking_change')
        }),
        ('Details', {
            'fields': ('description', 'changed_by', 'changed_at')
        }),
    )


@admin.register(SetupGuide)
class SetupGuideAdmin(admin.ModelAdmin):
    list_display = ['title', 'guide_type', 'order', 'is_published', 'updated_at']
    list_filter = ['guide_type', 'is_published', 'created_at']
    search_fields = ['title', 'content']
    ordering = ['order', 'title']
    
    fieldsets = (
        ('Guide Information', {
            'fields': ('title', 'guide_type', 'order', 'is_published')
        }),
        ('Content', {
            'fields': ('content',)
        }),
    )


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'category', 'order', 'is_published', 'created_at']
    list_filter = ['category', 'is_published', 'created_at']
    search_fields = ['question', 'answer']
    ordering = ['order', 'question']
    
    fieldsets = (
        ('Question', {
            'fields': ('question', 'category', 'order', 'is_published')
        }),
        ('Answer', {
            'fields': ('answer',)
        }),
    )

