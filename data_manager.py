import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/802ab903566d952628c23c0c93790639/flightDeals/prices"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def update_lowest_prices(self, id, new_flight_price):
        new_price = {
            "price": {
                "lowestPrice": new_flight_price
        }
    }
        response = requests.put(
            url = f"{SHEETY_PRICES_ENDPOINT}/{id}",
            json = new_price
    )
        response.raise_for_status()
        print(response.text)
