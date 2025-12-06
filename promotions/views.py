from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Campaign, Discount, Voucher, ProductPromotion
from .serializers import CampaignSerializer, DiscountSerializer, VoucherSerializer, ProductPromotionSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    """REST API ViewSet for Campaign management"""
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    
    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        """Activate a campaign"""
        campaign = self.get_object()
        campaign.status = 'active'
        campaign.save()
        return Response({"message": "Campaign activated successfully"})
    
    @action(detail=True, methods=['post'])
    def pause(self, request, pk=None):
        """Pause a campaign"""
        campaign = self.get_object()
        campaign.status = 'paused'
        campaign.save()
        return Response({"message": "Campaign paused successfully"})


class DiscountViewSet(viewsets.ModelViewSet):
    """REST API ViewSet for Discount management"""
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    
    @action(detail=True, methods=['post'])
    def validate_code(self, request, pk=None):
        """Validate a discount code"""
        discount = self.get_object()
        from django.utils import timezone
        
        if not discount.is_active:
            return Response({"valid": False, "message": "Discount is not active"})
        
        if timezone.now() < discount.valid_from or timezone.now() > discount.valid_until:
            return Response({"valid": False, "message": "Discount has expired"})
        
        if discount.usage_limit and discount.usage_count >= discount.usage_limit:
            return Response({"valid": False, "message": "Usage limit reached"})
        
        return Response({"valid": True, "discount": DiscountSerializer(discount).data})


class VoucherViewSet(viewsets.ModelViewSet):
    """REST API ViewSet for Voucher management"""
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer
    
    @action(detail=True, methods=['post'])
    def redeem(self, request, pk=None):
        """Redeem a voucher"""
        voucher = self.get_object()
        if voucher.is_redeemed:
            return Response(
                {"error": "Voucher has already been redeemed"},
                status=status.HTTP_400_BAD_REQUEST
            )
        from django.utils import timezone
        voucher.is_redeemed = True
        voucher.redeemed_at = timezone.now()
        voucher.save()
        return Response({"message": "Voucher redeemed successfully"})


class ProductPromotionViewSet(viewsets.ModelViewSet):
    """REST API ViewSet for Product Promotion management"""
    queryset = ProductPromotion.objects.all()
    serializer_class = ProductPromotionSerializer
