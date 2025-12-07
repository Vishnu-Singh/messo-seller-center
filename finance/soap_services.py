from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Payment, Invoice, Settlement
from soap_utils import create_soap_response, create_soap_error, parse_soap_request, create_wsdl


@csrf_exempt
@require_POST
def finance_soap_service(request):
    """Simple SOAP service for finance"""
    try:
        operation, params = parse_soap_request(request.body)
        response_data = ""
        
        if operation == 'get_payment':
            payment_id = params.get('payment_id')
            if payment_id:
                try:
                    payment = Payment.objects.get(payment_id=payment_id)
                    response_data = f"Payment: {payment.payment_id}, Amount: ${payment.amount}, Status: {payment.status}"
                except Payment.DoesNotExist:
                    response_data = f"Payment with ID {payment_id} not found"
        
        elif operation == 'list_settlements':
            settlements = Settlement.objects.all()[:10]
            result = []
            for settlement in settlements:
                result.append(f"{settlement.settlement_id}: ${settlement.net_amount} ({settlement.status})")
            response_data = "\n".join(result) if result else "No settlements found"
        
        else:
            response_data = f"Unknown operation: {operation}"
        
        return create_soap_response(operation, response_data)
    
    except Exception as e:
        return create_soap_error(str(e))


def finance_wsdl(request):
    """WSDL definition for finance SOAP service"""
    return create_wsdl(
        "FinanceService",
        "http://messo.finance.soap/",
        ["get_payment", "list_settlements"],
        "http://localhost:8000/finance/soap/"
    )

