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
        uranus_second_small_moon = self.planets_obj.calculate_planet_moon_mass_by_position(uranus_sorted_moon_data, 1)
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

    def test_sort_planet_data_by_mass(self):
        planet_data = self.planets_obj.planets_raw_data[0]
        sorted_data = self.planets_obj.sort_planet_moons_data_by_mass(planet_data)
        l = [dict(item, **{'massInKg': item['mass']['massValue']
                                                          * math.pow(10, item['mass']['massExponent'])})
                                for item in sorted_data]
        self.assertTrue(all(l[i]['massInKg'] <= l[i+1]['massInKg'] for i in range(len(l)-1)))

    def test_calculate_planet_moon_mass_by_position(self):
        """Cupid mass is 3.8 * 10 ^ 15
        ref: https://en.wikipedia.org/wiki/Cupid_(moon)"""

        planet_data = self.planets_obj.planets_raw_data[0]
        sorted_data = self.planets_obj.sort_planet_moons_data_by_mass(planet_data)
        mass = self.planets_obj.calculate_planet_moon_mass_by_position(sorted_data, 0)
        self.assertIsNotNone(mass)
        self.assertIsInstance(mass, float)
        self.assertEqual(mass, 3.8 * math.pow(10, 15))

    def test_process_one_planet_data(self):
        planet_data = self.planets_obj.planets_raw_data[0]
        data = self.planets_obj.process_one_planet_data(planet_data)
        self.assertIsNotNone(data)
        keys_to_check = ['name', 'polarRadius', 'smallest moon mass',
                     'second smallest moon mass', 'biggest moon mass']
        for d in keys_to_check:
            self.assertIn(d, data.keys())

    def test_process_all_planet_data(self):
        data = self.planets_obj.process_all_planet_data()
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertIsInstance(data[0], dict)
        self.assertGreater(len(data), 2)

    def test_output_data(self):
        data = self.planets_obj.output_data()
        processed_data = self.planets_obj.process_all_planet_data()
        self.assertEqual(data, processed_data)

    def tearDown(self) -> None:
        self.planets_obj = None
