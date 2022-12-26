import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from .base import *

ALLOWED_HOSTS = ['www.gotya.com', '18.185.97.220', '127.0.0.1']
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gotya_db_dv',
        'USER': 'root',
        'PASSWORD': env('MY_PASSWORD'),
        'HOST': 'host.docker.internal',
        'PORT': '3306',
    }
}
