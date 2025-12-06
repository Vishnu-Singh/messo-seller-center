#!/bin/bash
# Setup script for Messo Seller Center

echo "=== Messo Seller Center Setup ==="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"

# Install dependencies
echo ""
echo "Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies"
    exit 1
fi

echo "✓ Dependencies installed successfully"

# Run migrations
echo ""
echo "Running database migrations..."
python3 manage.py makemigrations
python3 manage.py migrate

if [ $? -ne 0 ]; then
    echo "Error: Failed to run migrations"
    exit 1
fi

echo "✓ Database migrations completed"

# Create superuser prompt
echo ""
echo "Would you like to create a superuser for the admin panel? (y/n)"
read -r create_superuser

if [ "$create_superuser" = "y" ] || [ "$create_superuser" = "Y" ]; then
    echo ""
    echo "Creating superuser..."
    python3 manage.py createsuperuser
fi

# Setup complete
echo ""
echo "==================================="
echo "✓ Setup completed successfully!"
echo "==================================="
echo ""
echo "To start the development server, run:"
echo "  python3 manage.py runserver"
echo ""
echo "Then visit:"
echo "  - API Root: http://localhost:8000/"
echo "  - Admin Panel: http://localhost:8000/admin/"
echo ""
echo "For API testing examples, see API_TESTING.md"
echo ""
