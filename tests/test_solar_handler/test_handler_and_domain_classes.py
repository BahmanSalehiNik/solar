from src.domain.planets import PlanetsDataCollector
from src.domain.asteroids import AsteroidDataCollector
from src.domain.solar_handler import handle_solar_data
from unittest import TestCase


class TestHandlerWithPlanet(TestCase):
    def test_handler_returns_correct_type_with_planet_input(self):
        obj = handle_solar_data('planet')
        self.assertEqual(obj, PlanetsDataCollector)

    def test_handler_returns_correct_type_with_asteroid_input(self):
        obj = handle_solar_data('asteroid')
        self.assertEqual(obj, AsteroidDataCollector)
