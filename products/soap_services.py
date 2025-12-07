from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Product, Inventory
import xml.etree.ElementTree as ET


@csrf_exempt
@require_POST
def products_soap_service(request):
    """Simple SOAP service for products"""
    try:
        # Parse SOAP request
        root = ET.fromstring(request.body)
        
        # Extract operation name
        body = root.find('.//{http://schemas.xmlsoap.org/soap/envelope/}Body')
        if body is None:
            body = root.find('.//Body') or root
        
        operation = None
        for child in body:
            operation = child.tag.split('}')[-1] if '}' in child.tag else child.tag
            break
        
        response_data = ""
        
        # Handle different operations
        if operation == 'get_product':
            product_id = None
            for child in body[0]:
                if 'product_id' in child.tag:
                    product_id = child.text
                    break
            
            if product_id:
                try:
                    product = Product.objects.get(product_id=product_id)
                    response_data = f"Product: {product.name}, SKU: {product.sku}, Price: {product.price}, Stock: {product.stock_quantity}"
                except Product.DoesNotExist:
                    response_data = f"Product with ID {product_id} not found"
            else:
                response_data = "Product ID is required"
        
        elif operation == 'list_products':
            products = Product.objects.all()[:10]
            result = []
            for product in products:
                result.append(f"{product.product_id}: {product.name} - ${product.price}")
            response_data = "\n".join(result) if result else "No products found"
        
        else:
            response_data = f"Unknown operation: {operation}"
        
        # Create SOAP response
        soap_response = f"""<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <{operation}Response>
            <result>{response_data}</result>
        </{operation}Response>
    </soap:Body>
</soap:Envelope>"""
        
        return HttpResponse(soap_response, content_type='text/xml')
    
    except Exception as e:
        error_response = f"""<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <soap:Fault>
            <faultcode>soap:Server</faultcode>
            <faultstring>{str(e)}</faultstring>
        </soap:Fault>
    </soap:Body>
</soap:Envelope>"""
        return HttpResponse(error_response, content_type='text/xml', status=500)


def products_wsdl(request):
    """WSDL definition for products SOAP service"""
    wsdl = """<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://schemas.xmlsoap.org/wsdl/"
             xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
             xmlns:tns="http://messo.products.soap/"
             targetNamespace="http://messo.products.soap/">
    <message name="get_productRequest">
        <part name="product_id" type="xsd:string"/>
    </message>
    <message name="get_productResponse">
        <part name="result" type="xsd:string"/>
    </message>
    <portType name="ProductServicePortType">
        <operation name="get_product">
            <input message="tns:get_productRequest"/>
            <output message="tns:get_productResponse"/>
        </operation>
    </portType>
    <binding name="ProductServiceBinding" type="tns:ProductServicePortType">
        <soap:binding transport="http://schemas.xmlsoap.org/soap/http"/>
        <operation name="get_product">
            <soap:operation soapAction="get_product"/>
            <input><soap:body use="literal"/></input>
            <output><soap:body use="literal"/></output>
        </operation>
    </binding>
    <service name="ProductService">
        <port name="ProductServicePort" binding="tns:ProductServiceBinding">
            <soap:address location="http://localhost:8000/products/soap/"/>
        </port>
    </service>
</definitions>"""
    return HttpResponse(wsdl, content_type='text/xml')

