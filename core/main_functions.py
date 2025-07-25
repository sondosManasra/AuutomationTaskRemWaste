import csv
import json
import configparser


class MainFunctions(object):
    def __init__(self):
        """
        Constructor
        """

    @staticmethod
    def get_csv_data(csv_path):
        rows = []
        csv_data = open(str(csv_path),"r", encoding="utf8")
        content = csv.reader(csv_data)
        next(content, None)
        for row in content:
            rows.append(row)
        return rows

    @staticmethod
    def get_json(file_path):
        with open(file_path, 'r') as my_file:
            data = my_file.read()
        obj = json.loads(data)
        return obj

    def read_json(self, file_path, prop):
        obj = self.get_json(file_path)
        return obj[prop]

    def general_get_api_json_data(self, body, expected_results_key, body_file=None, expected_results_file=None):
        """
        This method is in general return expected_result and body request data after reading json data from
        config files
        Args:
            body (str): body to indicate the body key name of each test
            expected_results_key (str): expected_results_key to indicate the expected results key name of each test
            body_file(str):file path for body requests
            expected_results_file(str): file path of the expected results
        Returns:
            body_data(dict): body request data
            expected_result(dict): expected result
        """
        if body:
            body_data = self.read_json(body_file, body)
        else:
            body_data = ""
        if expected_results_key:
            expected_result = self.read_json(expected_results_file,expected_results_key)
        else:
            expected_result = ""
        return body_data, expected_result

    @staticmethod
    def read_config(config_path, key):
        config = configparser.RawConfigParser()
        config.read(config_path)
        value = config.get("DataSection", key)
        return value

