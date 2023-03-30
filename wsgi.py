"""
Application entry point
"""
# https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html
from app.scraper.scraper import create_app


application = create_app()
