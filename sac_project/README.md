# SAC Website - Django Backend

A complete Django-based backend for the Student Activity Council (SAC) website at IIIT Naya Raipur.

## Features

### 🔐 Authentication
- Django admin login with username/password
- Only admin users can access dashboard features

### 🧩 Admin Dashboard Features

#### 1️⃣ Clubs Management
- Add/edit/delete clubs from Django admin
- Each club has: name, description, registration status, spots, image, and Google Form link
- "Apply Now" button only appears if a Google Form link is provided
- Admin can easily attach/update Google Form links

#### 2️⃣ Gallery Management
- Add photos to different sections: workshops, events, projects, social
- Delete photos from the admin panel
- Frontend automatically filters photos by section
- "All Photos" option to display all gallery items

#### 3️⃣ Events Management
- Add new events with full details (name, description, timing, location, date, image)
- Mark events as "upcoming" or "past"
- Events automatically display in the correct section
- Admin actions to bulk mark events as past/upcoming
- Edit or delete any event

## 📦 Technology Stack

- **Backend**: Django >= 4.2
- **Database**: SQLite (default, can be changed to PostgreSQL/MySQL)
- **Image Processing**: Pillow
- **Frontend**: HTML, CSS, JavaScript (integrated with Django templates)

## 🚀 Setup Instructions

### 1. Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### 2. Installation

```bash
# Navigate to the project directory
cd sac_project

# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Database Setup

```bash
# Run migrations to create database tables
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser (Admin Account)

```bash
# Create an admin account
python manage.py createsuperuser

# Follow the prompts:
# - Username: (your choice, e.g., admin)
# - Email: (your email)
# - Password: (choose a strong password)
# - Password (again): (confirm password)
```

### 5. Collect Static Files

```bash
# Collect all static files
python manage.py collectstatic --noinput
```

### 6. Run the Development Server

```bash
# Start the Django development server
python manage.py runserver

# The website will be available at: http://127.0.0.1:8000/
# Admin panel: http://127.0.0.1:8000/admin/
```

## 📂 Project Structure

```
sac_project/
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── db.sqlite3                # SQLite database (created after migrations)
│
├── sac_project/              # Main project settings
│   ├── __init__.py
│   ├── settings.py           # Django settings
│   ├── urls.py               # Main URL configuration
│   ├── asgi.py
│   └── wsgi.py
│
├── clubs/                    # Clubs app
│   ├── models.py            # Club model
│   ├── admin.py             # Club admin configuration
│   ├── views.py             # Club views
│   └── urls.py              # Club URLs
│
├── events/                   # Events app
│   ├── models.py            # Event model
│   ├── admin.py             # Event admin configuration
│   ├── views.py             # Event views
│   └── urls.py              # Event URLs
│
├── gallery/                  # Gallery app
│   ├── models.py            # GalleryPhoto model
│   ├── admin.py             # Gallery admin configuration
│   ├── views.py             # Gallery views
│   └── urls.py              # Gallery URLs
│
├── core/                     # Core app (home, contact, members)
│   ├── views.py             # Core views
│   └── urls.py              # Core URLs
│
├── templates/                # Django templates
│   ├── base.html            # Base template with navbar/footer
│   ├── core/
│   │   ├── index.html       # Home page
│   │   ├── contact.html     # Contact page
│   │   └── members.html     # Members page
│   ├── clubs/
│   │   └── about.html       # Clubs page
│   ├── events/
│   │   └── events.html      # Events page
│   └── gallery/
│       └── gallery.html     # Gallery page
│
├── static/                   # Static files
│   ├── css/
│   │   └── style.css        # Main stylesheet
│   ├── js/
│   │   └── script.js        # JavaScript file
│   └── images/              # Static images
│
└── media/                    # User-uploaded media files
    ├── clubs/               # Club images
    ├── events/              # Event images
    └── gallery/             # Gallery photos
```

## 🎯 Usage Guide

### Admin Panel Access

1. Start the development server (if not already running)
2. Navigate to: http://127.0.0.1:8000/admin/
3. Login with your superuser credentials
4. You'll see the admin dashboard with:
   - Clubs
   - Events
   - Gallery Photos
   - Authentication and Authorization (Users, Groups)

### Managing Clubs

1. Go to **Admin Panel** → **Clubs** → **Add Club**
2. Fill in the form:
   - **Name**: Club name (e.g., "AIML Club")
   - **Description**: Detailed description
   - **Registration Status**: Choose "Open" or "Closed"
   - **Spots**: Number of available spots
   - **Image**: Upload club image
   - **Google Form Link**: Paste Google Form URL (optional)
     - If provided, "Apply Now" button will appear on frontend
     - If empty, "Apply Now" button will be hidden
3. Click **Save**

### Managing Events

1. Go to **Admin Panel** → **Events** → **Add Event**
2. Fill in the form:
   - **Name**: Event name
   - **Description**: Event details
   - **Timing**: Time (e.g., "2:00 PM - 5:00 PM")
   - **Location**: Venue (e.g., "Room no.138")
   - **Additional Info**: Extra details (e.g., "100 spots available")
   - **Date**: Event date
   - **Status**: Choose "Upcoming" or "Past"
   - **Image**: Upload event image
3. Click **Save**

**Bulk Actions:**
- Select multiple events
- Choose "Mark selected events as Past" or "Mark selected events as Upcoming"
- Click "Go" to apply the action

### Managing Gallery

1. Go to **Admin Panel** → **Gallery Photos** → **Add Gallery Photo**
2. Fill in the form:
   - **Title**: Photo title
   - **Section**: Choose from:
     - Workshops
     - Events
     - Projects
     - Social
   - **Image**: Upload photo
3. Click **Save**

**Frontend Filtering:**
- Visitors can filter photos by clicking section buttons
- "All Photos" shows all images regardless of section

## 🌐 Frontend Pages

- **Home**: http://127.0.0.1:8000/
- **Clubs**: http://127.0.0.1:8000/clubs/
- **Events**: http://127.0.0.1:8000/events/
- **Gallery**: http://127.0.0.1:8000/gallery/
- **Members**: http://127.0.0.1:8000/members/
- **Contact**: http://127.0.0.1:8000/contact/

## 🔧 Configuration

### Media Files
Media files (uploaded images) are stored in the `media/` directory:
- `MEDIA_URL = '/media/'`
- `MEDIA_ROOT = BASE_DIR / 'media'`

### Static Files
Static files (CSS, JS, images) are stored in the `static/` directory:
- `STATIC_URL = '/static/'`
- `STATIC_ROOT = BASE_DIR / 'staticfiles'`

### Database
The project uses SQLite by default. To use PostgreSQL or MySQL, update the `DATABASES` setting in `sac_project/settings.py`.

## 🎨 Customization

### Changing Secret Key
Before deploying to production, change the `SECRET_KEY` in `settings.py`:
```python
SECRET_KEY = 'your-new-secret-key-here'
```

### Debug Mode
For production, set `DEBUG = False` in `settings.py` and configure `ALLOWED_HOSTS`.

## 📝 Models Reference

### Club Model
```python
- name: CharField (max 200 chars)
- description: TextField
- registration_status: CharField (choices: 'open', 'closed')
- spots: IntegerField
- image: ImageField (upload to 'clubs/')
- google_form_link: URLField (optional)
- created_at: DateTimeField (auto)
- updated_at: DateTimeField (auto)
```

### Event Model
```python
- name: CharField (max 200 chars)
- description: TextField
- timing: CharField (max 100 chars)
- location: CharField (max 200 chars)
- additional_info: TextField (optional)
- date: DateField
- status: CharField (choices: 'upcoming', 'past')
- image: ImageField (upload to 'events/')
- created_at: DateTimeField (auto)
- updated_at: DateTimeField (auto)
```

### GalleryPhoto Model
```python
- title: CharField (max 200 chars)
- image: ImageField (upload to 'gallery/')
- section: CharField (choices: 'workshops', 'events', 'projects', 'social')
- created_at: DateTimeField (auto)
- updated_at: DateTimeField (auto)
```

## 🐛 Troubleshooting

### Issue: Static files not loading
```bash
python manage.py collectstatic --noinput
```

### Issue: Images not displaying
- Ensure `MEDIA_URL` and `MEDIA_ROOT` are configured in `settings.py`
- Check that media files exist in the `media/` directory
- In development, Django serves media files automatically

### Issue: Database errors
```bash
# Delete the database and migrations
rm db.sqlite3
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

# Recreate migrations and database
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## 📧 Contact

For issues or questions, contact: sac@iiitnr.edu.in

## 📄 License

Made with ❤️ By INNOVENTURES

---

**Note**: Remember to keep your `SECRET_KEY` secure and never commit it to version control in production!
