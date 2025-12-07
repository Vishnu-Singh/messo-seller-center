# Messo Seller Center

A full-fledged Django project for Messo Seller Center APIs with both REST and SOAP endpoints.

## Features

- **7 Django Apps** organized by API classification:
  - **Products** - Product management, catalog, and inventory
  - **Orders** - Order processing, fulfillment, and tracking
  - **Logistics** - Shipping, delivery, and warehouse management
  - **Finance** - Payments, invoices, and settlements
  - **Promotions** - Discounts, campaigns, and vouchers
  - **Analytics** - Reports, statistics, and insights
  - **Documentation** - Web-based documentation interface

- **Dual API Support**: Each app provides both REST and SOAP APIs
- **Django REST Framework** for REST APIs
- **Custom SOAP Services** with XML handlers
- **Comprehensive Models** for all business entities
- **Web-Based Documentation** at `/docs/`
- **Interactive Admin Panel** for managing all data

## Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Vishnu-Singh/messo-seller-center.git
cd messo-seller-center
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Populate documentation (optional):
```bash
python manage.py populate_docs
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

## Documentation

### Web-Based Documentation
Visit `http://127.0.0.1:8000/docs/` for the interactive documentation interface featuring:
- 📚 **Homepage** - Project overview with statistics
- 🔍 **API Docs** - Searchable catalog of all endpoints
- 📝 **Changelog** - Version history and API changes
- 📖 **Setup Guide** - Installation and configuration
- 🧪 **Testing Guide** - API testing examples
- 🏗️ **Architecture** - System design documentation
- ❓ **FAQ** - Frequently asked questions

### API Root
Visit `http://127.0.0.1:8000/` to see the API root with quick links.

### REST API Endpoints

#### Products
- **Base URL**: `/products/api/`
- Endpoints:
  - `GET/POST /products/` - List/Create products
  - `GET/PUT/PATCH/DELETE /products/{id}/` - Retrieve/Update/Delete product
  - `GET /products/{id}/inventory/` - Get product inventory
  - `GET /products/{id}/images/` - Get product images
  - `GET /products/search/?q=query&category=cat` - Search products
  - `GET/POST /product-images/` - Manage product images
  - `GET/POST /inventory/` - Manage inventory

#### Orders
- **Base URL**: `/orders/api/`
- Endpoints:
  - `GET/POST /orders/` - List/Create orders
  - `GET/PUT/PATCH/DELETE /orders/{id}/` - Manage orders
  - `POST /orders/{id}/cancel/` - Cancel order
  - `POST /orders/{id}/confirm/` - Confirm order
  - `GET /orders/{id}/tracking/` - Get order tracking
  - `GET /orders/by_status/?status=pending` - Filter by status
  - `GET/POST /order-items/` - Manage order items
  - `GET/POST /order-tracking/` - Manage order tracking

#### Logistics
- **Base URL**: `/logistics/api/`
- Endpoints:
  - `GET/POST /shipments/` - List/Create shipments
  - `GET/PUT/PATCH/DELETE /shipments/{id}/` - Manage shipments
  - `GET /shipments/{id}/track/` - Track shipment with events
  - `POST /shipments/{id}/update_status/` - Update shipment status
  - `GET/POST /shipment-events/` - Manage shipment events
  - `GET/POST /warehouses/` - Manage warehouses

#### Finance
- **Base URL**: `/finance/api/`
- Endpoints:
  - `GET/POST /payments/` - List/Create payments
  - `GET/PUT/PATCH/DELETE /payments/{id}/` - Manage payments
  - `POST /payments/{id}/process/` - Process payment
  - `POST /payments/{id}/refund/` - Refund payment
  - `GET/POST /invoices/` - Manage invoices
  - `POST /invoices/{id}/mark_paid/` - Mark invoice as paid
  - `GET/POST /settlements/` - Manage settlements
  - `POST /settlements/{id}/complete/` - Complete settlement

#### Promotions
- **Base URL**: `/promotions/api/`
- Endpoints:
  - `GET/POST /campaigns/` - List/Create campaigns
  - `GET/PUT/PATCH/DELETE /campaigns/{id}/` - Manage campaigns
  - `POST /campaigns/{id}/activate/` - Activate campaign
  - `POST /campaigns/{id}/pause/` - Pause campaign
  - `GET/POST /discounts/` - Manage discounts
  - `POST /discounts/{id}/validate_code/` - Validate discount code
  - `GET/POST /vouchers/` - Manage vouchers
  - `POST /vouchers/{id}/redeem/` - Redeem voucher
  - `GET/POST /product-promotions/` - Manage product promotions

#### Analytics
- **Base URL**: `/analytics/api/`
- Endpoints:
  - `GET/POST /sales-reports/` - Manage sales reports
  - `GET /sales-reports/by_period/?period_type=monthly` - Filter by period
  - `GET/POST /product-analytics/` - Manage product analytics
  - `GET /product-analytics/top_products/?limit=10` - Top products
  - `GET/POST /customer-insights/` - Manage customer insights
  - `GET /customer-insights/top_customers/?limit=10` - Top customers
  - `GET /customer-insights/by_segment/?segment=vip` - Filter by segment
  - `GET/POST /performance-metrics/` - Manage performance metrics
  - `GET /performance-metrics/by_type/?metric_type=revenue` - Filter by type

### SOAP API Endpoints

Each app provides SOAP endpoints at `/{app}/soap/`:
- `/products/soap/` - Product SOAP services
- `/orders/soap/` - Order SOAP services
- `/logistics/soap/` - Logistics SOAP services
- `/finance/soap/` - Finance SOAP services
- `/promotions/soap/` - Promotions SOAP services
- `/analytics/soap/` - Analytics SOAP services

Access WSDL at `/{app}/soap/?wsdl` (e.g., `/products/soap/?wsdl`)

## Project Structure

```
messo-seller-center/
├── manage.py
├── requirements.txt
├── README.md
├── messo_seller_center/          # Main project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── products/                      # Products app
│   ├── models.py                 # Product, ProductImage, Inventory
│   ├── serializers.py            # REST serializers
│   ├── views.py                  # REST API views
│   ├── soap_services.py          # SOAP services
│   └── urls.py                   # URL routing
├── orders/                        # Orders app
│   ├── models.py                 # Order, OrderItem, OrderTracking
│   ├── serializers.py
│   ├── views.py
│   ├── soap_services.py
│   └── urls.py
├── logistics/                     # Logistics app
│   ├── models.py                 # Shipment, ShipmentEvent, Warehouse
│   ├── serializers.py
│   ├── views.py
│   ├── soap_services.py
│   └── urls.py
├── finance/                       # Finance app
│   ├── models.py                 # Payment, Invoice, Settlement
│   ├── serializers.py
│   ├── views.py
│   ├── soap_services.py
│   └── urls.py
├── promotions/                    # Promotions app
│   ├── models.py                 # Campaign, Discount, Voucher, ProductPromotion
│   ├── serializers.py
│   ├── views.py
│   ├── soap_services.py
│   └── urls.py
└── analytics/                     # Analytics app
    ├── models.py                 # SalesReport, ProductAnalytics, CustomerInsight, PerformanceMetric
    ├── serializers.py
    ├── views.py
    ├── soap_services.py
    └── urls.py
```

## Technology Stack

- **Django 6.0** - Web framework
- **Django REST Framework 3.16** - REST API framework
- **Spyne 2.14** - SOAP web services framework
- **lxml** - XML processing
- **django-cors-headers** - CORS support

## Admin Panel

Access the Django admin panel at `http://127.0.0.1:8000/admin/` to manage all models through a web interface.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is open source and available under the MIT License.
