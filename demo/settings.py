import os
from pathlib import Path

# --------------------------------------------------
# BASE
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

SECRET_KEY = os.getenv('SECRET_KEY', '-05sgp9!deq=q1nltm@^^2cc+v29i(tyybv3v2t77qi66czazj')

DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

# --------------------------------------------------
# APPLICATIONS
# --------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',

    # Third-party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'crispy_forms',
    'django_countries',

    # Local
    'core',
]

# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # REQUIRED for django-allauth
    'allauth.account.middleware.AccountMiddleware',
]

# --------------------------------------------------
# URLS / TEMPLATES
# --------------------------------------------------

ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'demo.wsgi.application'

# --------------------------------------------------
# DATABASE (MySQL)
# --------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('MYSQL_DATABASE', 'ecommerce_db'),
        'USER': os.getenv('MYSQL_USER', 'root'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD', ''),
        'HOST': os.getenv('MYSQL_HOST', '127.0.0.1'),
        'PORT': os.getenv('MYSQL_PORT', '3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES', innodb_strict_mode=1",
            'charset': 'utf8mb4',
            'autocommit': True,
        },
        'CONN_MAX_AGE': 600,
    }
}

# --------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# --------------------------------------------------
# STATIC & MEDIA
# --------------------------------------------------

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static_in_env',
]

STATIC_ROOT = BASE_DIR / 'static_root'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media_root'

# --------------------------------------------------
# DJANGO 3.2 REQUIRED
# --------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --------------------------------------------------
# AUTH / ALLAUTH
# --------------------------------------------------

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'

# --------------------------------------------------
# SOCIAL AUTH (GOOGLE)
# --------------------------------------------------

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': os.getenv('GOOGLE_CLIENT_ID', '123'),
            'secret': os.getenv('GOOGLE_CLIENT_SECRET', '456'),
            'key': os.getenv('GOOGLE_CLIENT_SECRET', '666'),
        }
    }
}

# --------------------------------------------------
# CRISPY FORMS
# --------------------------------------------------

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# --------------------------------------------------
# STRIPE
# --------------------------------------------------

STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', 'pk_test_lX3r6OMjOU2yzFsNSHq6belT00EY82kZmH')
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")

# --------------------------------------------------
# EMAIL CONFIGURATION
# --------------------------------------------------

EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True').lower() == 'true'

# --------------------------------------------------
# PRODUCTION SECURITY
# --------------------------------------------------

if ENVIRONMENT == 'production':
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')

    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    CSRF_COOKIE_HTTPONLY = True

    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
