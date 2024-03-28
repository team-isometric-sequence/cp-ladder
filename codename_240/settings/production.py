from .base import *

import dj_database_url


SECRET_KEY = "cf5dc42c56a6fe9aaec6d6222002f4862095a5d032ea2dc1a7e14ea6fd1f1c99"


# pylint: disable=used-before-assignment, undefined-variable
DATABASES["default"] = dj_database_url.parse(
    os.environ["DATABASE_URL"], conn_max_age=600
)
