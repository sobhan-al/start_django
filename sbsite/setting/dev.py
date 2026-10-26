from sbsite.settings import *

SECRET_KEY = 'django-insecure-rs@#%w@$0o+@3hmz0@cc_#r8r)y^dl4(ddg%c^$x)yle%jta94'
DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'multi_captcha_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website.apps.WebsiteConfig',
    'blog.apps.BlogConfig',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'robots',
    'debug_toolbar',
    'django_summernote',
    'captcha',
    'allauth',
    'allauth.account',
]

SITE_ID = 2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'
