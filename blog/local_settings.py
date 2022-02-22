DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogdatabase',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '172.17.0.2',
        'PORT': '3306',
    }
}

SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = None
SESSION_COOKIE_SECURE = None
CSRF_COOKIE_SECURE = None