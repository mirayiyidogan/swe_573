from .base import *

ALLOWED_HOSTS = ['*']
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gotya_local',
        'USER': 'root',
        'PASSWORD': env('MY_PASSWORD'),
        'HOST': 'host.docker.internal',
        'PORT': '3306',
    }
}
