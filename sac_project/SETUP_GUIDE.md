# SAC IIIT Naya Raipur - Quick Start Guide

## Quick Setup (5 minutes)

### 1. Navigate to project directory
```bash
cd /Users/ankitagarwal546/Desktop/frontend/COLLEGE-CLUB-WEBSITE/sac_project
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create admin user
```bash
python manage.py createsuperuser
```
Enter your desired username, email, and password.

### 6. Run the server
```bash
python manage.py runserver
```

## Access the Application

- **Website**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## First Steps in Admin Panel

1. **Login** to admin panel with your superuser credentials

2. **Add a Club**:
   - Go to Clubs → Add Club
   - Fill in name, description, status, spots
   - Upload an image
   - Add Google Form link (optional)
   - Save

3. **Add an Event**:
   - Go to Events → Add Event
   - Fill in all details
   - Set status to "Upcoming"
   - Upload event image
   - Save

4. **Add Gallery Photos**:
   - Go to Gallery Photos → Add Gallery Photo
   - Upload photo
   - Add title
   - Select section (Workshops/Events/Projects/Social)
   - Save

## URLs Reference

| Page | URL |
|------|-----|
| Home | http://127.0.0.1:8000/ |
| Clubs | http://127.0.0.1:8000/clubs/ |
| Events | http://127.0.0.1:8000/events/ |
| Gallery | http://127.0.0.1:8000/gallery/ |
| Members | http://127.0.0.1:8000/members/ |
| Contact | http://127.0.0.1:8000/contact/ |
| Admin | http://127.0.0.1:8000/admin/ |

## Common Commands

```bash
# Start server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files (for production)
python manage.py collectstatic

# Check for issues
python manage.py check
```

## Tips

- Always activate the virtual environment before running commands
- The SAC logo (sac.png) is in `static/images/` directory
- Uploaded images go to `media/` directory
- CSS is in `static/css/style.css`
- JavaScript is in `static/js/script.js`

## Need Help?

Check the full README.md for detailed information.
