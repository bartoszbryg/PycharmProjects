from data_manager import DataManager
from flight_search import FlightSearch


data_manager = DataManager()
data_manager.add_iata_codes_to_template()

# CHECKING EVERY SINGLE LINE IN TEMPLATE
for row in data_manager.flight_data_in_template:
    flight_search = FlightSearch(row["city"], data_manager)
    flight_search.find_the_lowest_price_in_flight_data()

    if flight_search.compare_lowest_price_with_data_in_template():
        data_manager.change_price(row["city"], flight_search.current_lowest_price)
        flight_search.flight_data.store_flight_data(flight_search.current_lowest_price)
        stored_flight_data = flight_search.flight_data.stored_flight_data
        stored_date_and_time = stored_flight_data["route"][0]["local_departure"].split("T")
        print(f"Low price alert! Only {flight_search.current_lowest_price}EUR to fly from \n"
              f"{stored_flight_data['route'][0]['cityFrom']}-{stored_flight_data['route'][0]['cityCodeFrom']}\n"
              f"to {stored_flight_data['route'][len(stored_flight_data['route'])-1]['cityTo']}-{stored_flight_data['route'][len(stored_flight_data['route'])-1]['cityCodeTo']}, \n"
              f"Flight scheduled for {stored_date_and_time[0]} at {stored_date_and_time[1]}")
        print(f"To book flight use: {stored_flight_data['deep_link']}. \n"
              f"Booking token: {stored_flight_data['booking_token']}")

