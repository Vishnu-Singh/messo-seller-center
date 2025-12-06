from rest_framework import serializers
from .models import Shipment, ShipmentEvent, Warehouse


class ShipmentEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentEvent
        fields = ['id', 'event_type', 'description', 'location', 'timestamp']


class ShipmentSerializer(serializers.ModelSerializer):
    events = ShipmentEventSerializer(many=True, read_only=True)
    
    class Meta:
        model = Shipment
        fields = ['id', 'shipment_id', 'order', 'carrier_name', 'tracking_number',
                  'status', 'origin_address', 'destination_address', 'weight',
                  'shipping_cost', 'estimated_delivery_date', 'actual_delivery_date',
                  'created_at', 'updated_at', 'events']
        read_only_fields = ['created_at', 'updated_at']


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'warehouse_id', 'name', 'address', 'city', 'state',
                  'country', 'postal_code', 'capacity', 'manager_name', 'contact_phone']
