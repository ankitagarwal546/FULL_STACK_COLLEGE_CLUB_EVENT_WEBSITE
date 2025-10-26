# SAC Website - Command Reference

## Essential Commands

### Setup Commands
```bash
# Navigate to project
cd /Users/ankitagarwal546/Desktop/frontend/COLLEGE-CLUB-WEBSITE/sac_project

# Create virtual environment
python3 -m venv venv

# Activate virtual environment (macOS/Linux)
source venv/bin/activate

# Deactivate virtual environment
deactivate

# Install dependencies
pip install -r requirements.txt

# Upgrade pip
pip install --upgrade pip
```

### Database Commands
```bash
# Create migrations (after model changes)
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migrations
python manage.py showmigrations

# Rollback migrations
python manage.py migrate app_name migration_name
```

### Server Commands
```bash
# Start development server
python manage.py runserver

# Start on specific port
python manage.py runserver 8080

# Start on all interfaces
python manage.py runserver 0.0.0.0:8000
```

### Admin Commands
```bash
# Create superuser
python manage.py createsuperuser

# Change password
python manage.py changepassword username
```

### Static Files Commands
```bash
# Collect static files (for production)
python manage.py collectstatic

# Clear collected static files
python manage.py collectstatic --clear
```

### Database Shell Commands
```bash
# Open Django shell
python manage.py shell

# Example: Query clubs
from clubs.models import Club
Club.objects.all()

# Example: Create a club
club = Club.objects.create(
    name="Test Club",
    description="Test description",
    registration_status="open",
    spots=50
)
```

### Database Management
```bash
# Backup database
cp db.sqlite3 db.sqlite3.backup

# Restore database
cp db.sqlite3.backup db.sqlite3

# Clear database (careful!)
rm db.sqlite3
python manage.py migrate
```

### Development Helpers
```bash
# Check for issues
python manage.py check

# Check deployment readiness
python manage.py check --deploy

# Show project settings
python manage.py diffsettings

# Test a specific app
python manage.py test app_name
```

### Useful pip Commands
```bash
# List installed packages
pip list

# Show package info
pip show django

# Freeze requirements
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Upgrade a package
pip install --upgrade django
```

## Quick Workflows

### Starting Development
```bash
cd /Users/ankitagarwal546/Desktop/frontend/COLLEGE-CLUB-WEBSITE/sac_project
source venv/bin/activate
python manage.py runserver
```

### After Model Changes
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Adding New Content
1. Navigate to http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. Add/edit content
4. View changes on frontend

### Troubleshooting
```bash
# Clear Python cache
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name "*.pyc" -delete

# Reset migrations (careful!)
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
```

## URLs Reference

| Description | URL |
|------------|-----|
| Homepage | http://127.0.0.1:8000/ |
| Clubs | http://127.0.0.1:8000/clubs/ |
| Events | http://127.0.0.1:8000/events/ |
| Gallery | http://127.0.0.1:8000/gallery/ |
| Members | http://127.0.0.1:8000/members/ |
| Contact | http://127.0.0.1:8000/contact/ |
| Admin Panel | http://127.0.0.1:8000/admin/ |

## File Locations

| Item | Path |
|------|------|
| Settings | sac_project/settings.py |
| Main URLs | sac_project/urls.py |
| Templates | templates/ |
| Static Files | static/ |
| Media Files | media/ |
| Models | */models.py |
| Admin Config | */admin.py |
| Views | */views.py |

## Tips

- Always activate virtual environment before running commands
- Run `python manage.py check` to verify configuration
- Use `python manage.py shell` for quick database queries
- Backup db.sqlite3 before major changes
- Check admin panel after adding content
- Use `git status` to track changes

## Common Issues & Solutions

### Port already in use
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9
```

### Permission denied on setup.sh
```bash
chmod +x setup.sh
```

### Module not found error
```bash
pip install -r requirements.txt
```

### Static files not loading
```bash
python manage.py collectstatic --noinput
```

---

Keep this file handy for quick reference!
