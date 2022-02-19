import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.google_sheet = "https://api.sheety.co/20239f610f76006a9ea9ac1260e0c27d/flightDeals/hoja1"
        self.data = requests.get(self.google_sheet).json()["hoja1"]
        self.places = []
        self.prices = []
        self.id = []
        for i in range(0, len(self.data)):
            self.places.append(self.data[i]["city"])
        for i in range(0, len(self.data)):
            self.prices.append(self.data[i]["lowestPrice"])
        for i in range(0, len(self.data)):
            self.id.append(self.data[i]["id"])
        self.i = 0

    def update(self, code):
        chane = {
            "hoja1": {
                "iataCode": code}
        }
        update = requests.put(
            f"https://api.sheety.co/20239f610f76006a9ea9ac1260e0c27d/flightDeals/hoja1/{self.id[self.i]}",
            json=chane)
        self.i += 1
        print(update.text)
