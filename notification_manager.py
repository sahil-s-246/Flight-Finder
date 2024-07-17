from twilio.rest import Client
from datetime import datetime, timedelta
import smtplib
import configparser
config  = configparser.read("val.cfg")
my_mail = config["notiman"]["mail"]
password = config["notiman"]["pass"]


class NotificationManager:
    def __init__(self, details, stopovers, via_city):
        self.details = details
        self.account_sid = config["notiman"]["tsid"]
        self.auth_token = config["notiman"]["tauth"]
        self.message = None
        self.stopovers = stopovers
        self.via_city = via_city
        self.departure_date = self.details['utc_departure'].split("T")[0]
        dept_obj = datetime.strptime(self.departure_date, "%Y-%m-%d")
        arrival_obj = dept_obj + timedelta(days=self.details['nightsInDest'])
        self.arrival = arrival_obj.strftime("%Y-%m-%d")

    # This class is responsible for sending notifications with the deal flight details.
    # "utc_arrival": "2021-04-02T13:07:00.000Z"

    def send_msg(self):

        self.message = f"""Low Price alert!\n\n Only ₹{self.details['price']} to fly from {self.details["route"][0]
            ['flyFrom']}-{self.details["route"][0]['cityFrom']} to {self.details["route"][1]['flyTo']}-{self.details
        ["route"][1]['cityTo']} from{self.departure_date} to {self.arrival}  """

        if self.stopovers > 0 and self.via_city != self.details["cityTo"]:
            self.message += f"The flight has {self.stopovers} stopover(s), via {self.via_city}."
        else:
            self.message.replace(f"{self.details['route'][1]['flyTo']}-{self.details['route'][1]['cityTo']}",
                                 f"{self.details['route'][0]['flyTo']}-{self.details['route'][0]['cityTo']}")

        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
                body=self.message,
                from_=config["notiman"]["tnum"],
                to=config["notiman"]["mynum"]
        
                )
        print(message.status)

    def send_mail(self, mail, link):
        with smtplib.SMTP("smtp-mail.outlook.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)

            connection.sendmail(from_addr=my_mail,
                                to_addrs=mail,
                                msg=f"Subject:New Low Price Flight!\n\n{self.message}\n"
                                    f"{link}".encode('utf-8'))


