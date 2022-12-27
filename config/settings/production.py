import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from .base import *

ALLOWED_HOSTS = ['www.gotya.com', '18.185.97.220', '127.0.0.1']
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",  # set in docker-compose.yml
        "PORT": 5432,  # default postgres port
    }
}
## GRANT ALL PRIVILEGES on *.* to 'root'@'%' IDENTIFIED BY 'password';