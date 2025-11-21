"""
Django settings for class_scheduling_system project.
"""

import os
from pathlib import Path

# ---------------- BASE DIR ---------------- #
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------- SECRET KEY ---------------- #
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "unsafe-secret-for-dev")

# ---------------- DEBUG ---------------- #
DEBUG = os.environ.get("DEBUG", "False") == "True"

# ---------------- ALLOWED HOSTS ---------------- #
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "ace-scheduling-system-2.onrender.com"
]

# ---------------- INSTALLED APPS ---------------- #
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'scheduler',

    # Third-party
    'crispy_forms',
    'crispy_bootstrap5',
    'tailwind',
    'widget_tweaks',
    'multiselectfield',
]

TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ["127.0.0.1"]

# ---------------- MIDDLEWARE ---------------- #
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'class_scheduling_system.urls'

# ---------------- TEMPLATES ---------------- #
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'class_scheduling_system.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', 'class_scheduling_system'),
        'USER': os.environ.get('DB_USER', 'root'),
        'PASSWORD': os.environ.get('DB_PASSWORD', '12345'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '3306'),
    }
}

# ---------------- PASSWORD VALIDATION ---------------- #
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'scheduler.validators.FourDigitPasswordValidator',
    },
]

# ---------------- INTERNATIONALIZATION ---------------- #
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ---------------- STATIC FILES ---------------- #
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ---------------- MEDIA FILES ---------------- #
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ---------------- DEFAULT PRIMARY KEY ---------------- #
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ---------------- CUSTOM USER MODEL ---------------- #
AUTH_USER_MODEL = 'scheduler.User'

# ---------------- LOGIN/LOGOUT REDIRECTS ---------------- #
LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = '/login/'
LOGIN_REDIRECT_URL = '/admin_dashboard/'

# ---------------- CRISPY FORMS ---------------- #
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
