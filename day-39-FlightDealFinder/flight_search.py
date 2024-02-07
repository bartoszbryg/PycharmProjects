from flight_data import FlightData


class FlightSearch:
    def __init__(self, destination_city, data_manager):

        self.flight_data = FlightData(destination_city)
        self.data_manager = data_manager

        self.current_price_in_template = [row["lowestPrice"] for row in self.data_manager.flight_data_in_template if row["city"] == destination_city][0]
        self.current_lowest_price = None

    def find_the_lowest_price_in_flight_data(self):
        for flight in self.flight_data.flight_data:
            if self.current_lowest_price is None:
                self.current_lowest_price = int(flight["price"])

            if int(flight["price"]) < self.current_lowest_price:
                self.current_lowest_price = int(flight["price"])

    def compare_lowest_price_with_data_in_template(self):
        return self.current_lowest_price < self.current_price_in_template
