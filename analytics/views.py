from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import SalesReport, ProductAnalytics, CustomerInsight, PerformanceMetric
from .serializers import (SalesReportSerializer, ProductAnalyticsSerializer, 
                         CustomerInsightSerializer, PerformanceMetricSerializer)


class SalesReportViewSet(viewsets.ModelViewSet):
    """REST API ViewSet for Sales Report management"""
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer
    
    @action(detail=False, methods=['get'])
    def by_period(self, request):
        """Filter reports by period type"""
        period_type = request.query_params.get('period_type', '')
        if period_type:
            reports = self.queryset.filter(period_type=period_type)
        else:
            reports = self.queryset
        
        serializer = self.get_serializer(reports, many=True)
        return Response(serializer.data)


class ProductAnalyticsViewSet(viewsets.ModelViewSet):
    """REST API ViewSet for Product Analytics"""
    queryset = ProductAnalytics.objects.all()
    serializer_class = ProductAnalyticsSerializer
    
    @action(detail=False, methods=['get'])
    def top_products(self, request):
        """Get top performing products by revenue"""
        limit = int(request.query_params.get('limit', 10))
        products = self.queryset.order_by('-revenue')[:limit]
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)


class CustomerInsightViewSet(viewsets.ModelViewSet):
    """REST API ViewSet for Customer Insights"""
    queryset = CustomerInsight.objects.all()
    serializer_class = CustomerInsightSerializer
    
    @action(detail=False, methods=['get'])
    def top_customers(self, request):
        """Get top customers by total spent"""
        limit = int(request.query_params.get('limit', 10))
        customers = self.queryset.order_by('-total_spent')[:limit]
        serializer = self.get_serializer(customers, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_segment(self, request):
        """Filter customers by segment"""
        segment = request.query_params.get('segment', '')
        if segment:
            customers = self.queryset.filter(customer_segment=segment)
        else:
            customers = self.queryset
        
        serializer = self.get_serializer(customers, many=True)
        return Response(serializer.data)


class PerformanceMetricViewSet(viewsets.ModelViewSet):
    """REST API ViewSet for Performance Metrics"""
    queryset = PerformanceMetric.objects.all()
    serializer_class = PerformanceMetricSerializer
    
    @action(detail=False, methods=['get'])
    def by_type(self, request):
        """Filter metrics by type"""
        metric_type = request.query_params.get('metric_type', '')
        if metric_type:
            metrics = self.queryset.filter(metric_type=metric_type)
        else:
            metrics = self.queryset
        
        serializer = self.get_serializer(metrics, many=True)
        return Response(serializer.data)
