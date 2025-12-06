from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Campaign, Discount, Voucher
from soap_utils import create_soap_response, create_soap_error, parse_soap_request, create_wsdl


@csrf_exempt
@require_POST
def promotions_soap_service(request):
    """Simple SOAP service for promotions"""
    try:
        operation, params = parse_soap_request(request.body)
        response_data = ""
        
        if operation == 'validate_discount_code':
            code = params.get('code')
            if code:
                try:
                    discount = Discount.objects.get(code=code)
                    if discount.is_active:
                        response_data = f"Valid: {discount.name}, Type: {discount.discount_type}, Value: {discount.discount_value}"
                    else:
                        response_data = "Discount code is not active"
                except Discount.DoesNotExist:
                    response_data = f"Discount code {code} not found"
        
        elif operation == 'list_active_campaigns':
            campaigns = Campaign.objects.filter(status='active')[:10]
            result = []
            for campaign in campaigns:
                result.append(f"{campaign.campaign_id}: {campaign.name}")
            response_data = "\n".join(result) if result else "No active campaigns found"
        
        else:
            response_data = f"Unknown operation: {operation}"
        
        return create_soap_response(operation, response_data)
    
    except Exception as e:
        return create_soap_error(str(e))


def promotions_wsdl(request):
    """WSDL definition for promotions SOAP service"""
    return create_wsdl(
        "PromotionService",
        "http://messo.promotions.soap/",
        ["validate_discount_code", "list_active_campaigns"],
        "http://localhost:8000/promotions/soap/"
    )

