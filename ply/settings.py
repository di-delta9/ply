"""
Django settings for ply project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY") 
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#TODO: MAKE IT SO ALLOWED HOSTS ARE OPTIONAL!
ALLOWED_HOSTS = [config("ALLOWED_HOST_1"),config("ALLOWED_HOST_2"),config("ALLOWED_HOST_3")] 


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_bootstrap5',
    'dashboard',
    'dynapages',
    'profiles',
    'comms',
    'gallery',
    'stream',
    'group',
    'keywords',
    'community',
    'gallery_photos',
    'metrics',
    'stats',
    'combat',
    'skills',
    'equipment',
    'spells',
    'items',
    'forge',
    'testdata',
    'ply'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ply.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ply.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pixel',
        'USER': 'pixel',
        'PASSWORD': 'OhT4jaem',
        'HOST': '10.100.102.5',
        'PORT': ''
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PLY_USER_DASHBOARD_MODULES = [
    "profiles",
    "gallery"
    
    ]

PLY_GALLERY_PLUGINS = [
    "gallery_photos"
    ]

PLY_TEMP_FILE_BASE_PATH = "/var/www/html/ply_incoming/"
PLY_TEMP_FILE_URL_BASE_URL="http://10.100.102.5/ply_incoming/"
PLY_GALLERY_ORIGINAL_FILE_BASE_PATH = "/opt/ply/originals/"
PLY_GALLERY_FILE_BASE_PATH = "/var/www/html/ply_gallery/"
PLY_GALLERY_FILE_URL_BASE_URL="http://10.100.102.5/ply_gallery/"
PLY_GALLERY_HASH_BUF_SIZE  = 65536
PLY_MSG_BROKER_URL="amqp://guest:guest@localhost:5672/%2F?connection_attempts=10&heartbeat=360"
GALLERY_PHOTOS_THUMBNAIL_SIZE = 450
PLY_GALLERY_MIN_DPI = 100
CELERY_BROKER_URL=PLY_MSG_BROKER_URL
