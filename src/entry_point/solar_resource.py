import os.path
import csv
from flask_restful import Resource, reqparse
from flask import jsonify
# from src.domain.planets import PlanetsDataCollector
# from src.domain.asteroids import AsteroidDataCollector
from src.domain.solar_handler import *


class SolarResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('solar-type', type=str, required=True, help='This field is required')

    def get(self, solar_type):
        file_path = f'../data/{solar_type}.csv'
        if os.path.exists(file_path):
            json_array = []
            with open(file_path) as csv_file:
                csv_reader = csv.DictReader(csv_file)
                json_list = [row for row in csv_reader]
                return jsonify(json_list), 200

        else:
            return {'no csv is created yet, use POST to save them'}, 404

    def post(self):
        data = SolarResource.parser.parse_args()
        solar_type = data['solar-type']
        solar_obj = handle_solar_data(solar_type)
        csv_data = solar_obj().output_data()
        write_list_of_dicts_to_csv(csv_data, f'../data/{solar_type}.csv')
        return {'successfully saved solar data'}, 201
