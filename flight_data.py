import requests
import datetime as dt
import configparser
config = configparser.read("val.cfg")

tomorrow = dt.datetime.now() + dt.timedelta(days=1)
six_months_after = tomorrow + dt.timedelta(days=180)
SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
TEQ_API_KEY = config["flidat"]["teq"]

headers = {
    "apikey": TEQ_API_KEY
}


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.flight_det = None

    def get_flight_price(self, code, city):
        params = {
            "fly_from": "DEL",
            "fly_to": code,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_months_after.strftime("%d/%m/%Y"),
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "INR",
            "sort": "price",
            "max_stopovers": 1,
            "one_for_city": 1

        }
        resp = requests.get(url=SEARCH_ENDPOINT, params=params, headers=headers)
        try:
            self.flight_det = resp.json()["data"][0]

        except IndexError:

            print(f"No flight found from Delhi(DEL) to {city}({code})")
            return None

        else:
            return self.flight_det
