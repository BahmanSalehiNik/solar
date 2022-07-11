import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'MAGNESITA_SECRET_KEY'
    DEBUG = True
    CSRF_ENABLED = False