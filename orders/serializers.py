from rest_framework import serializers
from .models import Order, OrderItem, OrderTracking
from products.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'unit_price', 'subtotal']


class OrderTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTracking
        fields = ['tracking_number', 'carrier', 'shipped_at', 'estimated_delivery', 'actual_delivery']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    tracking = OrderTrackingSerializer(read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'order_id', 'customer_name', 'customer_email', 'customer_phone',
                  'status', 'total_amount', 'shipping_address', 'billing_address',
                  'payment_method', 'payment_status', 'notes', 'created_at', 'updated_at',
                  'items', 'tracking']
        read_only_fields = ['created_at', 'updated_at']
