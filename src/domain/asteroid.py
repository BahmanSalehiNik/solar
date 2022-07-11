import requests


SOLAR_API_URL = 'https://api.le-systeme-solaire.net/rest/bodies'
KILOMETER_TO_MILE_CONSTANT = 0.621371


def get_data_from_external_api(api_url):
    response = requests.get(api_url)
    return response.json()


class AsteroidDataCollector:
    def __init__(self):
        pass

{"id":"quaoar","name":"(50000) Quaoar",
 "englishName":"50000 Quaoar","isPlanet":false,
 "moons":[{"moon":"Weywot","rel":"https://api.le-systeme-solaire.net/rest/bodies/weywot"}],
 "semimajorAxis":6489054000,"perihelion":6266487000,"aphelion":6711620000,"eccentricity":0.03400,
 "inclination":7.98400,"mass":{"massValue":1.00000,"massExponent":21},"vol":null,"density":1.00000,
 "gravity":0.00000,"escape":0.00000,"meanRadius":675.00000,"equaRadius":0.00000,"polarRadius":0.00000,
 "flattening":0.00000,"dimension":"","sideralOrbit":104347.57500,"sideralRotation":0.00000,
 "aroundPlanet":null,"discoveredBy":"Chadwick Trujillo, Michael E. Brown",
 "discoveryDate":"04/06/2002","alternativeName":"2002 LM60","axialTilt":0,
 "avgTemp":0,"mainAnomaly":0.00000,"argPeriapsis":0.00000,
 "longAscNode":0.00000,"bodyType":"Asteroid",
 "rel":"https://api.le-systeme-solaire.net/rest/bodies/quaoar"}