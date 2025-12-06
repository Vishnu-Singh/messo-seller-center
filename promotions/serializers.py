from rest_framework import serializers
from .models import Campaign, Discount, Voucher, ProductPromotion


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['id', 'campaign_id', 'name', 'description', 'status', 'start_date',
                  'end_date', 'budget', 'target_audience', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'discount_id', 'code', 'name', 'description', 'discount_type',
                  'discount_value', 'minimum_purchase', 'maximum_discount', 'usage_limit',
                  'usage_count', 'valid_from', 'valid_until', 'is_active', 'created_at']
        read_only_fields = ['created_at', 'usage_count']


class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = ['id', 'voucher_id', 'code', 'discount', 'customer_email',
                  'is_redeemed', 'redeemed_at', 'created_at']
        read_only_fields = ['created_at']


class ProductPromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPromotion
        fields = ['id', 'promotion_id', 'product', 'campaign', 'discount_percentage',
                  'start_date', 'end_date', 'is_active']
