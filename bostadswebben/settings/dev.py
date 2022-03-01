from .base import *
import mimetypes

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vma@@7+g3h1igf#t3s)=9i!unr=$kkq)(%a#^gb%=tudp1z&ej'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += [
    # "debug_toolbar",
    'wagtail.contrib.styleguide',

]


# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

# INTERNAL_IPS = ("127.0.0.1", "127.17.0.1",)
# # this is the main reason for not showing up the toolbar
# mimetypes.add_type("application/javascript", ".js", True)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}


try:
    from .local import *
except ImportError:
    pass
