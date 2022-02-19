import requests


class FlightSearch:
    def __init__(self):
        self.endpoint = "https://tequila-api.kiwi.com/locations/query"
        self.api_key = "VeTiYn5fldaphRDR7YtuR4VPF3QtwNyP"
        self.list = []

        # This class is responsible for talking to the Flight Search API

    def request(self, sheet_places):
        for place in sheet_places:
            print(place)
            headers = {
                "apikey": self.api_key,
            }
            parameters = {
                "term": place,
                "location_types": "city",
            }
            response = requests.get(self.endpoint, params=parameters, headers=headers)
            self.list.append(response.json()["locations"][0]["code"])
        return self.list
