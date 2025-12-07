# Messo Seller Center API Endpoints Map

## Complete Endpoint Structure

```
http://localhost:8000/
│
├── / (API Root - Documentation)
│   └── GET → API documentation with all endpoints
│
├── /admin/ (Django Admin Panel)
│   └── Full CRUD interface for all models
│
├── /products/
│   ├── /api/ (REST API)
│   │   ├── /products/
│   │   │   ├── GET → List all products
│   │   │   ├── POST → Create product
│   │   │   ├── /{id}/ → GET/PUT/PATCH/DELETE specific product
│   │   │   ├── /{id}/inventory/ → GET product inventory
│   │   │   ├── /{id}/images/ → GET product images
│   │   │   └── /search/ → GET search products (?q=&category=)
│   │   ├── /product-images/
│   │   │   ├── GET → List all images
│   │   │   ├── POST → Create image
│   │   │   └── /{id}/ → GET/PUT/PATCH/DELETE
│   │   └── /inventory/
│   │       ├── GET → List all inventory
│   │       ├── POST → Create inventory
│   │       └── /{id}/ → GET/PUT/PATCH/DELETE
│   │
│   └── /soap/ (SOAP API)
│       ├── POST → SOAP operations
│       │   ├── get_product
│       │   └── list_products
│       └── /wsdl/ → GET WSDL definition
│
├── /orders/
│   ├── /api/ (REST API)
│   │   ├── /orders/
│   │   │   ├── GET → List all orders
│   │   │   ├── POST → Create order
│   │   │   ├── /{id}/ → GET/PUT/PATCH/DELETE
│   │   │   ├── /{id}/cancel/ → POST cancel order
│   │   │   ├── /{id}/confirm/ → POST confirm order
│   │   │   ├── /{id}/tracking/ → GET tracking info
│   │   │   └── /by_status/ → GET filter by status (?status=)
│   │   ├── /order-items/
│   │   │   ├── GET → List all items
│   │   │   ├── POST → Create item
│   │   │   └── /{id}/ → GET/PUT/PATCH/DELETE
│   │   └── /order-tracking/
│   │       ├── GET → List all tracking
│   │       ├── POST → Create tracking
│   │       └── /{id}/ → GET/PUT/PATCH/DELETE
│   │
│   └── /soap/ (SOAP API)
│       ├── POST → SOAP operations
│       │   ├── get_order
│       │   ├── list_orders
│       │   └── get_tracking
│       └── /wsdl/ → GET WSDL definition
│
├── /logistics/
│   ├── /api/ (REST API)
│   │   ├── /shipments/
│   │   │   ├── GET → List all shipments
│   │   │   ├── POST → Create shipment
│   │   │   ├── /{id}/ → GET/PUT/PATCH/DELETE
│   │   │   ├── /{id}/track/ → GET tracking with events
│   │   │   └── /{id}/update_status/ → POST update status
│   │   ├── /shipment-events/
│   │   │   ├── GET → List all events
│   │   │   ├── POST → Create event
│   │   │   └── /{id}/ → GET/PUT/PATCH/DELETE
│   │   └── /warehouses/
│   │       ├── GET → List all warehouses
│   │       ├── POST → Create warehouse
│   │       └── /{id}/ → GET/PUT/PATCH/DELETE
│   │
│   └── /soap/ (SOAP API)
│       ├── POST → SOAP operations
│       │   ├── track_shipment
│       │   └── list_warehouses
│       └── /wsdl/ → GET WSDL definition
│
├── /finance/
│   ├── /api/ (REST API)
│   │   ├── /payments/
│   │   │   ├── GET → List all payments
│   │   │   ├── POST → Create payment
│   │   │   ├── /{id}/ → GET/PUT/PATCH/DELETE
│   │   │   ├── /{id}/process/ → POST process payment
│   │   │   └── /{id}/refund/ → POST refund payment
│   │   ├── /invoices/
│   │   │   ├── GET → List all invoices
│   │   │   ├── POST → Create invoice
│   │   │   ├── /{id}/ → GET/PUT/PATCH/DELETE
│   │   │   └── /{id}/mark_paid/ → POST mark as paid
│   │   └── /settlements/
│   │       ├── GET → List all settlements
│   │       ├── POST → Create settlement
│   │       ├── /{id}/ → GET/PUT/PATCH/DELETE
│   │       └── /{id}/complete/ → POST complete settlement
│   │
│   └── /soap/ (SOAP API)
│       ├── POST → SOAP operations
│       │   ├── get_payment
│       │   └── list_settlements
│       └── /wsdl/ → GET WSDL definition
│
├── /promotions/
│   ├── /api/ (REST API)
│   │   ├── /campaigns/
│   │   │   ├── GET → List all campaigns
│   │   │   ├── POST → Create campaign
│   │   │   ├── /{id}/ → GET/PUT/PATCH/DELETE
│   │   │   ├── /{id}/activate/ → POST activate campaign
│   │   │   └── /{id}/pause/ → POST pause campaign
│   │   ├── /discounts/
│   │   │   ├── GET → List all discounts
│   │   │   ├── POST → Create discount
│   │   │   ├── /{id}/ → GET/PUT/PATCH/DELETE
│   │   │   └── /{id}/validate_code/ → POST validate code
│   │   ├── /vouchers/
│   │   │   ├── GET → List all vouchers
│   │   │   ├── POST → Create voucher
│   │   │   ├── /{id}/ → GET/PUT/PATCH/DELETE
│   │   │   └── /{id}/redeem/ → POST redeem voucher
│   │   └── /product-promotions/
│   │       ├── GET → List all promotions
│   │       ├── POST → Create promotion
│   │       └── /{id}/ → GET/PUT/PATCH/DELETE
│   │
│   └── /soap/ (SOAP API)
│       ├── POST → SOAP operations
│       │   ├── validate_discount_code
│       │   └── list_active_campaigns
│       └── /wsdl/ → GET WSDL definition
│
└── /analytics/
    ├── /api/ (REST API)
    │   ├── /sales-reports/
    │   │   ├── GET → List all reports
    │   │   ├── POST → Create report
    │   │   ├── /{id}/ → GET/PUT/PATCH/DELETE
    │   │   └── /by_period/ → GET filter by period (?period_type=)
    │   ├── /product-analytics/
    │   │   ├── GET → List all analytics
    │   │   ├── POST → Create analytics
    │   │   ├── /{id}/ → GET/PUT/PATCH/DELETE
    │   │   └── /top_products/ → GET top products (?limit=)
    │   ├── /customer-insights/
    │   │   ├── GET → List all insights
    │   │   ├── POST → Create insight
    │   │   ├── /{id}/ → GET/PUT/PATCH/DELETE
    │   │   ├── /top_customers/ → GET top customers (?limit=)
    │   │   └── /by_segment/ → GET filter by segment (?segment=)
    │   └── /performance-metrics/
    │       ├── GET → List all metrics
    │       ├── POST → Create metric
    │       ├── /{id}/ → GET/PUT/PATCH/DELETE
    │       └── /by_type/ → GET filter by type (?metric_type=)
    │
    └── /soap/ (SOAP API)
        ├── POST → SOAP operations
        │   ├── get_sales_report
        │   ├── get_top_products
        │   └── get_top_customers
        └── /wsdl/ → GET WSDL definition
```

## Quick Reference

### REST API Base URLs
| App | Base URL |
|-----|----------|
| Products | `/products/api/` |
| Orders | `/orders/api/` |
| Logistics | `/logistics/api/` |
| Finance | `/finance/api/` |
| Promotions | `/promotions/api/` |
| Analytics | `/analytics/api/` |

### SOAP API Base URLs
| App | Base URL | WSDL |
|-----|----------|------|
| Products | `/products/soap/` | `/products/soap/wsdl/` |
| Orders | `/orders/soap/` | `/orders/soap/wsdl/` |
| Logistics | `/logistics/soap/` | `/logistics/soap/wsdl/` |
| Finance | `/finance/soap/` | `/finance/soap/wsdl/` |
| Promotions | `/promotions/soap/` | `/promotions/soap/wsdl/` |
| Analytics | `/analytics/soap/` | `/analytics/soap/wsdl/` |

## Endpoint Count Summary

| App | REST Endpoints | SOAP Operations | Total |
|-----|----------------|-----------------|-------|
| Products | 11 | 2 | 13 |
| Orders | 12 | 3 | 15 |
| Logistics | 11 | 2 | 13 |
| Finance | 14 | 2 | 16 |
| Promotions | 16 | 2 | 18 |
| Analytics | 18 | 3 | 21 |
| **Total** | **82** | **14** | **96** |

## HTTP Methods Used

### REST APIs
- **GET**: Retrieve resources
- **POST**: Create resources or trigger actions
- **PUT**: Full update of resources
- **PATCH**: Partial update of resources
- **DELETE**: Remove resources

### SOAP APIs
- **POST**: All SOAP operations use POST method
- Request body contains XML SOAP envelope
- Response is XML SOAP envelope

## Authentication & Authorization

**Current Status**: Open access (Development)

**Production Recommendations**:
- Add JWT or OAuth2 for REST APIs
- Add WS-Security for SOAP APIs
- Implement role-based access control
- Use API keys for service-to-service calls

## Response Formats

### REST API
```json
{
  "id": 1,
  "field": "value",
  "nested": {
    "field": "value"
  }
}
```

### SOAP API
```xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <operationResponse>
      <result>Result data</result>
    </operationResponse>
  </soap:Body>
</soap:Envelope>
```

## Testing Tools

- **REST**: curl, Postman, HTTPie, Insomnia
- **SOAP**: SoapUI, Postman, curl with XML
- **Browser**: Django REST Framework browsable API

## See Also

- `README.md` - Project overview and setup
- `API_TESTING.md` - Detailed testing examples
- `ARCHITECTURE.md` - System architecture
- `PROJECT_SUMMARY.md` - Implementation summary
