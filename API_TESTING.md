# API Testing Guide

This document provides examples of how to test the Messo Seller Center APIs.

## Prerequisites

Start the development server:
```bash
python manage.py runserver
```

The server will be available at `http://localhost:8000/`

## REST API Testing

You can use tools like `curl`, Postman, or any HTTP client to test the REST APIs.

### Products API

#### List all products
```bash
curl -X GET http://localhost:8000/products/api/products/
```

#### Create a product
```bash
curl -X POST http://localhost:8000/products/api/products/ \
  -H "Content-Type: application/json" \
  -d '{
    "product_id": "PROD001",
    "name": "Sample Product",
    "sku": "SKU001",
    "price": "99.99",
    "stock_quantity": 100,
    "status": "active",
    "category": "Electronics",
    "brand": "SampleBrand"
  }'
```

#### Get a specific product
```bash
curl -X GET http://localhost:8000/products/api/products/1/
```

#### Search products
```bash
curl -X GET "http://localhost:8000/products/api/products/search/?q=Sample&category=Electronics"
```

### Orders API

#### List all orders
```bash
curl -X GET http://localhost:8000/orders/api/orders/
```

#### Create an order
```bash
curl -X POST http://localhost:8000/orders/api/orders/ \
  -H "Content-Type: application/json" \
  -d '{
    "order_id": "ORD001",
    "customer_name": "John Doe",
    "customer_email": "john@example.com",
    "total_amount": "149.99",
    "shipping_address": "123 Main St, City, Country",
    "payment_method": "credit_card"
  }'
```

#### Cancel an order
```bash
curl -X POST http://localhost:8000/orders/api/orders/1/cancel/
```

#### Filter orders by status
```bash
curl -X GET "http://localhost:8000/orders/api/orders/by_status/?status=pending"
```

### Logistics API

#### List shipments
```bash
curl -X GET http://localhost:8000/logistics/api/shipments/
```

#### Track a shipment
```bash
curl -X GET http://localhost:8000/logistics/api/shipments/1/track/
```

#### List warehouses
```bash
curl -X GET http://localhost:8000/logistics/api/warehouses/
```

### Finance API

#### List payments
```bash
curl -X GET http://localhost:8000/finance/api/payments/
```

#### Process a payment
```bash
curl -X POST http://localhost:8000/finance/api/payments/1/process/
```

#### List settlements
```bash
curl -X GET http://localhost:8000/finance/api/settlements/
```

### Promotions API

#### List campaigns
```bash
curl -X GET http://localhost:8000/promotions/api/campaigns/
```

#### Validate a discount code
```bash
curl -X POST http://localhost:8000/promotions/api/discounts/1/validate_code/
```

#### List active discounts
```bash
curl -X GET http://localhost:8000/promotions/api/discounts/
```

### Analytics API

#### List sales reports
```bash
curl -X GET http://localhost:8000/analytics/api/sales-reports/
```

#### Get top products
```bash
curl -X GET "http://localhost:8000/analytics/api/product-analytics/top_products/?limit=10"
```

#### Get top customers
```bash
curl -X GET "http://localhost:8000/analytics/api/customer-insights/top_customers/?limit=10"
```

## SOAP API Testing

You can use tools like SoapUI, Postman (with SOAP support), or `curl` to test SOAP APIs.

### Get WSDL

Each SOAP service provides a WSDL:
- Products: `http://localhost:8000/products/soap/wsdl/`
- Orders: `http://localhost:8000/orders/soap/wsdl/`
- Logistics: `http://localhost:8000/logistics/soap/wsdl/`
- Finance: `http://localhost:8000/finance/soap/wsdl/`
- Promotions: `http://localhost:8000/promotions/soap/wsdl/`
- Analytics: `http://localhost:8000/analytics/soap/wsdl/`

### Example SOAP Requests

#### Get Product (SOAP)
```bash
curl -X POST http://localhost:8000/products/soap/ \
  -H "Content-Type: text/xml" \
  -d '<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <get_product>
      <product_id>PROD001</product_id>
    </get_product>
  </soap:Body>
</soap:Envelope>'
```

#### List Products (SOAP)
```bash
curl -X POST http://localhost:8000/products/soap/ \
  -H "Content-Type: text/xml" \
  -d '<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <list_products/>
  </soap:Body>
</soap:Envelope>'
```

#### Get Order (SOAP)
```bash
curl -X POST http://localhost:8000/orders/soap/ \
  -H "Content-Type: text/xml" \
  -d '<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <get_order>
      <order_id>ORD001</order_id>
    </get_order>
  </soap:Body>
</soap:Envelope>'
```

#### Track Shipment (SOAP)
```bash
curl -X POST http://localhost:8000/logistics/soap/ \
  -H "Content-Type: text/xml" \
  -d '<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <track_shipment>
      <tracking_number>TRACK001</tracking_number>
    </track_shipment>
  </soap:Body>
</soap:Envelope>'
```

#### Validate Discount Code (SOAP)
```bash
curl -X POST http://localhost:8000/promotions/soap/ \
  -H "Content-Type: text/xml" \
  -d '<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <validate_discount_code>
      <code>DISCOUNT10</code>
    </validate_discount_code>
  </soap:Body>
</soap:Envelope>'
```

## Django Admin Panel

Access the admin panel at `http://localhost:8000/admin/`

First, create a superuser:
```bash
python manage.py createsuperuser
```

Then login to manage all data through the web interface.

## API Documentation

For comprehensive API documentation, visit:
```
http://localhost:8000/
```

This will show all available endpoints for both REST and SOAP APIs.
