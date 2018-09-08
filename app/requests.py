import urllib.request,json
from .models import User,Role

def configure_request(app):
    global secret_key
    secret_key = app.config['SECRET_KEY']