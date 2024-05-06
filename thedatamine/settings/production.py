from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-+i=9*#ou@q6g^hv*&!q#5dy-he&r51jxh@07s3%_aj9m7=bt)m"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["api.thedatamine.io", "https://api.thedatamine.io/" "http://api.thedatamine.io/"]


try:
    from .local import *
except ImportError:
    pass
