from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-+i=9*#ou@q6g^hv*&!q#5dy-he&r51jxh@07s3%_aj9m7=bt)m"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["http://127.0.0.1:8000/", "http://localhost:8000/", "localhost", "127.0.0.1"]

CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:8000/", "http://localhost:8000/"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_ROOT = os.path.join(BASE_DIR, "media")



try:
    from .local import *
except ImportError:
    pass
