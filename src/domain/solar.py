import requests
import unicodedata

SOLAR_API_URL = 'https://api.le-systeme-solaire.net/rest/bodies'


def get_data_from_external_api(api_url):
    response = requests.get(api_url)
    return response.json()


def filter_all_planet_data(solar_data):
    all_planet_data = [item for item in solar_data['bodies'] if item.get("isPlanet")]
    return all_planet_data


def planet_specific_moons(planet_specific_data):
    moons = planet_specific_data.get('moons', None)
    return moons


def filter_moon_data(solar_data, moon_id):
    moon_data = [item for item in solar_data['bodies'] if item.get("id") in [moon_id, strip_accents(moon_id.lower())]]
    return moon_data


def detailed_planet_moons_data(solar_data, planet_specific_data):
    planet_moon_data = planet_specific_moons(planet_specific_data)
    detailed_data = [filter_moon_data(solar_data, item['moon']) for item in planet_moon_data]
    return detailed_data




def strip_accents(text):
    """ for converting Latin letters to English i.e: é --> e"""
    return ''.join(char for char in
                   unicodedata.normalize('NFKD', text)
                   if unicodedata.category(char) != 'Mn')


if __name__ == '__main__':
    url = SOLAR_API_URL
    #params = {'filter[]':'isPlanet,neq,false'}
    data = get_data_from_external_api(url)#, params)
    planet_data = filter_all_planet_data(data)
    uranus_data = planet_data[0]
    print(uranus_data['moons'])
    uranus_moons_data = planet_specific_moons(uranus_data)
    # print(uranus_moons_data)
    # print(filter_moon_data(data, 'Ariel'))
    print(detailed_planet_moons_data(data, uranus_data))