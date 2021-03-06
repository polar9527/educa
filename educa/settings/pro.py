from .base import *

DEBUG = False

ADMINS = (
    ('Polar Sun', 'polar9527@163.com'),
)

ALLOWED_HOSTS = ['educa.com', 'www.educa.com', '127.0.0.1', 'django.educa.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'educadb',
        'USER': 'educa',
        'PASSWORD': '888888',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True