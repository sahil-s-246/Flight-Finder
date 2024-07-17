import requests
import configparser
config = configparser.read("")
TEQ_API_KEY = config["flidat"]["teq"]
TEQ_ENDPOINT_LOC = "https://api.tequila.kiwi.com/locations/query"


class FlightSearch:
    def __init__(self):
        self.result = None

    def get_iata_code(self, city):

        headers = {
            "apikey": TEQ_API_KEY
        }

        params = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(url=TEQ_ENDPOINT_LOC, headers=headers, params=params)
        self.result = response.json()["locations"][0]["code"]
        return self.result
        # each["iataCode"] = response.json()["locations"]
    # This class is responsible for talking to the Flight Search API.
