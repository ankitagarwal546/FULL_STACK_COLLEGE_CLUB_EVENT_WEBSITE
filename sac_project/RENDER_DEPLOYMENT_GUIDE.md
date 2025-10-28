# Render Deployment Guide for SAC Website

## 🚀 Complete Render Deployment Steps

### Prerequisites
- GitHub account
- Render account (sign up at https://render.com - it's FREE!)
- Your code pushed to GitHub repository

---

## Step 1: Push Your Code to GitHub (If Not Already Done)

```bash
cd /Users/ankitagarwal546/Desktop/FULL_STACK_COLLEGE_CLUB_EVENT_WEBSITE/sac_project

# Add all files
git add .

# Commit
git commit -m "Add Render deployment configuration"

# Push to GitHub
git push origin main
```

---

## Step 2: Create Render Account & New Web Service

1. Go to https://render.com
2. Click **"Get Started for Free"** or **"Sign Up"**
3. Sign up with GitHub (recommended)
4. Authorize Render to access your GitHub repositories

---

## Step 3: Create Web Service

1. After logging in, click **"New +"** → **"Web Service"**
2. Connect your GitHub repository: `FULL_STACK_COLLEGE_CLUB_EVENT_WEBSITE`
3. If you don't see it, click **"Configure account"** and grant access to the repo

---

## Step 4: Configure Web Service

Fill in the following settings:

### Basic Settings:
- **Name:** `sac-website` (or any name you prefer)
- **Region:** Choose closest to your users (e.g., Oregon, Frankfurt, Singapore)
- **Branch:** `main`
- **Root Directory:** `sac_project` ⚠️ **IMPORTANT!**
- **Runtime:** `Python 3`

### Build & Deploy:
- **Build Command:** `./build.sh`
- **Start Command:** `gunicorn sac_project.wsgi:application`

### Instance Type:
- **Free** (select the free tier)

---

## Step 5: Add Environment Variables

Scroll down to **"Environment Variables"** section and click **"Add Environment Variable"**.

Add these variables one by one:

### Required Variables:

```
SECRET_KEY
Value: 2=gutdd^a%bz4#ch(f3%a@&171v$l#sesexrss)zrksv2aqzh5

DEBUG
Value: False

PYTHON_VERSION
Value: 3.13.7

ALLOWED_HOSTS
Value: .onrender.com

WEB_CONCURRENCY
Value: 4
```

**Note:** We use `.onrender.com` for ALLOWED_HOSTS because Render domains end with `.onrender.com`

---

## Step 6: Add PostgreSQL Database

1. In Render dashboard, click **"New +"** → **"PostgreSQL"**
2. **Name:** `sac-database` (or any name)
3. **Database:** `sac_db`
4. **User:** `sac_user` (auto-generated)
5. **Region:** Same as your web service
6. **PostgreSQL Version:** `16` (latest)
7. **Plan:** **Free**
8. Click **"Create Database"**

---

## Step 7: Connect Database to Web Service

1. Go to your PostgreSQL database in Render
2. Scroll down to **"Connections"**
3. Copy the **"Internal Database URL"** (starts with `postgresql://`)
4. Go back to your Web Service
5. Go to **"Environment"** tab
6. Click **"Add Environment Variable"**
7. Add:
   ```
   DATABASE_URL
   Value: <paste-the-internal-database-url>
   ```

---

## Step 8: Deploy!

1. Click **"Create Web Service"** at the bottom
2. Render will start building your app (takes 3-5 minutes)
3. Watch the logs in real-time
4. Wait for "Your service is live 🎉" message

---

## Step 9: Create Admin User

After deployment succeeds:

1. In your web service, go to **"Shell"** tab (top right)
2. Click **"Launch Shell"**
3. Run these commands:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

---

## Step 10: Access Your Website! 🎉

Your website will be live at:
- **Main site:** `https://sac-website.onrender.com`
- **Admin panel:** `https://sac-website.onrender.com/admin`

(Replace `sac-website` with your actual service name)

---

## 📋 Complete Checklist

- [ ] Code pushed to GitHub
- [ ] Render account created
- [ ] Web Service created with correct settings
- [ ] Root Directory set to `sac_project`
- [ ] Build command: `./build.sh`
- [ ] Start command: `gunicorn sac_project.wsgi:application`
- [ ] Environment variables added (SECRET_KEY, DEBUG, PYTHON_VERSION, ALLOWED_HOSTS, WEB_CONCURRENCY)
- [ ] PostgreSQL database created
- [ ] DATABASE_URL connected to web service
- [ ] Deployment successful
- [ ] Admin user created via Shell
- [ ] Website is accessible

---

## 🔧 Troubleshooting

### Issue: "Permission denied: ./build.sh"
**Solution:** Make build.sh executable locally, then push:
```bash
chmod +x build.sh
git add build.sh
git commit -m "Make build.sh executable"
git push origin main
```

### Issue: "DisallowedHost" error
**Solution:** Your ALLOWED_HOSTS is already set to `.onrender.com` which covers all Render domains ✅

### Issue: Static files not loading
**Solution:** 
- Build command runs `collectstatic` automatically ✅
- WhiteNoise serves static files ✅
- Should work by default

### Issue: Database connection error
**Solution:** 
- Make sure DATABASE_URL is set in environment variables
- Use **Internal Database URL** from PostgreSQL dashboard
- Check that database is in the same region as web service

### Issue: Build fails
**Solution:** Check build logs in Render dashboard. Common issues:
- Wrong root directory (should be `sac_project`)
- Missing packages in requirements.txt
- Python version mismatch

---

## 🔄 Updating Your Website

After making changes:

```bash
git add .
git commit -m "Your update message"
git push origin main
```

Render will automatically detect the push and redeploy! 🎉

---

## 💰 Render Pricing

### Free Tier Includes:
- **Web Services:** Sleeps after 15 minutes of inactivity (wakes up in ~30 seconds)
- **PostgreSQL:** 1GB storage, limited to 90 days for free tier
- **Bandwidth:** 100GB/month
- **Build minutes:** 500 minutes/month

**Perfect for testing and small projects!**

### Paid Plans:
- **Starter ($7/month):** No sleep, better performance
- **Database ($7/month):** Persistent database, no time limit

---

## 📱 Custom Domain (Optional)

To use your own domain:
1. In web service → **Settings** → **Custom Domain**
2. Add your domain
3. Update DNS records as shown by Render
4. Update ALLOWED_HOSTS environment variable to include your domain

---

## ⚠️ Important Notes

### Free Tier Limitations:
1. **Web service sleeps after 15 min inactivity** (wakes in ~30s on next visit)
2. **Database expires after 90 days** (upgrade to paid to keep data)
3. **Monthly build minutes limited** (500 min/month)

### Tips:
- Use internal database URL (faster connection)
- Keep web service awake with uptime monitoring (optional)
- Media files uploaded via admin will persist on Render disk

---

## 🆘 Need Help?

- **Render Docs:** https://render.com/docs/deploy-django
- **Render Community:** https://community.render.com
- **Django Deployment:** https://docs.djangoproject.com/en/4.2/howto/deployment/

---

## ✅ Quick Reference

### Build Command:
```bash
./build.sh
```

### Start Command:
```bash
gunicorn sac_project.wsgi:application
```

### Environment Variables:
```
SECRET_KEY=2=gutdd^a%bz4#ch(f3%a@&171v$l#sesexrss)zrksv2aqzh5
DEBUG=False
PYTHON_VERSION=3.13.7
ALLOWED_HOSTS=.onrender.com
WEB_CONCURRENCY=4
DATABASE_URL=<from-postgresql-dashboard>
```

---

**Your SAC website will be live on Render in minutes! 🚀**
