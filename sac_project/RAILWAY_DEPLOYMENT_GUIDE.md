# Railway Deployment Guide for SAC Website

## 🚀 Complete Deployment Steps

### Prerequisites
- GitHub account
- Railway account (sign up at https://railway.app with GitHub)
- Your code pushed to GitHub repository

---

## Step 1: Push Your Code to GitHub

If you haven't already pushed your code:

```bash
cd /Users/ankitagarwal546/Desktop/FULL_STACK_COLLEGE_CLUB_EVENT_WEBSITE/sac_project

# Initialize git if not already done
git init

# Add all files
git add .

# Commit
git commit -m "Prepare for Railway deployment"

# Add your GitHub repository (replace with your repo URL)
git remote add origin https://github.com/ankitagarwal546/FULL_STACK_COLLEGE_CLUB_EVENT_WEBSITE.git

# Push to GitHub
git push -u origin main
```

---

## Step 2: Create Railway Project

1. Go to https://railway.app
2. Click **"Start a New Project"**
3. Select **"Deploy from GitHub repo"**
4. Authorize Railway to access your GitHub
5. Select your repository: `FULL_STACK_COLLEGE_CLUB_EVENT_WEBSITE`
6. Railway will automatically detect it's a Django project

---

## Step 3: Add PostgreSQL Database

1. In your Railway project, click **"+ New"**
2. Select **"Database"**
3. Choose **"PostgreSQL"**
4. Railway will automatically create a `DATABASE_URL` environment variable

---

## Step 4: Configure Environment Variables

In Railway project settings, go to **"Variables"** tab and add:

### Required Variables:

```
SECRET_KEY=your-super-secret-key-here-make-it-long-and-random
DEBUG=False
ALLOWED_HOSTS=your-app-name.up.railway.app
```

### How to generate SECRET_KEY:
Run this command locally:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Note:** `DATABASE_URL` is automatically set by Railway when you add PostgreSQL.

---

## Step 5: Deploy!

1. Railway will automatically deploy after you add the database
2. Wait for the build to complete (usually 2-3 minutes)
3. Click on your deployment to see the public URL
4. Your website will be live at: `https://your-app-name.up.railway.app`

---

## Step 6: Create Admin User (Important!)

After first deployment, you need to create an admin user:

1. In Railway, go to your **project**
2. Click on the **service** (your Django app)
3. Go to **"Settings"** → **"Deploys"**
4. Find the latest deploy and click the **three dots** → **"View Logs"**
5. On the top right, click **"+ New Tab"** (terminal icon)
6. This opens a terminal in your Railway container

Run these commands in the Railway terminal:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

---

## Step 7: Update ALLOWED_HOSTS

After Railway gives you your public domain:

1. Copy your Railway domain (e.g., `your-app-name.up.railway.app`)
2. Update the `ALLOWED_HOSTS` environment variable in Railway:
   ```
   ALLOWED_HOSTS=your-app-name.up.railway.app
   ```
3. Railway will automatically redeploy

---

## 📋 Checklist

- [ ] Code pushed to GitHub
- [ ] Railway project created from GitHub repo
- [ ] PostgreSQL database added
- [ ] Environment variables set (SECRET_KEY, DEBUG, ALLOWED_HOSTS)
- [ ] Deployment successful
- [ ] Admin user created
- [ ] Can access admin panel at: `https://your-domain.up.railway.app/admin`
- [ ] Website is live and working

---

## 🔧 Troubleshooting

### Issue: "DisallowedHost" error
**Solution:** Add your Railway domain to `ALLOWED_HOSTS` environment variable

### Issue: Static files not loading
**Solution:** Railway should run `collectstatic` automatically. Check deployment logs.

### Issue: Database connection error
**Solution:** Make sure PostgreSQL database is added and `DATABASE_URL` is set

### Issue: Can't access admin panel
**Solution:** Create superuser using Railway terminal (see Step 6)

---

## 🔄 Updating Your Website

After making changes:

```bash
# Commit your changes
git add .
git commit -m "Your update message"

# Push to GitHub
git push origin main
```

Railway will automatically detect the push and redeploy! 🎉

---

## 💰 Railway Pricing

- **Free tier**: $5 credit per month
- Your small Django app should use ~$3-5/month
- No credit card required to start
- Monitor usage in Railway dashboard

---

## 📱 Accessing Your Website

- **Main site**: https://your-app-name.up.railway.app
- **Admin panel**: https://your-app-name.up.railway.app/admin
- **Login with the superuser credentials you created**

---

## 🎯 Next Steps After Deployment

1. **Upload your media files** (club images, gallery photos) through admin panel
2. **Test all features** on production
3. **Share your live website URL** with your team
4. **Set up custom domain** (optional, available in Railway settings)

---

## 📞 Need Help?

- Railway Docs: https://docs.railway.app
- Django Deployment Checklist: https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
- Railway Discord: https://discord.gg/railway

---

**Congratulations! Your SAC website is now live on Railway! 🎉**
