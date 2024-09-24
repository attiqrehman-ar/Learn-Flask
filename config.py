import os

class config(object):
    SECRET_KY = os.environ.get('SECRET_KY') or"secret_string"
    