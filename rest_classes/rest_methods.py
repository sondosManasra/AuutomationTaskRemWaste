import logging
import requests
import json


class RestApi:
    """
    A class for making API requests.
    This class now contain all methods from REST package which was separated in the several files.
    They are refactored to be more understandable, without code repetition.
    """
    def api_request(self, url, method, body=None, headers=None, status_code=None, data=None, cookies=None,
                    params=None):
        """
        This method makes different API request according to the passed method argument.

        Args:
            url (str): The URL for the request.
            method (str): The HTTP method (POST, PUT, PATCH, DELETE, GET, GET_TOKEN).
            body: The body of the request.
            headers: The headers of the request.
            status_code: The status code.
            data: The data for the request.
            cookies: cookies for the request
            params: parameters to be send with the request

        Returns:
            Response: The response of the API request.
        """

        request_arguments = []
        logging.debug(f"Trigger api URL is: {url}")
        # print(f"Trigger api URL is: {url}")
        request = {"POST": self.post_request,
                   "PUT": self.put_request,
                   "PATCH": self.patch_request,
                   "DELETE": self.delete_request,
                   "GET": self.get_request,
                   "GET_TOKEN": self.get_with_token_request
                   }
        if method in ["POST", "PUT", "PATCH"]:
            request_arguments = [url, headers, body, cookies]
        elif method in ["DELETE", "GET"]:
            request_arguments = [url, headers, params]
        elif method in ["GET_TOKEN"]:
            request_arguments = [url, data, headers, cookies, params]
        response = request[method](*request_arguments)
        logging.debug(f"Response: {response}")
        print(response.text)
        if status_code:
            logging.debug(f"Status code: {response.status_code}")
            return response.status_code, response
        return response

    @staticmethod
    def post_request(url, headers, body, cookies):
        response = requests.post(url, headers=headers, data=json.dumps(body), cookies=cookies)
        return response

    @staticmethod
    def put_request(url, headers, body, cookies):
        response = requests.put(url, headers=headers, data=json.dumps(body), cookies=cookies)
        return response

    @staticmethod
    def patch_request(url, headers, body, cookies):
        response = requests.patch(url, headers=headers, data=json.dumps(body), cookies=cookies)
        return response

    @staticmethod
    def delete_request(url, headers, params=None):
        response = requests.delete(url, headers=headers, params=params)
        return response

    @staticmethod
    def get_request(url, headers, params=None):
        response = requests.get(url, headers=headers, params=params)
        return response

    @staticmethod
    def get_with_token_request(url, data, headers, cookies, params):
        response = requests.get(url + data, headers=headers, cookies=cookies, params=params)
        return response

