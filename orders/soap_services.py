from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Order, OrderTracking
from soap_utils import create_soap_response, create_soap_error, parse_soap_request, create_wsdl


@csrf_exempt
@require_POST
def orders_soap_service(request):
    """Simple SOAP service for orders"""
    try:
        operation, params = parse_soap_request(request.body)
        response_data = ""
        
        if operation == 'get_order':
            order_id = params.get('order_id')
            if order_id:
                try:
                    order = Order.objects.get(order_id=order_id)
                    response_data = f"Order: {order.order_id}, Customer: {order.customer_name}, Status: {order.status}, Total: ${order.total_amount}"
                except Order.DoesNotExist:
                    response_data = f"Order with ID {order_id} not found"
        
        elif operation == 'list_orders':
            orders = Order.objects.all()[:10]
            result = []
            for order in orders:
                result.append(f"{order.order_id}: {order.customer_name} - ${order.total_amount} ({order.status})")
            response_data = "\n".join(result) if result else "No orders found"
        
        elif operation == 'get_tracking':
            order_id = params.get('order_id')
            if order_id:
                try:
                    order = Order.objects.get(order_id=order_id)
                    tracking = order.tracking
                    response_data = f"Tracking Number: {tracking.tracking_number}, Carrier: {tracking.carrier}"
                except Order.DoesNotExist:
                    response_data = f"Order with ID {order_id} not found"
                except OrderTracking.DoesNotExist:
                    response_data = f"Tracking information not available"
        
        else:
            response_data = f"Unknown operation: {operation}"
        
        return create_soap_response(operation, response_data)
    
    except Exception as e:
        return create_soap_error(str(e))


def orders_wsdl(request):
    """WSDL definition for orders SOAP service"""
    return create_wsdl(
        "OrderService",
        "http://messo.orders.soap/",
        ["get_order", "list_orders", "get_tracking"],
        "http://localhost:8000/orders/soap/"
    )

