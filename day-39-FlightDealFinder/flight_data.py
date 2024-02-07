import requests
import datetime as dt
from data_manager import get_iata_code, HEADER

# from requests.adapters import HTTPAdapter
# from urllib3.util.retry import Retry


KIWI_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
KIWI_API_KEY = "KIWI_API"


stored_flight_data = None


def get_city_location_by_ip():
    try:
        # session = requests.Session()
        # retry = Retry(connect=3, backoff_factor=0.5)
        # adapter = HTTPAdapter(max_retries=retry)
        # session.mount('http://', adapter)
        # session.mount('https://', adapter)
        #
        # ip_response = session.get("https://ipinfo.io/json")
        ip_response = requests.get("https://ipinfo.io/json")
        ip_data = ip_response.json()
        city = ip_data.get("city")
        return city
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_tomorrow_and_next_date():
    tomorrow_date = dt.datetime.now() + dt.timedelta(days=1)
    next_date = tomorrow_date + dt.timedelta(days=4 * 30)

    return tomorrow_date.date().strftime("%d/%m/%Y"), next_date.date().strftime("%d/%m/%Y")


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, destination_city):

        self.current_city = get_city_location_by_ip()
        self.destination_city = destination_city

        self.current_city = get_iata_code(self.current_city)
        self.destination_city = get_iata_code(self.destination_city)

        self.formatted_tomorrow_date, self.formatted_next_date = get_tomorrow_and_next_date()

        print(self.current_city)
        print(self.destination_city)
        print(self.formatted_tomorrow_date)
        print(self.formatted_next_date)

        flight_params = {
            "fly_from": self.current_city,
            "fly_to": self.destination_city,
            "date_from": self.formatted_tomorrow_date,
            "date_to": self.formatted_next_date
        }

        self.response = requests.get(url=KIWI_SEARCH_ENDPOINT, params=flight_params, headers=HEADER)
        self.flight_data = self.response.json()["data"]
        self.stored_flight_data = None

    def store_flight_data(self, price):
        for flight in self.flight_data:
            if flight["price"] == price:
                self.stored_flight_data = flight




