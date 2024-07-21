from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-+i=9*#ou@q6g^hv*&!q#5dy-he&r51jxh@07s3%_aj9m7=bt)m"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["https://thedatamine.site", "http://thedatamine.site", "thedatamine.site", "156.155.253.131", "localhost", "127.0.0.1"]

CSRF_TRUSTED_ORIGINS = ["https://thedatamine.site", "http://thedatamine.site"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
