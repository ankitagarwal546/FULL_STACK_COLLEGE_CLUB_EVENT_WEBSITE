#!/bin/bash

echo "🚀 Setting up SAC Django Project..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "✅ Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "🔨 Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "✨ Setup complete! ✨"
echo ""
echo "📝 Next steps:"
echo "1. Create a superuser account:"
echo "   python manage.py createsuperuser"
echo ""
echo "2. Start the development server:"
echo "   python manage.py runserver"
echo ""
echo "3. Access the website at: http://127.0.0.1:8000/"
echo "4. Access admin panel at: http://127.0.0.1:8000/admin/"
echo ""
