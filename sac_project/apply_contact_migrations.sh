# Run this script after stopping the server to create and apply migrations
#
# To use:
# 1. Stop the development server (Ctrl+C)
# 2. Run: source venv/bin/activate && python manage.py makemigrations core
# 3. Run: python manage.py migrate
# 4. Restart the server: python manage.py runserver

echo "Creating migrations for ContactMessage model..."
python manage.py makemigrations core

echo "Applying migrations..."
python manage.py migrate

echo "Done! You can now restart the server."
