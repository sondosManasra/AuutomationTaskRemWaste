import pytest
from core.base_class_apis import BaseClassAPIs
from core.main_functions import MainFunctions
from dictdiffer import diff
apis_test_data = MainFunctions.get_csv_data('../config_files/api_positive_test.csv')
list_of_ignored = ['id']
headers = {
    "Content-Type": "application/json",
    "Content-Length": "<calculated when request is sent>",
    "Host": "<calculated when request is sent>",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Cache-Control": "no-cache"
}


class APIsTest:
    @pytest.fixture(autouse=True)
    def setup_base(self):
        self.base_class = BaseClassAPIs()

    @pytest.mark.parametrize("test_case_name, route, method, body, expected_status_code,expected_results_key",
                             apis_test_data)
    def test_apis(self, test_case_name, route, method, body, expected_status_code, expected_results_key):
        status_code, response, expected_results = self.base_class.general_do_apis_flow\
            (route, method, body, expected_results_key)
        expected_status_code = int(expected_status_code)
        result = diff(response.json(), expected_results, ignore=set(list_of_ignored))
        list_result = list(result)
        assert status_code == expected_status_code
        assert list_result == [], f"actual results are not equal to expected results: here the differences:" \
            f"{list_result}"
