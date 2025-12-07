from django.core.management.base import BaseCommand
from documentation.models import APIEndpoint, APIChangeLog, SetupGuide, FAQ


class Command(BaseCommand):
    help = 'Populate initial documentation data with API endpoints and guides'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Populating documentation data...'))
        
        # Clear existing data
        APIEndpoint.objects.all().delete()
        APIChangeLog.objects.all().delete()
        SetupGuide.objects.all().delete()
        FAQ.objects.all().delete()
        
        # Create sample API endpoints
        endpoints_data = [
            # Products endpoints
            {'app': 'products', 'api_type': 'rest', 'name': 'List Products', 'url_path': '/products/api/products/', 'http_method': 'GET', 'description': 'Retrieve a list of all products'},
            {'app': 'products', 'api_type': 'rest', 'name': 'Create Product', 'url_path': '/products/api/products/', 'http_method': 'POST', 'description': 'Create a new product'},
            {'app': 'products', 'api_type': 'rest', 'name': 'Get Product', 'url_path': '/products/api/products/{id}/', 'http_method': 'GET', 'description': 'Retrieve a specific product by ID'},
            {'app': 'products', 'api_type': 'soap', 'name': 'get_product', 'url_path': '/products/soap/', 'description': 'SOAP operation to get product details'},
            {'app': 'products', 'api_type': 'soap', 'name': 'list_products', 'url_path': '/products/soap/', 'description': 'SOAP operation to list all products'},
            
            # Orders endpoints
            {'app': 'orders', 'api_type': 'rest', 'name': 'List Orders', 'url_path': '/orders/api/orders/', 'http_method': 'GET', 'description': 'Retrieve a list of all orders'},
            {'app': 'orders', 'api_type': 'rest', 'name': 'Create Order', 'url_path': '/orders/api/orders/', 'http_method': 'POST', 'description': 'Create a new order'},
            {'app': 'orders', 'api_type': 'rest', 'name': 'Cancel Order', 'url_path': '/orders/api/orders/{id}/cancel/', 'http_method': 'POST', 'description': 'Cancel an existing order'},
            {'app': 'orders', 'api_type': 'soap', 'name': 'get_order', 'url_path': '/orders/soap/', 'description': 'SOAP operation to get order details'},
            
            # Logistics endpoints
            {'app': 'logistics', 'api_type': 'rest', 'name': 'List Shipments', 'url_path': '/logistics/api/shipments/', 'http_method': 'GET', 'description': 'Retrieve a list of all shipments'},
            {'app': 'logistics', 'api_type': 'rest', 'name': 'Track Shipment', 'url_path': '/logistics/api/shipments/{id}/track/', 'http_method': 'GET', 'description': 'Track a shipment with events'},
            {'app': 'logistics', 'api_type': 'soap', 'name': 'track_shipment', 'url_path': '/logistics/soap/', 'description': 'SOAP operation to track shipment'},
            
            # Finance endpoints
            {'app': 'finance', 'api_type': 'rest', 'name': 'List Payments', 'url_path': '/finance/api/payments/', 'http_method': 'GET', 'description': 'Retrieve a list of all payments'},
            {'app': 'finance', 'api_type': 'rest', 'name': 'Process Payment', 'url_path': '/finance/api/payments/{id}/process/', 'http_method': 'POST', 'description': 'Process a pending payment'},
            {'app': 'finance', 'api_type': 'soap', 'name': 'get_payment', 'url_path': '/finance/soap/', 'description': 'SOAP operation to get payment details'},
            
            # Promotions endpoints
            {'app': 'promotions', 'api_type': 'rest', 'name': 'List Campaigns', 'url_path': '/promotions/api/campaigns/', 'http_method': 'GET', 'description': 'Retrieve a list of all marketing campaigns'},
            {'app': 'promotions', 'api_type': 'rest', 'name': 'Validate Discount', 'url_path': '/promotions/api/discounts/{id}/validate_code/', 'http_method': 'POST', 'description': 'Validate a discount code'},
            {'app': 'promotions', 'api_type': 'soap', 'name': 'validate_discount_code', 'url_path': '/promotions/soap/', 'description': 'SOAP operation to validate discount code'},
            
            # Analytics endpoints
            {'app': 'analytics', 'api_type': 'rest', 'name': 'List Sales Reports', 'url_path': '/analytics/api/sales-reports/', 'http_method': 'GET', 'description': 'Retrieve sales reports'},
            {'app': 'analytics', 'api_type': 'rest', 'name': 'Top Products', 'url_path': '/analytics/api/product-analytics/top_products/', 'http_method': 'GET', 'description': 'Get top performing products'},
            {'app': 'analytics', 'api_type': 'soap', 'name': 'get_top_products', 'url_path': '/analytics/soap/', 'description': 'SOAP operation to get top products'},
        ]
        
        for endpoint_data in endpoints_data:
            APIEndpoint.objects.create(**endpoint_data)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(endpoints_data)} API endpoints'))
        
        # Create initial changelog entry
        APIChangeLog.objects.create(
            change_type='created',
            version='1.0.0',
            description='Initial release of Messo Seller Center APIs with 96 endpoints across 6 apps',
            changed_by='System'
        )
        
        self.stdout.write(self.style.SUCCESS('Created initial changelog entry'))
        
        # Create setup guides
        setup_guides = [
            {
                'title': 'Quick Start Guide',
                'guide_type': 'installation',
                'order': 1,
                'content': '''
## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

3. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

4. **Start Server**
   ```bash
   python manage.py runserver
   ```

5. **Access Documentation**
   Visit http://localhost:8000/docs/
'''
            },
            {
                'title': 'Environment Configuration',
                'guide_type': 'configuration',
                'order': 2,
                'content': '''
## Configuration

Create a `.env` file with these variables:

- `SECRET_KEY` - Django secret key
- `DEBUG` - Debug mode (True/False)
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts
- `DATABASE_URL` - Database connection string
'''
            },
        ]
        
        for guide_data in setup_guides:
            SetupGuide.objects.create(**guide_data)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(setup_guides)} setup guides'))
        
        # Create FAQs
        faqs = [
            {
                'question': 'How do I access the REST API documentation?',
                'answer': 'Visit /docs/api/ or use the browsable API at each endpoint URL (e.g., /products/api/products/)',
                'category': 'API Access',
                'order': 1
            },
            {
                'question': 'Where can I find WSDL for SOAP services?',
                'answer': 'WSDL is available at /app/soap/wsdl/ for each app (e.g., /products/soap/wsdl/)',
                'category': 'SOAP',
                'order': 2
            },
            {
                'question': 'How do I authenticate API requests?',
                'answer': 'Currently, the API is open for development. For production, implement token-based authentication using Django REST Framework tokens or JWT.',
                'category': 'Security',
                'order': 3
            },
            {
                'question': 'Can I test the APIs without writing code?',
                'answer': 'Yes! Use the browsable API for REST endpoints or tools like Postman/SoapUI for SOAP endpoints.',
                'category': 'Testing',
                'order': 4
            },
            {
                'question': 'How do I track API changes?',
                'answer': 'Visit /docs/changelog/ to see all API changes with version history.',
                'category': 'Documentation',
                'order': 5
            },
        ]
        
        for faq_data in faqs:
            FAQ.objects.create(**faq_data)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(faqs)} FAQs'))
        
        self.stdout.write(self.style.SUCCESS('✅ Documentation populated successfully!'))
