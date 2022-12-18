from .base import *

ALLOWED_HOSTS = ['www.gotya.com']
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'prod.sqlite3',
    }
}