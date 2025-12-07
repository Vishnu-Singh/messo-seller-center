from django.contrib import admin
from .models import Shipment, ShipmentEvent, Warehouse

# Register your models here.


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['shipment_id', 'tracking_number', 'carrier_name', 'status', 'created_at']
    list_filter = ['status', 'carrier_name', 'created_at']
    search_fields = ['shipment_id', 'tracking_number']


@admin.register(ShipmentEvent)
class ShipmentEventAdmin(admin.ModelAdmin):
    list_display = ['shipment', 'event_type', 'location', 'timestamp']
    list_filter = ['event_type', 'timestamp']


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['warehouse_id', 'name', 'city', 'country', 'capacity']
    search_fields = ['name', 'city', 'warehouse_id']
