from django.contrib import admin
from .models import Payment, Invoice, Settlement

# Register your models here.


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payment_id', 'order', 'amount', 'payment_method', 'status', 'created_at']
    list_filter = ['status', 'payment_method', 'created_at']
    search_fields = ['payment_id', 'transaction_id']


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_id', 'invoice_number', 'order', 'total_amount', 'issued_date']
    search_fields = ['invoice_id', 'invoice_number']


@admin.register(Settlement)
class SettlementAdmin(admin.ModelAdmin):
    list_display = ['settlement_id', 'period_start', 'period_end', 'net_amount', 'status', 'created_at']
    list_filter = ['status', 'created_at']
