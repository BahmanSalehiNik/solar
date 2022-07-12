from unittest import TestCase
from src.domain.solar_handler import write_list_of_dicts_to_csv
import csv


class TestWriteToCsv(TestCase):
    def test_write_list_of_dicts_to_csv(self):
        dict_1 = {'key1': 'a', 'key2': 'b'}
        dict_2 = {'key1': 'c', 'key2': 'd'}
        write_list_of_dicts_to_csv([dict_1, dict_2], './data/temp_data.csv')
        with open('./data/temp_data.csv') as temp_file:
            temp_data = csv.reader(temp_file)
            self.assertIsNotNone(temp_data)