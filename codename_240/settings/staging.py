import os

from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "codename_240",
        "USER": "postgres",
        "HOST": "localhost",
        "PASSWORD": os.environ["DB_PASSWORD"],
        "PORT": 5432
    }
}
