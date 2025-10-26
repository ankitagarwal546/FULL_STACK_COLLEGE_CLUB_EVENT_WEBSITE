# Setup Guide for New Machine

Follow these steps to run the SAC website on a new laptop after copying the project folder.

## Prerequisites
- Python 3.8 or higher installed
- pip (Python package installer)

## Setup Steps

### 1. Navigate to the project directory
```bash
cd /path/to/COLLEGE-CLUB-WEBSITE/sac_project
```

### 2. Create a virtual environment
```bash
# On macOS/Linux
python3 -m venv venv

# On Windows
python -m venv venv
```

### 3. Activate the virtual environment
```bash
# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### 4. Install required packages
```bash
pip install -r requirements.txt
```

### 5. Apply database migrations
```bash
python manage.py migrate
```

### 6. Create a superuser (admin account)
```bash
python manage.py createsuperuser
```
Follow the prompts to set:
- Username
- Email (optional)
- Password

### 7. Collect static files (optional, for production)
```bash
python manage.py collectstatic
```

### 8. Run the development server
```bash
python manage.py runserver
```

### 9. Access the website
- **Homepage**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

---

## Quick Start (If Database Already Exists)

If you're copying the project WITH the database file (`db.sqlite3`), you can skip the migration and superuser creation:

```bash
# 1. Navigate to project
cd /path/to/COLLEGE-CLUB-WEBSITE/sac_project

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows

# 4. Install packages
pip install -r requirements.txt

# 5. Run server
python manage.py runserver
```

**Existing Admin Credentials** (if database is copied):
- Username: `admin`
- Password: `admin123`

---

## Troubleshooting

### Issue: "python: command not found"
**Solution**: Use `python3` instead of `python`:
```bash
python3 -m venv venv
python3 manage.py runserver
```

### Issue: "No module named django"
**Solution**: Make sure virtual environment is activated and packages are installed:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Issue: "Port already in use"
**Solution**: Use a different port:
```bash
python manage.py runserver 8080
```

### Issue: Missing media files
**Solution**: Make sure the `media/` folder is copied with the project, or images won't display.

---

## What to Copy to New Machine

### Essential Files/Folders:
✅ `manage.py`
✅ `requirements.txt`
✅ `db.sqlite3` (database - contains all your data)
✅ `sac_project/` (settings folder)
✅ `clubs/`, `events/`, `gallery/`, `core/` (app folders)
✅ `templates/` (HTML templates)
✅ `static/` (CSS, JS, images)
✅ `media/` (uploaded images)

### Optional (Can Skip):
❌ `venv/` (virtual environment - recreate on new machine)
❌ `__pycache__/` folders (Python cache - auto-generated)
❌ `*.pyc` files (compiled Python - auto-generated)
❌ `staticfiles/` (collected static files - run collectstatic if needed)

---

## Notes

- Always activate the virtual environment before running any Django commands
- The database file (`db.sqlite3`) contains all your clubs, events, gallery photos, and admin users
- If you don't copy the database, you'll start with an empty database and need to create a new superuser
- Media files (uploaded images) are stored in the `media/` folder - copy this to preserve images
