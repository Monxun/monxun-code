
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'home/templates') 


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lr&ku5&pew+5w)6=eri*@j5(sg1&v&$_=x=o6f$l4_9jt$5!9('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['django.monxuncode.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    
    # APPS
    'home',

    # WIDGET TWEAKS
    'widget_tweaks',

    # AllAuth
#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount',
]

MIDDLEWARE = [
    # WHITENOISE
    'whitenoise.middleware.WhiteNoiseMiddleware',

    # CACHE MIDDLEWARE
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',

    # BOOTSTRAP MIDDLEWARE
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ALL AUTH CONFIG
# AUTHENTICATION_BACKENDS = [

#     # Needed to login by username in Django admin, regardless of `allauth`
#     'django.contrib.auth.backends.ModelBackend',

#     # `allauth` specific authentication methods, such as login by e-mail
#     'allauth.account.auth_backends.AuthenticationBackend',
# ]


SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "none"
LOGIN_REDIRECT_URL = "/biz"


WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    
    'home/static',
    
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


####################################################################
# MEMECACHED CONFIG (Local)

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }

# CACHE_MIDDLEWARE_ALIAS = 'default'
# CACHE_MIDDLEWARE_SECONDS = 10
# CACHE_MIDDLEWARE_KEY_PREFIX = ''


####################################################################
# HEROKU
# django_heroku.settings(locals())




# ####################################################################
# # MEMECACHIER CONFIG(Heroku)

# def get_cache():
#   import os
#   try:
#     servers = os.environ['MEMCACHIER_SERVERS']
#     username = os.environ['MEMCACHIER_USERNAME']
#     password = os.environ['MEMCACHIER_PASSWORD']
#     return {
#       'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
#         # TIMEOUT is not the connection timeout! It's the default expiration
#         # timeout that should be applied to keys! Setting it to `None`
#         # disables expiration.
#         'TIMEOUT': None,
#         'LOCATION': servers,
#         'OPTIONS': {
#           'binary': True,
#           'username': username,
#           'password': password,
#           'behaviors': {
#             # Enable faster IO
#             'no_block': True,
#             'tcp_nodelay': True,
#             # Keep connection alive
#             'tcp_keepalive': True,
#             # Timeout settings
#             'connect_timeout': 2000, # ms
#             'send_timeout': 750 * 1000, # us
#             'receive_timeout': 750 * 1000, # us
#             '_poll_timeout': 2000, # ms
#             # Better failover
#             'ketama': True,
#             'remove_failed': 1,
#             'retry_timeout': 2,
#             'dead_timeout': 30,
#           }
#         }
#       }
#     }
#   except:
#     return {
#       'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
#       }
#     }

# CACHES = get_cache()
