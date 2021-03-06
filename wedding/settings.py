import os
import configparser
import socket

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'settings.cfg'))

SECRET_KEY = config.get('django', 'secret_key')

ALLOWED_HOSTS = ['mhquavwrva.execute-api.us-east-1.amazonaws.com',
                 'hooks-jorissen.us']

try:
    HOSTNAME = socket.gethostname()
except:
    HOSTNAME = 'localhost'

# Application definition
INSTALLED_APPS = [
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'wedding',
    'phonenumber_field',
    'markupfield',
    'django_extensions',
    'zappa_django_utils'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wedding.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wedding.context_processors.event',
                'wedding.context_processors.base_background',
                'wedding.context_processors.pages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wedding.wsgi.application'


SCHEMA = config.get('lambda', 'db_schema')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': f'-c search_path={SCHEMA}'
        },
        'NAME': config.get('lambda', 'db_name'),
        'USER': config.get('lambda', 'db_user'),
        'PASSWORD': config.get('lambda', 'db_password'),
        'HOST': config.get('lambda', 'db_host'),
        'PORT': '5432',
    }
}

LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

# STATIC_URL = '/static/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_LOCATION = 'content'
AWS_S3_HOST = "s3.us-east-1.amazonaws.com"
AWS_ACCESS_KEY_ID = config.get('corrdyn', 'access_key_id')
AWS_SECRET_ACCESS_KEY = config.get('corrdyn', 'secret_access_key')
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = False
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_STORAGE_BUCKET_NAME = config.get('corrdyn', 'storage_bucket_name')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

STATIC_URL = "/static/"

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

LOGOUT_REDIRECT_URL = "/home"


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config.get('email', 'email_user')
EMAIL_HOST_PASSWORD = config.get('email', 'email_password')
DEFAULT_FROM_EMAIL = config.get('email', 'email_user')
CONTACT_FORM_RECIPIENT_LIST = ['jjorissen52@gmail.com', 'sarahlhooks@gmail.com']


if config.get('local', 'host_name') in HOSTNAME:
    DATABASES = {
        "default": {
            # Add "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "db",
            "USER": "",
            "PASSWORD": "",
            "HOST": "",
            "PORT": "",
        }
    }

    ALLOWED_HOSTS = ["*"]
    DEBUG = True

else:
    STATICFILES_STORAGE = 'wedding.custom_storages.StaticStorage'

# STATICFILES_STORAGE = 'wedding.custom_storages.StaticStorage'