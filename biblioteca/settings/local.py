from .base import *


DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbbiblioteca',
        'USER': 'castillo',
        'PASSWORD': 'cursopro',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATIC_URL = 'static/'
