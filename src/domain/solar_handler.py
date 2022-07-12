import csv
from src.domain.planets import PlanetsDataCollector
from src.domain.asteroids import AsteroidDataCollector
import os

solar_data_type_choices = ['planet', 'asteroid']


def handle_solar_data(solar_data_type):
    if solar_data_type in solar_data_type_choices:
        solar_class = solar_data_handler[solar_data_type]
        return solar_class
    raise ValueError('Unsupported input')


solar_data_handler = {
    'planet': PlanetsDataCollector,
    'asteroid': AsteroidDataCollector
}


def write_list_of_dicts_to_csv(input_data, output_file_name):
    if input_data is not None:
        with open(output_file_name, 'w+') as output_file:
            if len(input_data) > 0:
                dict_writer = csv.DictWriter(output_file, input_data[0].keys())
                dict_writer.writeheader()
                dict_writer.writerows(input_data)
            else:
                writer = csv.writer(output_file)
                writer.writerow(input_data)


if __name__ == '__main__':
    pl = PlanetsDataCollector()
    write_list_of_dicts_to_csv(pl.output_data(), '../data/planets.csv')

    astr = AsteroidDataCollector()
    write_list_of_dicts_to_csv(astr.output_data(), '../data/asteroids.csv')
