from .base import *
import os

DEBUG = False
SECRET_KEY='fhy2mklv8hj8*0@0-4#rp4^%a)tp&=q29l9zf51w@+na7c#lz_'
ALLOWED_HOSTS=['localhost','rocketman.vn','*']

cwd = os.getcwd()

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache",
    }
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "rocketman",
        "USER":'rocketman',
        "PASSWORD":'q5WtD1ChaGvzTa8',
        "HOST":'localhost',
        "PORT":'',
    }
}



import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://bfbc0986dd8c4e6599498251a636b473@o4505351520059392.ingest.sentry.io/4505351523532800",
    integrations=[
        DjangoIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)





try:
    from .local import *
except ImportError:
    pass
