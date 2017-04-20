"""
Django settings for TchirkataPhoto project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import os.path
TEMPLATE_DIRS =(os.path.join(os.path.dirname(__file__), 'templates'),)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_NAME = 'GPantix'
META_KEYWORDS = 'Music, instruments, music accessories, musician supplies'
META_DESCRIPTION = 'Modern Musician is an online supplier of instruments, sheet music, and other accessories for musicians'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4o6sio6y1w_%x+d6gv4s#w1=4nr+aydkxdaf_(y#ts#)vrxf%u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chirkphoto',
    'catalogue',
    #'shop.addressmodel', # The default Address and country models
    #'myShop', # the project we just created
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   # 'djangodblog.DBLogMiddleware',
)

ROOT_URLCONF = 'TchirkataPhoto.urls'

WSGI_APPLICATION = 'TchirkataPhoto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER' :'',
        'PASSWORD':'',
        'HOST':'',
        'PORT':'',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
