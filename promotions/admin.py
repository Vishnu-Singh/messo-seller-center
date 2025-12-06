from django.contrib import admin
from .models import Campaign, Discount, Voucher, ProductPromotion

# Register your models here.


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ['campaign_id', 'name', 'status', 'start_date', 'end_date', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['campaign_id', 'name']


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['discount_id', 'code', 'name', 'discount_type', 'discount_value', 'is_active']
    list_filter = ['discount_type', 'is_active', 'created_at']
    search_fields = ['code', 'name']


@admin.register(Voucher)
class VoucherAdmin(admin.ModelAdmin):
    list_display = ['voucher_id', 'code', 'is_redeemed', 'customer_email', 'created_at']
    list_filter = ['is_redeemed', 'created_at']
    search_fields = ['code', 'customer_email']


@admin.register(ProductPromotion)
class ProductPromotionAdmin(admin.ModelAdmin):
    list_display = ['promotion_id', 'product', 'discount_percentage', 'start_date', 'end_date', 'is_active']
    list_filter = ['is_active', 'start_date']
