"""
Django settings for testP project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')6+vf9(1tihg@u8!+(0abk+y*#$3r$(-d=g5qhm@1&lo4pays&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'my.hackupc.com', '127.0.0.1', ]

# Application definition

INSTALLED_APPS = [
    'jet',
    'jet.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'register',
    'checkin',
    'reimbursement',
    'table',
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['register/templates', 'app/templates', 'checkin/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',

            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + '/staticfiles'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, os.path.join('app', "static")),
]

if os.environ.get('EMAIL_DEBUG', None) and DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = 'tmp/email-messages/'
else:
    EMAIL_BACKEND = "sgbackend.SendGridBackend"
    SENDGRID_API_KEY = os.environ.get('SG_KEY', '.')

MAIL_LISTS_ENABLED = True
if DEBUG:
    MAIL_LISTS_ENABLED = False

# JET
JET_THEMES = [
    {
        'theme': 'default',  # theme folder name
        'color': '#47bac1',  # color of the theme's button in user menu
        'title': 'Default'  # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]
JET_SIDE_MENU_COMPACT = True
JET_MODULE_GOOGLE_ANALYTICS_CLIENT_SECRETS_FILE = os.path.join(BASE_DIR, 'client_secret.json')
JET_INDEX_DASHBOARD = 'app.dashboard.CustomIndexDashboard'

SITE_ID = 1
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_ENABLED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
LOGIN_REDIRECT_URL = 'root'

ACCOUNT_ADAPTER = 'app.utils.AccountAdapter'
ACCOUNT_USER_DISPLAY = lambda x: x.email
ACCOUNT_USERNAME_REQUIRED = False

DEFAULT_FROM_EMAIL = 'HackUPC Team <contact@hackupc.com>'

# Loaded on email templates (except auth ones)
STATIC_KEYS_TEMPLATES = {
    'fb': 'hackupc',
    'twitter': 'hackupc',
    'email': 'contact@hackupc.com',
    'description': 'Join us for BarcelonaTech\'s hackathon. 500 hackers. 36h. March 3rd-5th.',
    # Static url to your logo
    'logo_url': 'https://raw.githubusercontent.com/hackupc/frontend/master/src/images/hackupc-header-blue.png',
    # MailChimp subscribe URL (optional)
    'subscribe_url': '//hackupc.us12.list-manage.com/subscribe/post?u=d49fc444ec7d45ce418dc02d2&amp;id=3aeef9df9d',
    # Live page url
    'live_url': 'https://hackupc.com/live',
    # Issues url, shows up on 500 error
    'issues_url': 'https://github.com/hackupc/backend/issues/new',
    # Regex to match possible organizers emails
    'r_organizer_email': '^.*@hackupc\.com$'

}

REGISTER_APP = {
    'typeform_key': os.environ.get('TP_KEY'),
    'typeform_form': os.environ.get('TP_FORM', 'KaZTUa')
}

REIMBURSEMENT_APP = {
    'typeform_form': os.environ.get('TP_FORM', 'ZrEOYT')
}

EMAIL_SUBJECT_PREFIX = '[HackUPC]'
EVENT_NAME = 'HackUPC'
if DEBUG:
    EVENT_DOMAIN = 'localhost:8000'
else:
    EVENT_DOMAIN = 'my.hackupc.com'
ALLOWED_HOSTS.append(EVENT_DOMAIN)
CURRENT_EDITION = 'Fall 2017'

# Optional, if not set will skip invite.
# Highly recommended to create a separate user account to extract the token from
SLACK = {
    'team': os.environ.get('SL_TEAM', 'hackupctest'),
    # Get it here: https://api.slack.com/custom-integrations/legacy-tokens
    'token': os.environ.get('SL_TOKEN', None)
}

DEFAULT_REIMBURSEMENT = 100
