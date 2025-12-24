# Django-Ecommerce

Modern Ecommerce platform built with Django 3.2, Python 3.8+, and MySQL database. Features full shopping cart, Stripe payments, user authentication with OAuth, and admin dashboard.

![image](https://user-images.githubusercontent.com/29988949/65267147-499fc580-dac9-11e9-90e8-eccbc93c7c3a.png)

`Product Slide`

![image](https://user-images.githubusercontent.com/29988949/65999313-ff67fe00-e451-11e9-9ed9-fc7bce704f17.png)

`Shop Page`
![image](https://user-images.githubusercontent.com/29988949/66098968-923f9000-e559-11e9-8691-cd5c2b181ca1.png)

`Product Detail Page`
![image](https://user-images.githubusercontent.com/29988949/66291084-bff84200-e895-11e9-8d53-3aa23b29dbae.png)

`Cart Page`
![image](https://user-images.githubusercontent.com/29988949/66291144-f0d87700-e895-11e9-8545-b8f93f799063.png)

`BillingAddress Page`
![image](https://user-images.githubusercontent.com/29988949/66291542-013d2180-e897-11e9-8ea9-40afcb90cee2.png)

`Stripe Payment Page`
![image](https://user-images.githubusercontent.com/29988949/66291610-29c51b80-e897-11e9-8b47-20de35d6c1d0.png)

`Order Success Page`
![image](https://user-images.githubusercontent.com/29988949/66291657-3e091880-e897-11e9-830b-6cf44e72a995.png)




# Installation

## Quick Start

```bash
git clone https://github.com/your-username/Django-Ecommerce.git
cd Django-Ecommerce
```

### Setup Virtual Environment

**Windows:**
```bash
python -m venv env
env\Scripts\activate
```

**Mac/Linux:**
```bash
python -m venv env
source env/bin/activate
```

### Install Requirements

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Configure MySQL Database

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` with your MySQL credentials

3. Create MySQL database:
   ```bash
   mysql -u root -p
   CREATE DATABASE ecommerce_db CHARACTER SET utf8mb4;
   CREATE USER 'ecommerce_user'@'localhost' IDENTIFIED BY 'your_password';
   GRANT ALL PRIVILEGES ON ecommerce_db.* TO 'ecommerce_user'@'localhost';
   FLUSH PRIVILEGES;
   ```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Start Development Server

```bash
python manage.py runserver
```

Visit: http://localhost:8000/
Admin: http://localhost:8000/admin/

## Complete Setup Guide

For detailed MySQL setup and troubleshooting, see [MYSQL_SETUP.md](MYSQL_SETUP.md)

## Deprecated Installation Instructions

**Note:** The following versions are outdated and may cause conflicts with Django 3.2:

```python
# Do NOT use these - they will cause compatibility issues
# pip install Django==2.2.4
# python -m pip install django-allauth==0.40.0
# pip install django-crispy-forms==1.7.2
# pip install django-countries==5.5
# pip install stripe==2.37.1
# pip install Pillow
```

**Use `pip install -r requirements.txt` instead for compatible versions.**
# Demo

Live demo available at: http://djangoecommerce.pythonanywhere.com

## Features

- ✅ MySQL Database Integration
- ✅ User Authentication & Authorization
- ✅ Google OAuth Integration
- ✅ Shopping Cart Functionality
- ✅ Stripe Payment Integration
- ✅ Order Management System
- ✅ Admin Dashboard
- ✅ Responsive Design
- ✅ Product Catalog with Categories
- ✅ Refund Request System

## Technology Stack

- **Backend:** Django 3.2.25
- **Database:** MySQL 5.7+
- **Frontend:** HTML5, CSS3, Bootstrap 4, JavaScript
- **Payments:** Stripe API
- **Authentication:** Django-allauth
- **Server:** WSGI (production-ready)

## System Requirements

- Python 3.8+
- MySQL 5.7+
- 1GB RAM minimum
- 500MB disk space

## License

This project is protected under a proprietary license. See [LICENSE](LICENSE) file for details.

For commercial licensing or inquiries, contact: your-email@example.com

## Original Template

HTML Template based on: https://colorlib.com/etc/fashe/index.html


