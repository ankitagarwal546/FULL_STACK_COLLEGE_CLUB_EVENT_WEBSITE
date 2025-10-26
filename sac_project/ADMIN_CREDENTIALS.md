# Admin Credentials

## Django Admin Panel Access

**URL**: http://127.0.0.1:8000/admin/

**Credentials**:
- **Username**: `admin`
- **Password**: `admin123`

## Important Notes

⚠️ **For Production**: Change the password immediately!
```bash
python manage.py changepassword admin
```

## Quick Access

After starting the server with `python manage.py runserver`, you can access:

1. **Admin Panel**: http://127.0.0.1:8000/admin/
   - Login with credentials above
   - Manage Clubs, Events, Gallery Photos

2. **Website Pages**:
   - Home: http://127.0.0.1:8000/
   - Clubs: http://127.0.0.1:8000/clubs/
   - Events: http://127.0.0.1:8000/events/
   - Gallery: http://127.0.0.1:8000/gallery/
   - Members: http://127.0.0.1:8000/members/
   - Contact: http://127.0.0.1:8000/contact/

## Getting Started

1. Start the server (if not already running):
   ```bash
   source venv/bin/activate
   python manage.py runserver
   ```

2. Visit http://127.0.0.1:8000/admin/

3. Login with credentials above

4. Start adding content:
   - Add Clubs (with Google Form links)
   - Create Events (mark as upcoming/past)
   - Upload Gallery Photos (by section)

---

**Note**: This is a development setup. For production, use stronger passwords and environment variables.
