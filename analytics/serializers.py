from rest_framework import serializers
from .models import SalesReport, ProductAnalytics, CustomerInsight, PerformanceMetric


class SalesReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesReport
        fields = ['id', 'report_id', 'period_type', 'period_start', 'period_end',
                  'total_sales', 'total_orders', 'total_items_sold', 'average_order_value',
                  'created_at']
        read_only_fields = ['created_at']


class ProductAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAnalytics
        fields = ['id', 'product_id', 'product_name', 'views', 'clicks', 'add_to_cart_count',
                  'purchases', 'revenue', 'conversion_rate', 'report_date', 'created_at']
        read_only_fields = ['created_at']


class CustomerInsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInsight
        fields = ['id', 'customer_email', 'total_orders', 'total_spent', 'average_order_value',
                  'last_order_date', 'customer_segment', 'lifetime_value', 'updated_at']
        read_only_fields = ['updated_at']


class PerformanceMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceMetric
        fields = ['id', 'metric_type', 'metric_value', 'metric_date', 'comparison_period_value',
                  'percentage_change', 'notes', 'created_at']
        read_only_fields = ['created_at']
