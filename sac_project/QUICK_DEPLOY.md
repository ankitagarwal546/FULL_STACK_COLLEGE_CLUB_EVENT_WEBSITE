# 🚀 Railway Deployment - Quick Start

## Files Created for Deployment:

✅ **Procfile** - Tells Railway how to run your app
✅ **runtime.txt** - Specifies Python version
✅ **railway.json** - Railway configuration
✅ **nixpacks.toml** - Build configuration
✅ **.env** - Local environment variables (not pushed to GitHub)
✅ **.env.example** - Template for environment variables
✅ **Updated requirements.txt** - Added production dependencies
✅ **Updated settings.py** - Production-ready settings

## 🎯 Next Steps:

### 1. Push to GitHub
```bash
cd /Users/ankitagarwal546/Desktop/FULL_STACK_COLLEGE_CLUB_EVENT_WEBSITE/sac_project

git add .
git commit -m "Add Railway deployment configuration"
git push origin main
```

### 2. Deploy on Railway
1. Go to https://railway.app
2. Sign in with GitHub
3. Click "Start a New Project"
4. Select "Deploy from GitHub repo"
5. Choose your repository
6. Add PostgreSQL database (click "+ New" → "Database" → "PostgreSQL")

### 3. Set Environment Variables in Railway
```
SECRET_KEY=<generate-using-command-below>
DEBUG=False
ALLOWED_HOSTS=<your-railway-domain>
```

Generate SECRET_KEY:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 4. Create Admin User (After Deployment)
In Railway terminal:
```bash
python manage.py createsuperuser
```

## 📚 Full Guide
See **RAILWAY_DEPLOYMENT_GUIDE.md** for detailed step-by-step instructions.

## 💡 Important Notes:
- Your local dev still uses SQLite
- Production on Railway uses PostgreSQL (automatically configured)
- Media files will be stored on Railway's disk
- Free tier: $5/month credit (enough for small projects)

## ✅ What Changed:
- **settings.py**: Now supports both local (SQLite) and production (PostgreSQL)
- **Static files**: Handled by WhiteNoise (no separate server needed)
- **Security**: Production security settings enabled when DEBUG=False
- **Database**: Automatically switches based on environment

Your local development is still working normally! 🎉
