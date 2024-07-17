"""These flights are from Delhi. Program compares if prices have dropped and accordingly sends a message"""
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from urllib.parse import quote

data_man = DataManager()
sheet_data = data_man.get_prices()
user_data = data_man.get_users()
flight_search = FlightSearch()
details = FlightData()
for each in sheet_data:
    code = flight_search.get_iata_code(each["city"])

    data = details.get_flight_price(code, each["city"])

    if data is None:
        continue

    else:
        notif = NotificationManager(data, stopovers=1, via_city=data["route"][0]["cityTo"])
        # data_man.update_sheet(code, each)
        if each['lowestPrice'] > data["price"]:
            notif.send_msg()

            link = f"https://www.google.com/travel/flights?q=Flights%20to%20{quote(data['route'][1]['cityTo'])}" \
                   f"%20from%20{quote(data['route'][0]['cityFrom'])}%20on%20{notif.departure_date}%20through%20" \
                   f"{notif.arrival}"
            for mail in user_data:
                notif.send_mail(mail=mail["email"], link=link)
                break


# Sample output from API
"""
   {
      "id": "22ee0f6b491f000063ba729a_0",
      "nightsInDest": null,
      "duration": {
        "departure": 11220,
        "return": 0,
        "total": 11220
      },
      "flyFrom": "LGA",
      "cityFrom": "New York",
      "cityCodeFrom": "NYC",
      "countryFrom": {
        "code": "US",
        "name": "United States"
      },
      "flyTo": "MIA",
      "cityTo": "Miami",
      "cityCodeTo": "MIA",
      "countryTo": {
        "code": "US",
        "name": "United States"
      },
      "distance": 1770.31,
      "airlines": [
        "AA"
      ],
      "pnr_count": 1,
      "has_airport_change": false,
      "technical_stops": 0,
      "throw_away_ticketing": false,
      "hidden_city_ticketing": false,
      "price": 69,
      "bags_price": {
        "1": 36.96
      },
      "baglimit": {
        "hand_width": 23,
        "hand_height": 36,
        "hand_length": 56,
        "hand_weight": 10,
        "hold_width": 28,
        "hold_height": 52,
        "hold_length": 78,
        "hold_dimensions_sum": 158,
        "hold_weight": 23
      },
      "availability": {
        "seats": 7
      },
      "facilitated_booking_available": true,
      "conversion": {
        "EUR": 69
      },
      "quality": 142.86648200000002,
      "booking_token": "Eg"
      "fare": {
        "adults": 34.5,
        "children": 34.5,
        "infants": 34.5
      },
      "price_dropdown": {
        "base_fare": 69,
        "fees": 0
      },
      "virtual_interlining": false,
      "route": [
        {
          "fare_basis": "O7ALZNB3",
          "fare_category": "M",
          "fare_classes": "B",
          "fare_family": "",
          "return": 0,
          "bags_recheck_required": false,
          "vi_connection": false,
          "guarantee": false,
          "id": "22ee0f6b491f000063ba729a_0",
          "combination_id": "22ee0f6b491f000063ba729a",
          "cityTo": "Miami",
          "cityFrom": "New York",
          "cityCodeFrom": "NYC",
          "cityCodeTo": "MIA",
          "flyTo": "MIA",
          "flyFrom": "LGA",
          "airline": "AA",
          "operating_carrier": "AA",
          "equipment": "738",
          "flight_no": 1249,
          "vehicle_type": "aircraft",
          "operating_flight_no": "1249",
          "local_arrival": "2021-04-02T09:07:00.000Z",
          "utc_arrival": "2021-04-02T13:07:00.000Z",
          "local_departure": "2021-04-02T06:00:00.000Z",
          "utc_departure": "2021-04-02T10:00:00.000Z"
        }
      ],
      "local_arrival": "2021-04-02T09:07:00.000Z",
      "utc_arrival": "2021-04-02T13:07:00.000Z",
      "local_departure": "2021-04-02T06:00:00.000Z",
      "utc_departure": "2021-04-02T10:00:00.000Z"
    },
"""

