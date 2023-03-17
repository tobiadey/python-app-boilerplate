from unittest import TestCase

from app.internal.main import create_app


class TryTesting(TestCase):
    def test_create_app(self):
        res = create_app()
        self.assertTrue(res == "hello")
