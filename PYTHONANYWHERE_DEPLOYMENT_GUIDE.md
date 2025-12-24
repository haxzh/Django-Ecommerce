# PythonAnywhere Deployment Guide

## Complete Guide to Deploy Your Django E-commerce Project to PythonAnywhere

### Prerequisites
- PythonAnywhere account (free or paid)
- Your project ready with all changes committed
- Database populated with products and images

---

## Step 1: Create PythonAnywhere Account

1. Go to https://www.pythonanywhere.com/
2. Sign up for a free account (or paid if you need a custom domain)
3. Verify your email address

---

## Step 2: Upload Your Project

### Option A: Using Git (Recommended)

1. **Create a GitHub repository** (if you haven't already):
   ```bash
   # In your project directory
   git init
   git add .
   git commit -m "Initial commit - Django Ecommerce Project"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/django-ecommerce.git
   git push -u origin main
   ```

2. **Clone on PythonAnywhere**:
   - Log in to PythonAnywhere
   - Go to "Consoles" → "Bash"
   - Run:
   ```bash
   git clone https://github.com/YOUR_USERNAME/django-ecommerce.git
   cd django-ecommerce
   ```

### Option B: Upload Files Directly

1. Go to "Files" tab in PythonAnywhere
2. Create a directory: `/home/YOUR_USERNAME/django-ecommerce`
3. Upload your project files using the file browser
4. **Note**: This is slower for large projects

---

## Step 3: Set Up Virtual Environment

In the PythonAnywhere Bash console:

```bash
# Navigate to your project
cd ~/django-ecommerce

# Create virtual environment
mkvirtualenv --python=/usr/bin/python3.10 myenv

# Activate it (it should auto-activate after creation)
workon myenv

# Install requirements
pip install -r requirements.txt
```

---

## Step 4: Configure Database

### For SQLite (Recommended for Free Tier):

1. **Update settings.py** - Create a separate settings file or modify existing:

```python
# In demo/settings.py, add at the bottom:
import os

if 'PYTHONANYWHERE_DOMAIN' in os.environ:
    # PythonAnywhere-specific settings
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/home/YOUR_USERNAME/django-ecommerce/db.sqlite3',
        }
    }
    
    # Allowed hosts
    ALLOWED_HOSTS = ['YOUR_USERNAME.pythonanywhere.com']
    
    # Static files
    STATIC_ROOT = '/home/YOUR_USERNAME/django-ecommerce/staticfiles'
    STATIC_URL = '/static/'
    
    # Media files
    MEDIA_ROOT = '/home/YOUR_USERNAME/django-ecommerce/media_root'
    MEDIA_URL = '/media/'
    
    # Security
    DEBUG = False
else:
    # Local development settings (existing settings remain)
    pass
```

2. **Upload your db.sqlite3** file if you have data locally

### For MySQL (Paid Accounts Only):

PythonAnywhere free accounts don't support MySQL. Paid accounts can use:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'YOUR_USERNAME$ecommerce_db',
        'USER': 'YOUR_USERNAME',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'YOUR_USERNAME.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
```

---

## Step 5: Collect Static Files

```bash
cd ~/django-ecommerce
workon myenv

# Set environment variable for PythonAnywhere
export PYTHONANYWHERE_DOMAIN=1

# Collect static files
python manage.py collectstatic --noinput

# Create database tables (if not using existing db.sqlite3)
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

---

## Step 6: Upload Media Files

1. **Option A: Direct Upload**
   - Go to Files tab
   - Navigate to `/home/YOUR_USERNAME/django-ecommerce/media_root/`
   - Upload all your product images from local `media_root` folder

2. **Option B: Using SCP/SFTP**
   - Use FileZilla or WinSCP
   - Connect to: `YOUR_USERNAME.pythonanywhere.com`
   - Upload `media_root` folder contents

---

## Step 7: Configure Web App

1. **Go to Web tab** in PythonAnywhere dashboard

2. **Click "Add a new web app"**

3. **Select**: Manual configuration → Python 3.10

4. **Configure WSGI file**:
   - Click on the WSGI configuration file link
   - Replace contents with:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/YOUR_USERNAME/django-ecommerce'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variable
os.environ['PYTHONANYWHERE_DOMAIN'] = '1'

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'demo.settings'

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

5. **Set Virtual Environment**:
   - In Web tab, find "Virtualenv" section
   - Enter: `/home/YOUR_USERNAME/.virtualenvs/myenv`

6. **Configure Static Files**:
   - In "Static files" section, add:
     - URL: `/static/`
     - Directory: `/home/YOUR_USERNAME/django-ecommerce/staticfiles`
   
   - Add another mapping:
     - URL: `/media/`
     - Directory: `/home/YOUR_USERNAME/django-ecommerce/media_root`

7. **Set Source Code**:
   - In "Code" section
   - Source code: `/home/YOUR_USERNAME/django-ecommerce`
   - Working directory: `/home/YOUR_USERNAME/django-ecommerce`

---

## Step 8: Update Settings for Production

Create a separate production settings file or update `demo/settings.py`:

```python
# demo/settings.py additions

import os

# Security Settings for Production
if not DEBUG:
    SECURE_SSL_REDIRECT = False  # PythonAnywhere handles SSL
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'

# Allowed Hosts
ALLOWED_HOSTS = [
    'YOUR_USERNAME.pythonanywhere.com',
    'localhost',
    '127.0.0.1',
]

# Email Configuration (optional)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
```

---

## Step 9: Reload Web App

1. Go to Web tab
2. Click the green **"Reload"** button
3. Wait for reload to complete
4. Visit: `https://YOUR_USERNAME.pythonanywhere.com`

---

## Step 10: Populate Database (If Needed)

If starting fresh without uploading db.sqlite3:

```bash
cd ~/django-ecommerce
workon myenv

# Run setup script
python setup_ecommerce_data.py

# Or update products/images
python update_product_images.py
python convert_to_inr.py
```

---

## Troubleshooting

### Error: "Import Error" or "Module not found"

1. Check virtual environment is activated
2. Verify all packages in requirements.txt are installed
3. Check WSGI file paths are correct

```bash
workon myenv
pip list  # Verify packages
```

### Static Files Not Loading

1. Verify static files mapping in Web tab
2. Run collectstatic again:
```bash
python manage.py collectstatic --clear --noinput
```

3. Check STATIC_ROOT path in settings.py

### Images Not Displaying

1. Verify media files mapping in Web tab
2. Check MEDIA_ROOT and MEDIA_URL in settings.py
3. Ensure all images are uploaded to media_root folder
4. Check file permissions:
```bash
chmod -R 755 ~/django-ecommerce/media_root
```

### Database Errors

1. Run migrations:
```bash
python manage.py migrate
```

2. Check database path is absolute:
```python
'NAME': '/home/YOUR_USERNAME/django-ecommerce/db.sqlite3',
```

### Error Logs

View error logs in PythonAnywhere:
- Web tab → Log files → Error log
- Check for specific errors

---

## Post-Deployment Checklist

- [ ] Website loads at YOUR_USERNAME.pythonanywhere.com
- [ ] Static files (CSS, JS) are loading correctly
- [ ] Product images are displaying
- [ ] Homepage slider images are showing
- [ ] Navigation menu works
- [ ] Product listing pages work
- [ ] Product detail pages work
- [ ] Add to cart functionality works
- [ ] Cart page displays correctly
- [ ] Checkout process works
- [ ] Admin panel is accessible at /admin/
- [ ] All prices display in ₹ (Indian Rupees)
- [ ] Color scheme matches (Blue #2563EB)
- [ ] Mobile responsiveness works

---

## Updating Your Deployed Site

When you make changes to your project:

1. **Push changes to GitHub**:
```bash
git add .
git commit -m "Updated feature XYZ"
git push origin main
```

2. **Pull changes on PythonAnywhere**:
```bash
cd ~/django-ecommerce
workon myenv
git pull origin main

# If requirements changed
pip install -r requirements.txt

# If models changed
python manage.py migrate

# Collect static files if CSS/JS changed
python manage.py collectstatic --noinput
```

3. **Reload web app** from Web tab

---

## Custom Domain (Paid Accounts Only)

1. Go to Web tab
2. Add your custom domain
3. Update DNS records at your domain registrar:
   - CNAME record pointing to `YOUR_USERNAME.pythonanywhere.com`
4. Update ALLOWED_HOSTS in settings.py:
```python
ALLOWED_HOSTS = [
    'yourdomain.com',
    'www.yourdomain.com',
    'YOUR_USERNAME.pythonanywhere.com',
]
```

---

## Environment Variables (For Sensitive Data)

Store sensitive data in environment variables:

1. **In PythonAnywhere Bash console**:
```bash
# Edit .bashrc
nano ~/.bashrc

# Add at the end:
export SECRET_KEY='your-secret-key-here'
export EMAIL_USER='your-email@gmail.com'
export EMAIL_PASSWORD='your-email-password'

# Save and reload
source ~/.bashrc
```

2. **In settings.py**:
```python
import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'default-dev-key')
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
```

---

## Performance Optimization

### Enable Caching

```python
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
    }
}

# Create cache table
# python manage.py createcachetable
```

### Optimize Images

- Compress images before uploading
- Use WebP format where possible
- Images already in your media_root are optimized

### Enable Gzip Compression

PythonAnywhere enables this by default for static files.

---

## Backup Strategy

### Regular Backups

```bash
# Backup database
cd ~/django-ecommerce
cp db.sqlite3 db.sqlite3.backup-$(date +%Y%m%d)

# Backup media files
tar -czf media-backup-$(date +%Y%m%d).tar.gz media_root/

# Download to local machine using Files tab
```

---

## Support Resources

- **PythonAnywhere Help**: https://help.pythonanywhere.com/
- **PythonAnywhere Forum**: https://www.pythonanywhere.com/forums/
- **Django Documentation**: https://docs.djangoproject.com/
- **Your Project Docs**: See README.md, SETUP_GUIDE.md

---

## Quick Reference Commands

```bash
# Activate virtual environment
workon myenv

# Update code from Git
cd ~/django-ecommerce && git pull

# Install new packages
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Create superuser
python manage.py createsuperuser

# Run Django shell
python manage.py shell

# View logs
tail -f /var/log/YOUR_USERNAME.pythonanywhere.com.error.log
```

---

## Your Project-Specific Notes

Your Django E-commerce project includes:

- **Indian Rupee (₹) prices**: ₹1,199 - ₹3,999 range
- **Modern blue color scheme**: #2563EB primary, #F59E0B accent
- **Products**: 11 products with images (T-shirts, Shirts, Hoodies, Skirts)
- **Categories**: Multiple categories with banner images
- **Homepage sliders**: 3 sliders with actual images
- **Free shipping**: Message for orders over ₹2,999
- **Payment**: Stripe integration (configured for INR)

All localization for Indian market is complete!

---

## Need Help?

If you encounter issues during deployment:

1. Check PythonAnywhere error logs
2. Verify all paths use absolute paths
3. Ensure virtual environment is activated
4. Check file permissions (chmod 755)
5. Verify ALLOWED_HOSTS includes your domain
6. Test locally first with `DEBUG=False`

Good luck with your deployment! 🚀
