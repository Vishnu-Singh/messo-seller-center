from rest_framework import serializers
from .models import Product, ProductImage, Inventory


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image_url', 'is_primary', 'created_at']


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['warehouse_location', 'reserved_quantity', 'available_quantity', 'last_restocked_at']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    inventory = InventorySerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'product_id', 'name', 'description', 'sku', 'price', 
                  'stock_quantity', 'status', 'category', 'brand', 'weight',
                  'created_at', 'updated_at', 'images', 'inventory']
        read_only_fields = ['created_at', 'updated_at']
