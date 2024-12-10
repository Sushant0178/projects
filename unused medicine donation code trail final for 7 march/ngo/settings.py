import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'u_ef61bu5c8_%pmh5j@a)*8u4yil4vgu8z=cyn%+mb#5#6zdq0'

DEBUG = True

ALLOWED_HOSTS = ['.vercel.app', '.now.sh']

INSTALLED_APPS = [
    'home.apps.HomeConfig',  # Assuming this is your custom app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'ngo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'ngo.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# STATIC settings
STATIC_URL = '/static/'

# Directory where Django will search for additional static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Assuming your static files are in the 'static' folder
]

# Directory where static files will be collected when 'collectstatic' is run
STATIC_ROOT = os.path.join(BASE_DIR, 'public')  # You can specify this as 'public' or 'staticfiles_build'

# You can change it to 'staticfiles_build' or 'public' as per your project structure
