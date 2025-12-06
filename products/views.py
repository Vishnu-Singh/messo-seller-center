from django.db import models
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product, ProductImage, Inventory
from .serializers import ProductSerializer, ProductImageSerializer, InventorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    REST API ViewSet for Product management
    Provides CRUD operations for products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    @action(detail=True, methods=['get'])
    def inventory(self, request, pk=None):
        """Get inventory details for a specific product"""
        product = self.get_object()
        try:
            inventory = product.inventory
            serializer = InventorySerializer(inventory)
            return Response(serializer.data)
        except Inventory.DoesNotExist:
            return Response(
                {"error": "Inventory not found for this product"},
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=True, methods=['get'])
    def images(self, request, pk=None):
        """Get all images for a specific product"""
        product = self.get_object()
        images = product.images.all()
        serializer = ProductImageSerializer(images, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        """Search products by name, sku, or category"""
        query = request.query_params.get('q', '')
        category = request.query_params.get('category', '')
        
        products = self.queryset
        if query:
            products = products.filter(
                models.Q(name__icontains=query) | 
                models.Q(sku__icontains=query)
            )
        if category:
            products = products.filter(category__icontains=category)
        
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)


class ProductImageViewSet(viewsets.ModelViewSet):
    """REST API ViewSet for Product Images"""
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    """REST API ViewSet for Inventory management"""
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
