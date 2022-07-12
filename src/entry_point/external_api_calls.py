import requests


class ExternalApiError(Exception):
    def __init__(self, api_url:str):
        self.api_url = api_url
        super(ExternalApiError, self).__init__()

    def __str__(self):
        return f"Error connecting to external api: {self.api_url}"


def get_data_from_external_api(api_url):
    try:
        response = requests.get(api_url)
        return response.json()
    except Exception as e:
        raise ExternalApiError(api_url)