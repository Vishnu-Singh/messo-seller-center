# Documentation App

The documentation app provides a comprehensive web-based documentation interface for the Messo Seller Center API project.

## Features

### 1. **Web-Based Documentation**
- Beautiful, responsive UI accessible at `/docs/`
- Navigation through different sections
- Search and filter capabilities
- Real-time API endpoint listing

### 2. **API Endpoint Tracking**
- Complete catalog of all REST and SOAP endpoints
- Organized by app (products, orders, logistics, etc.)
- Request/response examples
- HTTP method information

### 3. **Change Log Management**
- Version history tracking
- Breaking change indicators
- Filterable by version
- Endpoint-specific changes

### 4. **Setup Guides**
- Installation instructions
- Configuration guides
- Deployment documentation
- Troubleshooting tips

### 5. **FAQ Section**
- Categorized questions and answers
- Searchable content
- Common use cases

### 6. **REST API for Documentation**
- Query endpoints programmatically
- Get changelog data via API
- Filter by app or type

## Models

### APIEndpoint
Tracks all API endpoints in the system
- `name` - Endpoint name
- `app` - Django app (products, orders, etc.)
- `api_type` - REST or SOAP
- `url_path` - URL path
- `http_method` - HTTP method (for REST)
- `description` - Endpoint description
- `request_example` - Example request
- `response_example` - Example response

### APIChangeLog
Records changes to APIs
- `endpoint` - Related endpoint (optional)
- `change_type` - created/updated/deprecated/removed
- `version` - Version number
- `description` - Change description
- `breaking_change` - Boolean flag

### SetupGuide
Installation and configuration guides
- `title` - Guide title
- `guide_type` - installation/configuration/deployment/troubleshooting
- `content` - Guide content (Markdown supported)
- `order` - Display order

### FAQ
Frequently asked questions
- `question` - The question
- `answer` - The answer
- `category` - FAQ category
- `order` - Display order

## URLs

### Web Interface
- `/docs/` - Documentation home
- `/docs/setup/` - Setup and installation guide
- `/docs/api/` - API documentation listing
- `/docs/api/<id>/` - API endpoint detail
- `/docs/changelog/` - API change log
- `/docs/faq/` - FAQ page
- `/docs/testing/` - API testing guide
- `/docs/architecture/` - System architecture

### REST API
- `/docs/api-data/endpoints/` - Query API endpoints
- `/docs/api-data/endpoints/by_app/?app=products` - Filter by app
- `/docs/api-data/changelog/` - Query change logs

## Usage

### Accessing Documentation
1. Start the development server:
   ```bash
   python manage.py runserver
   ```

2. Visit `http://localhost:8000/docs/`

3. Browse through different sections using the navigation menu

### Populating Initial Data
Run the management command to populate sample documentation:
```bash
python manage.py populate_docs
```

This will create:
- Sample API endpoints for all apps
- Initial changelog entries
- Setup guides
- FAQ entries

### Managing Documentation
Use the Django admin interface at `/admin/`:
1. Login with superuser credentials
2. Navigate to "Documentation" section
3. Add/edit/delete API endpoints, changelogs, guides, and FAQs

### Adding New Endpoints
Through Django admin:
1. Go to **Documentation > API Endpoints**
2. Click "Add API Endpoint"
3. Fill in the details:
   - Name: Endpoint name
   - App: Select the Django app
   - API Type: REST or SOAP
   - URL Path: The endpoint URL
   - HTTP Method: GET, POST, etc. (for REST)
   - Description: What the endpoint does
   - Examples: Request and response examples

### Recording API Changes
1. Go to **Documentation > API Change Logs**
2. Click "Add API Change Log"
3. Fill in:
   - Endpoint: Select related endpoint (optional)
   - Change Type: created/updated/deprecated/removed
   - Version: Version number
   - Description: What changed
   - Breaking Change: Check if it breaks compatibility

## Templates

The app includes responsive HTML templates:
- `base.html` - Base template with navigation
- `home.html` - Documentation homepage
- `api_docs.html` - API listing page
- `api_detail.html` - Single endpoint details
- `setup_guide.html` - Setup instructions
- `changelog.html` - Change log listing
- `faq.html` - FAQ page
- `api_testing.html` - Testing guide
- `architecture.html` - Architecture documentation

## Customization

### Styling
Edit `/documentation/templates/documentation/base.html` to customize:
- Colors and theme
- Navigation menu
- Header and footer
- Page layout

### Adding New Sections
1. Create a new view in `views.py`
2. Add URL pattern in `urls.py`
3. Create template in `templates/documentation/`

### Markdown Support
The app supports Markdown rendering for:
- Setup guide content
- README.md display
- API_TESTING.md display
- ARCHITECTURE.md display

## Integration with Existing Docs

The documentation app automatically loads and displays:
- `README.md` - Project overview
- `API_TESTING.md` - Testing examples
- `ARCHITECTURE.md` - System architecture

These are rendered with Markdown formatting in the web interface.

## REST API Usage

Query endpoints programmatically:

```python
import requests

# Get all endpoints
response = requests.get('http://localhost:8000/docs/api-data/endpoints/')
endpoints = response.json()

# Get products endpoints only
response = requests.get('http://localhost:8000/docs/api-data/endpoints/by_app/?app=products')
products_endpoints = response.json()

# Get changelog
response = requests.get('http://localhost:8000/docs/api-data/changelog/')
changes = response.json()
```

## Admin Interface

The documentation models are registered with Django admin:
- **API Endpoints**: Manage API endpoint documentation
- **API Change Logs**: Track API version changes
- **Setup Guides**: Manage installation/configuration guides
- **FAQs**: Manage frequently asked questions

Each model has:
- List views with filters
- Search functionality
- Inline editing
- Bulk actions

## Benefits

1. **Centralized Documentation**: All docs in one place
2. **Always Up-to-Date**: Managed through admin interface
3. **Version Tracking**: Complete change history
4. **User-Friendly**: Web interface is easy to navigate
5. **Developer-Friendly**: REST API for programmatic access
6. **Searchable**: Find endpoints and information quickly
7. **Examples Included**: Request/response examples for each endpoint

## Future Enhancements

Potential improvements:
- Search functionality across all docs
- API playground for testing endpoints
- Automatic endpoint discovery
- OpenAPI/Swagger integration
- PDF export of documentation
- Multi-language support
- Code snippet generation
