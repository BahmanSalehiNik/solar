from unittest import TestCase
from src.conf import KILOMETER_TO_MILE_CONSTANT
from src.domain.asteroids import AsteroidDataCollector


class TestAsteroidDataCollector(TestCase):
    def setUp(self) -> None:
        self.asteroid_obj = AsteroidDataCollector()

    def test_unit_conversion(self):
        self.assertAlmostEqual(1.60934 * KILOMETER_TO_MILE_CONSTANT, 1, places=5)

    def test_filter_all_asteroid_data(self):
        filtered_data = self.asteroid_obj.filter_all_asteroid_data()
        for d in filtered_data:
            self.assertIsNotNone(d)
            self.assertEqual(d['bodyType'], 'Asteroid')

    def test_get_planet_to_compare_data(self):
        planet_data = self.asteroid_obj.get_planet_to_compare_data()
        self.assertIsNotNone(planet_data)
        self.assertEqual(planet_data['name'], self.asteroid_obj.planet_to_compare_name)

    def test_calculate_planet_mass(self):
        mass = self.asteroid_obj.calculate_planet_mass()
        self.assertIsNotNone(mass)
        self.assertIsInstance(mass, float)

    def test_filter_asteroids_bigger_than_planet(self):
        big_list = self.asteroid_obj.filter_asteroids_bigger_than_planet()
        self.assertIsInstance(big_list, list)
        if self.asteroid_obj.planet_to_compare_name == 'Vénus':
            self.assertEqual(len(big_list), 0)

    def test_output_data(self):
        data = self.asteroid_obj.output_data()
        processed_data = self.asteroid_obj.filter_asteroids_bigger_than_planet()
        self.assertEqual(data, processed_data)

    def tearDown(self) -> None:
        self.asteroid_obj = None