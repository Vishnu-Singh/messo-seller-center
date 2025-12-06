from django.db import models
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Shipment, ShipmentEvent, Warehouse
from .serializers import ShipmentSerializer, ShipmentEventSerializer, WarehouseSerializer


class ShipmentViewSet(viewsets.ModelViewSet):
    """REST API ViewSet for Shipment management"""
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    
    @action(detail=True, methods=['get'])
    def track(self, request, pk=None):
        """Track shipment with events"""
        shipment = self.get_object()
        events = shipment.events.all()
        serializer = ShipmentEventSerializer(events, many=True)
        return Response({
            'shipment': ShipmentSerializer(shipment).data,
            'events': serializer.data
        })
    
    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        """Update shipment status"""
        shipment = self.get_object()
        new_status = request.data.get('status')
        if new_status:
            shipment.status = new_status
            shipment.save()
            return Response({"message": "Status updated successfully"})
        return Response({"error": "Status is required"}, status=status.HTTP_400_BAD_REQUEST)


class ShipmentEventViewSet(viewsets.ModelViewSet):
    """REST API ViewSet for Shipment Events"""
    queryset = ShipmentEvent.objects.all()
    serializer_class = ShipmentEventSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    """REST API ViewSet for Warehouse management"""
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
