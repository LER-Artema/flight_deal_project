from datetime import datetime, timedelta

import requests


class FlightData:
    def __init__(self):
        self.tomorrow = datetime.now() + timedelta(days=1)
        self.endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.api_key = "VeTiYn5fldaphRDR7YtuR4VPF3QtwNyP"
        self.period = datetime.now() + timedelta(days=(6 * 30))
        self.list = []

    def get_flights(self, places_info):
        for code in places_info:
            headers = {
                "apikey": self.api_key,
            }
            params = {
                "fly_from": "MEX",
                "fly_to": code,
                "date_from": self.tomorrow.strftime("%d/%m/%Y"),
                "date_to": self.period.strftime("%d/%m/%Y"),
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 0,
                "curr": "GBP"
            }
            flights_info = requests.get(self.endpoint, headers=headers, params=params).json()
            print(flights_info["data"])
            try:
                self.list.insert(0, [flights_info["data"][0]["cityTo"]])
                self.list[0].append(flights_info["data"][0]["price"])
                self.list[0].append(flights_info["data"][0]["cityCodeFrom"])
                self.list[0].append(flights_info["data"][0]["cityCodeTo"])
                self.list[0].append(f"The flight outbound departs in: {flights_info['data'][0]['local_departure']}")
                self.list[0].append(
                    f"The flight inbound departs in: {flights_info['data'][0]['route'][0]['local_arrival']}")
                self.list[0].append(
                    f"Link: {flights_info['data'][0]['deep_link']}")

            except IndexError:
                print(f"There is no available flight to {code}")
        print(self.list)
        return self.list
    # This class is responsible for structuring the flight data.
