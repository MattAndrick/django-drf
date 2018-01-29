from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY' , default='f8$t@ah-8n9fh%1@(&^or#8((8x#+h0^6!#spyf6egk1gs!si7')

DEBUG = env.bool('DJANGO_DEBUG', default=True)