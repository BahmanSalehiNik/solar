import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'MAGNESITA_SECRET_KEY'
    DEBUG = True
    CSRF_ENABLED = False


SOLAR_API_URL = 'https://api.le-systeme-solaire.net/rest/bodies'

KILOMETER_TO_MILE_CONSTANT = 0.621371