from .base import *

DEBUG = True #poner en false para q no aparezca la "ventana de errores" de django

ALLOWED_HOSTS = ['neurodata.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
