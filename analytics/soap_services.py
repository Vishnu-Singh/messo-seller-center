from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import SalesReport, ProductAnalytics, CustomerInsight
from soap_utils import create_soap_response, create_soap_error, parse_soap_request, create_wsdl


@csrf_exempt
@require_POST
def analytics_soap_service(request):
    """Simple SOAP service for analytics"""
    try:
        operation, params = parse_soap_request(request.body)
        response_data = ""
        
        if operation == 'get_sales_report':
            report_id = params.get('report_id')
            if report_id:
                try:
                    report = SalesReport.objects.get(report_id=report_id)
                    response_data = f"Report: {report.period_type}, Total Sales: ${report.total_sales}, Orders: {report.total_orders}"
                except SalesReport.DoesNotExist:
                    response_data = f"Sales report with ID {report_id} not found"
        
        elif operation == 'get_top_products':
            products = ProductAnalytics.objects.order_by('-revenue')[:10]
            result = []
            for product in products:
                result.append(f"{product.product_name}: ${product.revenue} revenue")
            response_data = "\n".join(result) if result else "No product analytics available"
        
        elif operation == 'get_top_customers':
            customers = CustomerInsight.objects.order_by('-total_spent')[:10]
            result = []
            for customer in customers:
                result.append(f"{customer.customer_email}: ${customer.total_spent} spent")
            response_data = "\n".join(result) if result else "No customer insights available"
        
        else:
            response_data = f"Unknown operation: {operation}"
        
        return create_soap_response(operation, response_data)
    
    except Exception as e:
        return create_soap_error(str(e))


def analytics_wsdl(request):
    """WSDL definition for analytics SOAP service"""
    return create_wsdl(
        "AnalyticsService",
        "http://messo.analytics.soap/",
        ["get_sales_report", "get_top_products", "get_top_customers"],
        "http://localhost:8000/analytics/soap/"
    )

