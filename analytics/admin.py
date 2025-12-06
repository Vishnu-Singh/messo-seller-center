from django.contrib import admin
from .models import SalesReport, ProductAnalytics, CustomerInsight, PerformanceMetric

# Register your models here.


@admin.register(SalesReport)
class SalesReportAdmin(admin.ModelAdmin):
    list_display = ['report_id', 'period_type', 'period_start', 'period_end', 'total_sales', 'total_orders']
    list_filter = ['period_type', 'created_at']
    search_fields = ['report_id']


@admin.register(ProductAnalytics)
class ProductAnalyticsAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'views', 'purchases', 'revenue', 'conversion_rate', 'report_date']
    list_filter = ['report_date', 'created_at']
    search_fields = ['product_id', 'product_name']


@admin.register(CustomerInsight)
class CustomerInsightAdmin(admin.ModelAdmin):
    list_display = ['customer_email', 'total_orders', 'total_spent', 'customer_segment', 'lifetime_value']
    list_filter = ['customer_segment', 'updated_at']
    search_fields = ['customer_email']


@admin.register(PerformanceMetric)
class PerformanceMetricAdmin(admin.ModelAdmin):
    list_display = ['metric_type', 'metric_value', 'metric_date', 'percentage_change']
    list_filter = ['metric_type', 'metric_date']
