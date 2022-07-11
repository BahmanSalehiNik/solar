import os.path
import os
import csv
from flask_restful import Resource
from flask import jsonify
from src.domain.solar_handler import *


class SolarResource(Resource):

    def get(self, solar_type):
        file_path = f'{os.getcwd()}/data/{solar_type}.csv'
        if os.path.exists(file_path):
            with open(file_path) as csv_file:
                csv_reader = csv.DictReader(csv_file)
                json_list = [row for row in csv_reader]
                print(json_list)
                print(type(json_list))
                return json_list, 200

        else:
            return {'no csv is created yet, use POST to save them'}, 404

    def post(self, solar_type):
        solar_obj = handle_solar_data(solar_type)
        csv_data = solar_obj().output_data()
        write_list_of_dicts_to_csv(csv_data, f'{os.getcwd()}/data/{solar_type}.csv')
        return {'data': 'successfully saved solar data'}, 201
