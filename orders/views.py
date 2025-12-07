from django.db import models
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Order, OrderItem, OrderTracking
from .serializers import OrderSerializer, OrderItemSerializer, OrderTrackingSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    REST API ViewSet for Order management
    Provides CRUD operations for orders
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        """Cancel an order"""
        order = self.get_object()
        if order.status in ['delivered', 'cancelled']:
            return Response(
                {"error": f"Cannot cancel order with status {order.status}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        order.status = 'cancelled'
        order.save()
        return Response({"message": "Order cancelled successfully"})
    
    @action(detail=True, methods=['post'])
    def confirm(self, request, pk=None):
        """Confirm an order"""
        order = self.get_object()
        if order.status != 'pending':
            return Response(
                {"error": f"Cannot confirm order with status {order.status}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        order.status = 'confirmed'
        order.save()
        return Response({"message": "Order confirmed successfully"})
    
    @action(detail=True, methods=['get'])
    def tracking(self, request, pk=None):
        """Get tracking information for an order"""
        order = self.get_object()
        try:
            tracking = order.tracking
            serializer = OrderTrackingSerializer(tracking)
            return Response(serializer.data)
        except OrderTracking.DoesNotExist:
            return Response(
                {"error": "Tracking information not available"},
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=False, methods=['get'])
    def by_status(self, request):
        """Filter orders by status"""
        status_filter = request.query_params.get('status', '')
        if status_filter:
            orders = self.queryset.filter(status=status_filter)
        else:
            orders = self.queryset
        
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)


class OrderItemViewSet(viewsets.ModelViewSet):
    """REST API ViewSet for Order Items"""
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderTrackingViewSet(viewsets.ModelViewSet):
    """REST API ViewSet for Order Tracking"""
    queryset = OrderTracking.objects.all()
    serializer_class = OrderTrackingSerializer
