import math

import requests


SOLAR_API_URL = 'https://api.le-systeme-solaire.net/rest/bodies'
KILOMETER_TO_MILE_CONSTANT = 0.621371


def get_data_from_external_api(api_url):
    response = requests.get(api_url)
    return response.json()


class AsteroidDataCollector:
    def __init__(self, planet_name_to_compare='Vénus', *args, **kwargs):
        self.asteroid_raw_data = None
        self.solar_data = get_data_from_external_api(SOLAR_API_URL)
        self.filter_all_asteroid_data()
        self.final_data = None
        self.planet_to_compare_name = planet_name_to_compare

    def filter_all_asteroid_data(self):
        asteroid_data = [d for d in self.solar_data['bodies'] if d.get('bodyType') == 'Asteroid']
        self.asteroid_raw_data = asteroid_data
        return asteroid_data

    def get_planet_to_compare_data(self):
        planet_data = [p for p in self.solar_data['bodies'] if p.get('name')==self.planet_to_compare_name]
        if len(planet_data) > 0:
            return planet_data[0]
        return None

    def calculate_planet_mass(self):
        planet_data = self.get_planet_to_compare_data()
        if planet_data:

            mass = planet_data['mass']['massValue'] * math.pow(10, planet_data['mass']['massValue'])
            return mass
        return None

    def filter_asteroids_bigger_than_planet(self):
        mass = self.calculate_planet_mass()
        dropped_none_mass_asteroids_list = [a for a in self.asteroid_raw_data if a['mass']]
        asteroids_list = [a for a in dropped_none_mass_asteroids_list if
                          a['mass']['massValue'] * math.pow(10, a['mass']['massValue']) > mass]
        return asteroids_list

    def output_data(self):
        return self.filter_asteroids_bigger_than_planet()


if __name__ == '__main__':

    a_data = AsteroidDataCollector('Vénus')
    print(a_data.asteroid_raw_data)
    print(a_data.get_planet_to_compare_data())
    print(len(a_data.filter_asteroids_bigger_than_planet()))
