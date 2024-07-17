import requests
import configparser
config = configparser.read("val.cfg")

# from pprint import pprint

SHEETY_ENDPOINT = config["datman"]["SHEETY_ENDPOINT"]
sheety_headers = {
    "Authorization": config["datman"]["Auth"]

                }
SHEETY_ENDPOINT_users =config["datman"]["user_endpoint"]


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.prices = None
        self.get_response = None
        self.put_response = None
        self.user_emails = None
        self.get_uresponse = None

    def get_prices(self):
        self.get_response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers)

        self.prices = self.get_response.json()['prices']
        return self.prices

    def get_users(self):
        self.get_uresponse = requests.get(url=SHEETY_ENDPOINT_users, headers=sheety_headers)
        self.user_emails = self.get_uresponse.json()["users"]
        return self.user_emails

    def update_sheet(self, city_code, city):

        sheety_upt_params = {
            "price": {
                "iataCode": city_code
                # "lowestPrice": city_code
            }
        }
        self.put_response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=sheety_upt_params)

