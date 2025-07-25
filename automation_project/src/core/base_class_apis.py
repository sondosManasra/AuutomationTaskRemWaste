from core.main_functions import MainFunctions
from rest_classes.rest_methods import RestApi
headers = {
    "Content-Type": "application/json",
    "Content-Length": "<calculated when request is sent>",
    "Host": "<calculated when request is sent>",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Cache-Control": "no-cache"
}


class BaseClassAPIs:

    def __init__(self):
        self.main_functions = MainFunctions()
        self.rest_apis = RestApi()
        self.body_data_file_path = '../config_files/body_data_apis.json'
        self.expected_results_file = '../config_files/expected_results_apis.json'
        self.config_path = '../config_files/project.properties'

    def get_config_value(self, key):
        config_value = self.main_functions.read_config(self.config_path, key)
        return config_value

    def general_do_apis_flow(self, route, method, body, expected_results_key):
        url = f"{self.get_config_value('local_host_backend')}{route}"
        body_data, expected_results = self.main_functions.general_get_api_json_data(body, expected_results_key,
                                                                                    self.body_data_file_path,
                                                                                    self.expected_results_file)
        status_code, response = self.rest_apis.api_request(url, method, body=body_data, headers=headers,
                                                           status_code=True, data="")
        return status_code, response, expected_results
