from rest_framework import serializers
from .models import Payment, Invoice, Settlement


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'payment_id', 'order', 'amount', 'currency', 'payment_method',
                  'status', 'transaction_id', 'payment_gateway', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'invoice_id', 'order', 'invoice_number', 'subtotal', 'tax_amount',
                  'discount_amount', 'total_amount', 'issued_date', 'due_date', 'paid_date', 'notes']
        read_only_fields = ['issued_date']


class SettlementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settlement
        fields = ['id', 'settlement_id', 'period_start', 'period_end', 'total_sales',
                  'commission', 'net_amount', 'status', 'payment_date', 'created_at']
        read_only_fields = ['created_at']
