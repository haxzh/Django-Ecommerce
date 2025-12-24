# Django-Ecommerce - MySQL Setup Guide

This guide will help you set up the Django-Ecommerce project with MySQL database.

## Prerequisites

- Python 3.8+
- MySQL Server 5.7+
- Git

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Django-Ecommerce.git
cd Django-Ecommerce
```

### 2. Create Virtual Environment

**For Windows:**
```bash
python -m venv env
env\Scripts\activate
```

**For Mac/Linux:**
```bash
python -m venv env
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. MySQL Database Setup

#### Option A: Using MySQL Command Line

```bash
# Log in to MySQL
mysql -u root -p

# Create database and user
CREATE DATABASE ecommerce_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'ecommerce_user'@'localhost' IDENTIFIED BY 'your_secure_password';
GRANT ALL PRIVILEGES ON ecommerce_db.* TO 'ecommerce_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

#### Option B: Using MySQL Workbench

1. Open MySQL Workbench
2. Create new Schema: `ecommerce_db` (Character Set: utf8mb4)
3. Create new User: `ecommerce_user` with password
4. Grant all privileges on `ecommerce_db` to `ecommerce_user`

### 5. Configure Environment Variables

Copy the `.env.example` file to `.env`:

```bash
cp .env.example .env
```

Edit `.env` with your MySQL credentials:

```
ENVIRONMENT=development
DEBUG=True

MYSQL_DATABASE=ecommerce_db
MYSQL_USER=ecommerce_user
MYSQL_PASSWORD=your_secure_password
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306

SECRET_KEY=your-secret-key-here
```

> **Important:** Never commit `.env` file to version control. It's already in `.gitignore`.

### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts:
- Username: admin
- Email: admin@example.com
- Password: your_secure_password

### 8. Collect Static Files (Production Only)

```bash
python manage.py collectstatic --noinput
```

### 9. Run Development Server

```bash
python manage.py runserver
```

Visit: http://localhost:8000/

Admin panel: http://localhost:8000/admin/

## Troubleshooting

### MySQL Connection Errors

**Error: "Access denied for user 'root'@'localhost'..."**
- Check your MySQL credentials in `.env`
- Verify MySQL server is running

**Error: "No module named 'MySQLdb'..."**
- Install MySQL client: `pip install mysqlclient`
- Alternative: `pip install PyMySQL`

### Migration Errors

```bash
# Reset migrations (development only - WARNING: deletes all data)
python manage.py migrate core zero
rm core/migrations/000*.py
python manage.py makemigrations
python manage.py migrate
```

### Database Issues

```bash
# Check current migrations
python manage.py showmigrations

# Fake migrations (if needed)
python manage.py migrate --fake
```

## Deployment Checklist

- [ ] Set `DEBUG = False` in `.env` or settings
- [ ] Update `SECRET_KEY` to a strong random value
- [ ] Set `ALLOWED_HOSTS` properly
- [ ] Configure email settings
- [ ] Set up Stripe keys
- [ ] Configure Google OAuth credentials
- [ ] Use MySQL on a secure server
- [ ] Enable HTTPS/SSL certificate
- [ ] Set `ENVIRONMENT=production` in `.env`

## Database Backup & Restore

### Backup

```bash
mysqldump -u ecommerce_user -p ecommerce_db > backup.sql
```

### Restore

```bash
mysql -u ecommerce_user -p ecommerce_db < backup.sql
```

## Performance Tips

1. **Enable Query Caching:**
   ```sql
   SET GLOBAL query_cache_type = ON;
   SET GLOBAL query_cache_size = 268435456;
   ```

2. **Add Database Indexes:**
   - Already configured in models
   - Review `core/models.py` for indexed fields

3. **Use Connection Pooling:**
   - Configured in settings with `CONN_MAX_AGE = 600`

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django with MySQL](https://docs.djangoproject.com/en/stable/ref/databases/#mysql-notes)
- [MySQL Documentation](https://dev.mysql.com/doc/)

## Support

For issues or questions, please create a GitHub issue or contact the development team.
