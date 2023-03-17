'''
Application entry point
'''
# https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html
from app.internal.app import create_app

application = create_app()
