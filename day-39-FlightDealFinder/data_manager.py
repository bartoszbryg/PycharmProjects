import requests

BEARER_TOKEN = "jkhl13h123h23ljskjad2132spdhau"
SHEETY_ENDPOINT = "https://api.sheety.co/a3918f6f853a5503c7151fca01b21656/flightDeals/arkusz1"

KIWI_LOCATION_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
KIWI_API_KEY = "ZcPV6_RF39_LzHWy3lt1Jp9jkCQ2bsiI"

HEADER = {
    "apikey": KIWI_API_KEY
}

num_of_row = 1


def get_iata_code(city_name):
    params = {
        "term": city_name
    }

    resp = requests.get(url=KIWI_LOCATION_ENDPOINT, headers=HEADER, params=params)
    resp.raise_for_status()
    return resp.json()['locations'][0]['code']


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.headers = {
            'Authorization': f'Bearer {BEARER_TOKEN}'
        }
        self.response = requests.get(url=SHEETY_ENDPOINT, headers=self.headers)
        print(self.response.json())
        self.flight_data_in_template = self.response.json()["arkusz1"]

    def add_iata_codes_to_template(self):
        global num_of_row
        for flight in self.flight_data_in_template:
            num_of_row += 1
            if len(flight["iataCode"]) == 0:
                iata_code = get_iata_code(flight["city"])
                row_config = {
                    "arkusz1": {
                        "iataCode": iata_code
                    }
                }
                re = requests.put(url=f"{SHEETY_ENDPOINT}/{num_of_row}", json=row_config, headers=self.headers)
                print(re.text)

    def change_price(self, city, price):
        id = [flight["id"] for flight in self.flight_data_in_template if city == flight["city"]][0]
        row_config = {
            "arkusz1": {
                "lowestPrice": price
            }
        }
        requests.put(url=f"{SHEETY_ENDPOINT}/{id}", json=row_config, headers=self.headers)



