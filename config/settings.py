import os

from decouple import config
from dj_database_url import parse as db_url

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

if not DEBUG:
    ALLOWED_HOSTS = []
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    SESSION_EXPIRE_AT_BROWSER_CLOSE = True
else:
    ALLOWED_HOST = []


# Application definition

INSTALLED_APPS = [
    'users',
    'master',
    'classes',
    'students',
    'teachers',
    'examination',
    'reception',

    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',
    'widget_tweaks',
    'django_countries',
    'multiselectfield',
    'formtools',
    'phonenumber_field',
    'tinymce',
    'import_export',
    'tinymce',
    'import_export',
    'phonenumber_field',
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

ROOT_URLCONF = 'config.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if not DEBUG:
    DATABASES = {
        'default': {
            # 'ENGINE': 'django.db.backends.mysql',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT', cast=int),
            # 'OPTIONS': {
            #     'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
            # },
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Email Configurations
if not DEBUG:
    EMAIL_BACKEND = config('EMAIL_BACKEND')
    EMAIL_HOST = config('EMAIL_HOST')
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    EMAIL_PORT = config('PORT', cast=int)
    EMAIL_USE_SSL = config('PORT', cast=bool)
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
else:
    EMAIL_HOST_USER = 'noreply@example.com'
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_mails')


CRISPY_TEMPLATE_PACK = 'bootstrap4'

AUTH_USER_MODEL = 'users.CustomUser'

LOGOUT_REDIRECT_URL = 'users:login'

LOGIN_URL = 'users:login'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

if not DEBUG:
    STATICFILES_DIRS = [BASE_DIR+"/static", ]

    MEDIA_ROOT = ''
    STATIC_ROOT = ''
else:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


### TINYMCE SETTINGS - START ###

TINYMCE_DEFAULT_CONFIG = {
	'height': 360,
	'width': '100%',
	'cleanup_on_startup': True,
	'custom_undo_redo_levels': 20,
	'selector': 'textarea',
	'forced_root_block_attrs': {
		'class': 'mycontent',
		},
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview
            table lists fullscreen  insertdatetime  nonbreaking
            searchreplace wordcount 
            fullscreen autolink lists  print  hr
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline |
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': False,
    'statusbar': True,
	}
	
### TINYMCE SETTINGS - END ###

## DJANGO IMPORT EXPORT SETTINGS ##

IMPORT_EXPORT_USE_TRANSACTIONS = True