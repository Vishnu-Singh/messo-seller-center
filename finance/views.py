from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Payment, Invoice, Settlement
from .serializers import PaymentSerializer, InvoiceSerializer, SettlementSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """REST API ViewSet for Payment management"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    @action(detail=True, methods=['post'])
    def process(self, request, pk=None):
        """Process a payment"""
        payment = self.get_object()
        if payment.status != 'pending':
            return Response(
                {"error": f"Cannot process payment with status {payment.status}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        payment.status = 'processing'
        payment.save()
        return Response({"message": "Payment processing started"})
    
    @action(detail=True, methods=['post'])
    def refund(self, request, pk=None):
        """Refund a payment"""
        payment = self.get_object()
        if payment.status != 'completed':
            return Response(
                {"error": "Can only refund completed payments"},
                status=status.HTTP_400_BAD_REQUEST
            )
        payment.status = 'refunded'
        payment.save()
        return Response({"message": "Payment refunded successfully"})


class InvoiceViewSet(viewsets.ModelViewSet):
    """REST API ViewSet for Invoice management"""
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    
    @action(detail=True, methods=['post'])
    def mark_paid(self, request, pk=None):
        """Mark an invoice as paid"""
        invoice = self.get_object()
        from django.utils import timezone
        invoice.paid_date = timezone.now()
        invoice.save()
        return Response({"message": "Invoice marked as paid"})


class SettlementViewSet(viewsets.ModelViewSet):
    """REST API ViewSet for Settlement management"""
    queryset = Settlement.objects.all()
    serializer_class = SettlementSerializer
    
    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        """Complete a settlement"""
        settlement = self.get_object()
        if settlement.status != 'pending':
            return Response(
                {"error": f"Cannot complete settlement with status {settlement.status}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        settlement.status = 'completed'
        from django.utils import timezone
        settlement.payment_date = timezone.now()
        settlement.save()
        return Response({"message": "Settlement completed successfully"})
