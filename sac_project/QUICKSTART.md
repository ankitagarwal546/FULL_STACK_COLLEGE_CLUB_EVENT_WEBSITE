# Quick Start Guide - SAC Website

## 🚀 Fast Setup (5 minutes)

### Step 1: Navigate to Project Directory
```bash
cd /Users/ankitagarwal546/Desktop/frontend/COLLEGE-CLUB-WEBSITE/sac_project
```

### Step 2: Run Setup Script (Recommended)
```bash
./setup.sh
```

**OR Manual Setup:**

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput
```

### Step 3: Create Admin Account
```bash
python manage.py createsuperuser
```
- Username: `admin` (or your choice)
- Email: your-email@example.com
- Password: (choose a strong password)

### Step 4: Start Server
```bash
python manage.py runserver
```

### Step 5: Access Website
- **Website**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

---

## 📋 First Time Admin Tasks

### Add Your First Club
1. Login to admin: http://127.0.0.1:8000/admin/
2. Click **Clubs** → **Add Club**
3. Fill in:
   - Name: "AI/ML Club"
   - Description: "Learn AI and Machine Learning"
   - Registration Status: "Registration Open"
   - Spots: 50
   - Image: Upload an image
   - Google Form Link: https://forms.google.com/... (optional)
4. Click **Save**

### Add Your First Event
1. Click **Events** → **Add Event**
2. Fill in:
   - Name: "Python Workshop"
   - Description: "Introduction to Python programming"
   - Timing: "2:00 PM - 5:00 PM"
   - Location: "Room 138"
   - Additional Info: "100 spots available"
   - Date: Choose a future date
   - Status: "Upcoming"
   - Image: Upload an image
3. Click **Save**

### Add Gallery Photos
1. Click **Gallery Photos** → **Add Gallery Photo**
2. Fill in:
   - Title: "AI Workshop Session"
   - Section: "Workshops"
   - Image: Upload a photo
3. Click **Save**
4. Repeat for different sections (Events, Projects, Social)

---

## 🎯 Key Features to Test

### Clubs Page
- Visit: http://127.0.0.1:8000/clubs/
- Check if clubs display correctly
- Verify "Apply Now" button only appears when Google Form link exists

### Events Page
- Visit: http://127.0.0.1:8000/events/
- Switch between "Upcoming" and "Past" tabs
- Verify events appear in correct sections

### Gallery Page
- Visit: http://127.0.0.1:8000/gallery/
- Click filter buttons (All Photos, Workshops, Events, Projects, Social)
- Verify filtering works correctly

---

## 🛠️ Useful Commands

### Database Management
```bash
# Create new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset database (if needed)
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Static Files
```bash
# Collect static files
python manage.py collectstatic --noinput
```

### Server
```bash
# Start development server
python manage.py runserver

# Start on different port
python manage.py runserver 8080

# Start on all interfaces (accessible from network)
python manage.py runserver 0.0.0.0:8000
```

### Admin Management
```bash
# Create superuser
python manage.py createsuperuser

# Change password
python manage.py changepassword username
```

---

## 📱 URLs Overview

| Page | URL | Description |
|------|-----|-------------|
| Home | http://127.0.0.1:8000/ | Landing page |
| Clubs | http://127.0.0.1:8000/clubs/ | All clubs with Apply Now buttons |
| Events | http://127.0.0.1:8000/events/ | Upcoming & Past events |
| Gallery | http://127.0.0.1:8000/gallery/ | Photo gallery with filtering |
| Members | http://127.0.0.1:8000/members/ | Team members page |
| Contact | http://127.0.0.1:8000/contact/ | Contact information |
| Admin | http://127.0.0.1:8000/admin/ | Admin dashboard |

---

## 🔥 Pro Tips

1. **Media Files**: All uploaded images are stored in `media/` directory
2. **Static Files**: CSS/JS are in `static/` directory
3. **Templates**: HTML templates are in `templates/` directory
4. **Admin Customization**: Check `admin.py` files in each app
5. **URL Patterns**: Check `urls.py` files for routing

---

## ❓ Common Issues

### Images not loading?
- Make sure `python manage.py collectstatic` was run
- Check that images exist in `media/` directory

### Admin not accessible?
- Make sure you created a superuser: `python manage.py createsuperuser`
- Check you're using the correct credentials

### CSS not applying?
- Run `python manage.py collectstatic --noinput`
- Hard refresh browser (Ctrl+Shift+R or Cmd+Shift+R)

---

## 📧 Support

For questions: sac@iiitnr.edu.in

**Happy coding! 🎉**
