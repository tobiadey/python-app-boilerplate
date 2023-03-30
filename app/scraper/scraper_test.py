from unittest import TestCase

from app.scraper.scraper import create_app


class TryTesting(TestCase):
    def test_create_app(self):
        res = create_app()
        self.assertTrue(res == "Hello from scraper")
