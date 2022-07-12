import math
from unittest import TestCase
from src.domain.planets import PlanetsDataCollector
from tests.tets_unit.data.planet_data import data


class TestPlanetDataCollector(TestCase):
    def setUp(self) -> None:
        self.planets_obj = PlanetsDataCollector()

    def test_second_smallest_moon(self):
        """ uranus second smallest moon is "trinculo" with a mass of 3.9 * 10^15
        ref: https://en.wikipedia.org/wiki/Moons_of_Uranus """

        uranus_data = data[0]
        uranus_sorted_moon_data = self.planets_obj.sort_planet_moons_data_by_mass(uranus_data)
        uranus_second_small_moon = self.planets_obj.calculate_planet_moon_by_position(uranus_sorted_moon_data, 1)
        self.assertEqual(uranus_second_small_moon, 3.9 * math.pow(10, 15))

    def test_filter_all_planet_data(self):
        filtered_data = self.planets_obj.filter_all_planet_data()
        for d in filtered_data:
            self.assertEqual(d['isPlanet'], True)

    def test_planet_specific_moons(self):
        planet_data = self.planets_obj.planets_raw_data[0]
        moons_data =self.planets_obj.planet_specific_moons(planet_data)
        for d in moons_data:
            self.assertIsNotNone(d['moon'])

    def test_valid_filter_moon_data(self):
        moon_data = self.planets_obj.filter_moon_data('Ariel')
        self.assertIsNotNone(moon_data)
        self.assertEqual(moon_data['name'], 'Ariel')

    def test_invalid_filter_moon_data(self):
        with self.assertRaises(KeyError):
            moon_data = self.planets_obj.filter_moon_data('earth')
            self.assertIsNotNone(moon_data)

    def test_extract_planet_moons_data(self):
        planet_data = self.planets_obj.planets_raw_data[0]
        planet_moon_data = self.planets_obj.extract_planet_moons_data(planet_data)
        self.assertIsNotNone(planet_moon_data)
        for d in planet_moon_data:
            self.assertIsInstance(d, dict)
            self.assertIn('id', d.keys())