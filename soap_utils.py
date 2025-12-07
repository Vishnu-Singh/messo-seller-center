"""Helper utilities for SOAP services"""
import xml.etree.ElementTree as ET
from django.http import HttpResponse


def create_soap_response(operation, result_data):
    """Create a SOAP response XML"""
    soap_response = f"""<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <{operation}Response>
            <result>{result_data}</result>
        </{operation}Response>
    </soap:Body>
</soap:Envelope>"""
    return HttpResponse(soap_response, content_type='text/xml')


def create_soap_error(error_message):
    """Create a SOAP fault response"""
    error_response = f"""<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <soap:Fault>
            <faultcode>soap:Server</faultcode>
            <faultstring>{error_message}</faultstring>
        </soap:Fault>
    </soap:Body>
</soap:Envelope>"""
    return HttpResponse(error_response, content_type='text/xml', status=500)


def parse_soap_request(request_body):
    """Parse SOAP request and extract operation name and parameters"""
    try:
        root = ET.fromstring(request_body)
        
        # Extract operation name
        body = root.find('.//{http://schemas.xmlsoap.org/soap/envelope/}Body')
        if body is None:
            body = root.find('.//Body') or root
        
        operation = None
        params = {}
        
        for child in body:
            operation = child.tag.split('}')[-1] if '}' in child.tag else child.tag
            # Extract parameters
            for param in child:
                param_name = param.tag.split('}')[-1] if '}' in param.tag else param.tag
                params[param_name] = param.text
            break
        
        return operation, params
    except Exception as e:
        raise ValueError(f"Invalid SOAP request: {str(e)}")


def create_wsdl(service_name, target_namespace, operations, location):
    """Generate basic WSDL for a service"""
    operations_xml = ""
    for op in operations:
        operations_xml += f"""
        <operation name="{op}">
            <input message="tns:{op}Request"/>
            <output message="tns:{op}Response"/>
        </operation>"""
    
    wsdl = f"""<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://schemas.xmlsoap.org/wsdl/"
             xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
             xmlns:tns="{target_namespace}"
             targetNamespace="{target_namespace}">
    <portType name="{service_name}PortType">{operations_xml}
    </portType>
    <binding name="{service_name}Binding" type="tns:{service_name}PortType">
        <soap:binding transport="http://schemas.xmlsoap.org/soap/http"/>
    </binding>
    <service name="{service_name}">
        <port name="{service_name}Port" binding="tns:{service_name}Binding">
            <soap:address location="{location}"/>
        </port>
    </service>
</definitions>"""
    return HttpResponse(wsdl, content_type='text/xml')
