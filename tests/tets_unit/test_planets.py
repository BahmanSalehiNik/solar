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

