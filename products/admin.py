from django.contrib import admin
from .models import Product, ProductImage, Inventory

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'name', 'sku', 'price', 'stock_quantity', 'status', 'created_at']
    list_filter = ['status', 'category', 'created_at']
    search_fields = ['name', 'sku', 'product_id']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image_url', 'is_primary', 'created_at']
    list_filter = ['is_primary', 'created_at']


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'warehouse_location', 'available_quantity', 'reserved_quantity']
    search_fields = ['product__name', 'warehouse_location']
