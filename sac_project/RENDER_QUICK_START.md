# 🚀 Render Deployment - Quick Start

## ✅ Files Created for Render:

1. **`build.sh`** - Build script (installs dependencies, runs migrations, collects static files)
2. **`render.yaml`** - Render configuration (optional, makes setup easier)
3. **`RENDER_DEPLOYMENT_GUIDE.md`** - Complete step-by-step guide

---

## 🎯 Quick Deploy Steps:

### 1. Push to GitHub
```bash
cd /Users/ankitagarwal546/Desktop/FULL_STACK_COLLEGE_CLUB_EVENT_WEBSITE/sac_project

git add .
git commit -m "Add Render deployment configuration"
git push origin main
```

### 2. Create Render Account
- Go to https://render.com
- Sign up with GitHub (FREE)

### 3. Create Web Service
1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repo: `FULL_STACK_COLLEGE_CLUB_EVENT_WEBSITE`
3. Configure:
   - **Root Directory:** `sac_project` ⚠️
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn sac_project.wsgi:application`
   - **Plan:** Free

### 4. Add Environment Variables
```
SECRET_KEY = 2=gutdd^a%bz4#ch(f3%a@&171v$l#sesexrss)zrksv2aqzh5
DEBUG = False
PYTHON_VERSION = 3.13.7
ALLOWED_HOSTS = .onrender.com
WEB_CONCURRENCY = 4
```

### 5. Create PostgreSQL Database
1. Click **"New +"** → **"PostgreSQL"**
2. Plan: **Free**
3. Copy **Internal Database URL**

### 6. Add DATABASE_URL
Go back to your web service → Environment → Add:
```
DATABASE_URL = <paste-internal-database-url>
```

### 7. Deploy!
Click **"Create Web Service"** and wait 3-5 minutes.

### 8. Create Admin User
After deployment, go to **Shell** tab:
```bash
python manage.py createsuperuser
```

---

## 🌐 Your Website Will Be Live At:
- **Site:** `https://sac-website.onrender.com`
- **Admin:** `https://sac-website.onrender.com/admin`

---

## 💡 Key Differences from Railway:

| Feature | Railway | Render |
|---------|---------|--------|
| **Free Tier** | $5 credit/month | Unlimited (sleeps after 15 min) |
| **Database** | PostgreSQL included | Separate PostgreSQL service |
| **Sleep Time** | Never sleeps (on paid) | Sleeps on free tier |
| **Wake Time** | N/A | ~30 seconds |
| **Setup** | Automatic | Manual config needed |

---

## ⚠️ Important: Free Tier Notes

1. **Web service sleeps after 15 min** of inactivity
2. **Database expires after 90 days** (upgrade to keep data permanently)
3. **First request after sleep takes ~30 seconds** to wake up

---

## 📚 Full Documentation
See **`RENDER_DEPLOYMENT_GUIDE.md`** for detailed instructions with troubleshooting.

---

**Render is easier to set up and perfect for student projects! Deploy now! 🚀**
