from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-+i=9*#ou@q6g^hv*&!q#5dy-he&r51jxh@07s3%_aj9m7=bt)m"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["https://databet.co.za", "http://databet.co.za", "databet.co.za", "156.155.253.16"]

CSRF_TRUSTED_ORIGINS = ["https://databet.co.za", "http://databet.co.za"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

STATICFILES_DIRS = [
    "/var/www/api.thedatamine.io/thedatamine/static/",
]

STATIC_ROOT = "/var/www/api.thedatamine.io/static/"

MEDIA_ROOT = "/var/www/api.thedatamine.io/media/"


try:
    from .local import *
except ImportError:
    pass
