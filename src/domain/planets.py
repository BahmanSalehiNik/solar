import requests
import math

SOLAR_API_URL = 'https://api.le-systeme-solaire.net/rest/bodies'
KILOMETER_TO_MILE_CONSTANT = 0.621371


def get_data_from_external_api(api_url):
    response = requests.get(api_url)
    return response.json()


class PlanetsDataCollector:
    def __init__(self):
        self.planets_raw_data = None
        self.solar_data = get_data_from_external_api(SOLAR_API_URL)
        self.filter_all_planet_data()
        self.final_data = None

    def filter_all_planet_data(self):
        all_planet_data = [item for item in self.solar_data['bodies'] if item.get("isPlanet")]
        self.planets_raw_data = all_planet_data

    @staticmethod
    def planet_specific_moons(planet_specific_data):
        moons = planet_specific_data.get('moons', None)
        return moons

    def filter_moon_data(self,moon_name):
        moon_data = [item for item in self.solar_data['bodies'] if item.get("name") == moon_name]
        if len(moon_data) > 0:
            return moon_data[0]
        raise KeyError(f'{moon_name} not found')

    def extract_planet_moons_data(self, planet_specific_data):
        planet_moon_data = self.planet_specific_moons(planet_specific_data)
        if planet_moon_data:
            detailed_data = [self.filter_moon_data(item['moon']) for item in planet_moon_data]
            return detailed_data
        return []

    def sort_planet_moons_data_by_mass(self, planet_specific_data):
        planet_moon_data = self.extract_planet_moons_data(planet_specific_data)
        dropped_none_mass_moons = [p for p in planet_moon_data if p['mass']]
        sorted_moon_data =sorted(dropped_none_mass_moons, key=lambda d: (d['mass']['massValue'] *
                                                       math.pow(10, d['mass']['massExponent'])))
        return sorted_moon_data

    @staticmethod
    def calculate_planet_moon_by_position(planet_sorted_moon_data, position):
        try:
            planet = planet_sorted_moon_data[position]
            mass = planet['mass']['massValue'] * math.pow(10, planet['mass']['massExponent'])
            return mass
        except IndexError as e:
            print(str(e))
        return None

    def process_one_planet_data(self, planet_specific_data):
        planet_name = planet_specific_data['name']
        polar_radius = planet_specific_data['polarRadius'] * KILOMETER_TO_MILE_CONSTANT
        sorted_moon_data = self.sort_planet_moons_data_by_mass(planet_specific_data)

        smallest_moon_mass = self.calculate_planet_moon_by_position(sorted_moon_data, 0)
        biggest_moon_mass = self.calculate_planet_moon_by_position(sorted_moon_data, -1)
        second_smallest_moon_mass = self.calculate_planet_moon_by_position(sorted_moon_data, 1)

        data = {'name': planet_name, 'polarRadius': polar_radius,'smallest moon mass': smallest_moon_mass,
                'second smallest moon mass': second_smallest_moon_mass,
                'biggest moon mass': biggest_moon_mass}
        return data

    def process_all_planet_data(self):
        ans_list = []
        for p_data in sorted(self.planets_raw_data, key=lambda d: d['name']):
            ans_list.append(self.process_one_planet_data(p_data))
        self.final_data = ans_list
        return ans_list


if __name__ == '__main__':
    url = SOLAR_API_URL
    p_data = PlanetsDataCollector()
    planet_data = p_data.planets_raw_data
    uranus_data = planet_data[0]
    print(uranus_data['moons'])
    uranus_moons_data = p_data.planet_specific_moons(uranus_data)
    print(len(uranus_moons_data))
    detailed_moon_data = p_data.extract_planet_moons_data(uranus_data)
    print(detailed_moon_data)
    print(p_data.sort_planet_moons_data_by_mass(uranus_data))
    print(p_data.process_one_planet_data(uranus_data))
    print(p_data.process_all_planet_data())
