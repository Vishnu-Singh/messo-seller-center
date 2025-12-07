from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Shipment, Warehouse
from soap_utils import create_soap_response, create_soap_error, parse_soap_request, create_wsdl


@csrf_exempt
@require_POST
def logistics_soap_service(request):
    """Simple SOAP service for logistics"""
    try:
        operation, params = parse_soap_request(request.body)
        response_data = ""
        
        if operation == 'track_shipment':
            tracking_number = params.get('tracking_number')
            if tracking_number:
                try:
                    shipment = Shipment.objects.get(tracking_number=tracking_number)
                    response_data = f"Shipment: {shipment.shipment_id}, Status: {shipment.status}, Carrier: {shipment.carrier_name}"
                except Shipment.DoesNotExist:
                    response_data = f"Shipment with tracking number {tracking_number} not found"
        
        elif operation == 'list_warehouses':
            warehouses = Warehouse.objects.all()[:10]
            result = []
            for warehouse in warehouses:
                result.append(f"{warehouse.warehouse_id}: {warehouse.name} - {warehouse.city}, {warehouse.country}")
            response_data = "\n".join(result) if result else "No warehouses found"
        
        else:
            response_data = f"Unknown operation: {operation}"
        
        return create_soap_response(operation, response_data)
    
    except Exception as e:
        return create_soap_error(str(e))


def logistics_wsdl(request):
    """WSDL definition for logistics SOAP service"""
    return create_wsdl(
        "LogisticsService",
        "http://messo.logistics.soap/",
        ["track_shipment", "list_warehouses"],
        "http://localhost:8000/logistics/soap/"
    )

