from flask_testing import TestCase
from app import app as base_app


class TestApi(TestCase):
    def setUp(self) -> None:
        app = self.create_app()
        self.test_client = app.test_client()

    def create_app(self):
        return base_app

    def test_planet(self):
        res_post = self.test_client.post('/solar/planet')
        self.assertEqual(res_post.status_code, 201)

        res_get = self.test_client.get('/solar/planet')
        self.assertEqual(res_get.status_code, 200)

    def test_asteroid(self):
        res_post = self.test_client.post('/solar/asteroid')
        self.assertEqual(res_post.status_code, 201)

        res_get = self.test_client.get('/solar/asteroid')
        self.assertEqual(res_get.status_code, 200)