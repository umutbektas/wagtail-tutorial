from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+a6#^i^kyi0%qxd0$$j^cc9%+9+@$my+w*@=1b)$i0)^vo5gkn'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



"""For Django Debug Tools"""

"""INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar'
]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ("127.0.0.1")
"""
"""For Django Debug Tools"""

# if you want to cache ?  Remove from comment lines
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
#         "LOCATION": os.path.join(BASE_DIR, 'cache')
#     }
# }


INSTALLED_APPS = INSTALLED_APPS + [
    # 'debug_toolbar',
    'django_extensions'
]

try:
    from .local import *
except ImportError:
    pass
