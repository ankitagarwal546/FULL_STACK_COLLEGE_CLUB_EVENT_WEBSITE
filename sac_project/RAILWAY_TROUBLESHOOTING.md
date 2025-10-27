# Railway Deployment Troubleshooting Guide

## ⚠️ Common Deployment Failures & Solutions

### 1. **Missing Environment Variables** ❌
**Error:** `DisallowedHost`, `SECRET_KEY error`, or `Database connection failed`

**Solution:** In Railway dashboard, go to your service → Variables tab and add:

```
SECRET_KEY=<your-generated-secret-key>
DEBUG=False
ALLOWED_HOSTS=<your-railway-domain>.up.railway.app
```

**Generate SECRET_KEY locally:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

### 2. **Database Not Added** ❌
**Error:** `Database connection error`, `no DATABASE_URL`

**Solution:**
1. In Railway project, click **"+ New"**
2. Select **"Database"** → **"PostgreSQL"**
3. Railway automatically creates `DATABASE_URL` variable
4. Make sure your Django service is linked to the database

---

### 3. **Build Fails - Missing Dependencies** ❌
**Error:** `ModuleNotFoundError`, `No module named 'gunicorn'`

**Solution:** Make sure `requirements.txt` has all dependencies:
```
Django>=4.2
Pillow
gunicorn
whitenoise
psycopg2-binary
dj-database-url
python-dotenv
```

---

### 4. **Wrong Start Command** ❌
**Error:** `Application failed to start`, `Port binding error`

**Solution:** Railway should use the command from `railway.json`:
```
python manage.py migrate && python manage.py collectstatic --noinput && gunicorn sac_project.wsgi
```

If Railway ignores `railway.json`, set custom start command in Railway settings.

---

### 5. **Port Configuration** ❌
**Error:** `Application timeout`, `Health check failed`

**Solution:** Railway auto-assigns a PORT. Update `settings.py` if needed (usually not required for Django).

---

### 6. **Static Files Not Loading** ❌
**Error:** CSS/JS not working on deployed site

**Solution:** Make sure:
1. WhiteNoise is in MIDDLEWARE (already done ✅)
2. `collectstatic` runs during deployment (in railway.json ✅)
3. `STATIC_ROOT` is set correctly (already done ✅)

---

### 7. **Migration Failures** ❌
**Error:** `django.db.utils.OperationalError`

**Solution:** 
- Migrations run automatically in railway.json
- If failing, check database connection
- Ensure PostgreSQL database is added and linked

---

### 8. **ALLOWED_HOSTS Error** ❌
**Error:** `DisallowedHost at /`

**Solution:** 
1. Get your Railway domain (e.g., `myapp-production-xxxx.up.railway.app`)
2. Add to Railway Variables:
   ```
   ALLOWED_HOSTS=myapp-production-xxxx.up.railway.app
   ```
3. Redeploy

---

## 🔍 How to Check Railway Logs:

1. Go to your Railway project
2. Click on your Django service
3. Click **"Deployments"** tab
4. Click on the latest deployment
5. View **"Build Logs"** and **"Deploy Logs"**

---

## 📋 Deployment Checklist:

- [ ] PostgreSQL database added to Railway project
- [ ] Environment variables set (SECRET_KEY, DEBUG=False, ALLOWED_HOSTS)
- [ ] Code pushed to GitHub
- [ ] Railway connected to GitHub repo
- [ ] Check build logs for errors
- [ ] Check deploy logs for errors
- [ ] Verify DATABASE_URL variable exists
- [ ] Check if migrations ran successfully

---

## 🆘 If Still Failing:

**Please provide:**
1. **Build logs** from Railway (copy the error messages)
2. **Deploy logs** from Railway
3. **Which step failed:** Build or Deploy?

**Common log locations in Railway:**
- Service → Deployments → Click deployment → View Logs

---

## ✅ Quick Fixes to Try:

### Fix 1: Redeploy
Sometimes Railway caches fail. Try:
1. In Railway → Service → Deployments
2. Click **"..."** menu on latest deployment
3. Click **"Redeploy"**

### Fix 2: Force Rebuild
1. Make a small change (add empty line to README)
2. Commit and push:
   ```bash
   git add .
   git commit -m "Trigger rebuild"
   git push origin main
   ```

### Fix 3: Check Python Version
Railway might be using wrong Python. Add to `runtime.txt`:
```
python-3.13.7
```
(Already created ✅)

---

## 🎯 Most Likely Issues:

Based on your setup, the most common issues are:

1. **Missing environment variables** (80% of failures)
2. **Database not connected** (15% of failures)
3. **ALLOWED_HOSTS not set correctly** (5% of failures)

**Copy the error from Railway logs and I can provide specific help!**
