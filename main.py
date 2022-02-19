from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

manage_tool = DataManager()
sheet_data = manage_tool.data
sheet_prices = manage_tool.prices
sheet_places = manage_tool.places
sheet_id = manage_tool.id

api_kiwi = FlightSearch()
places_info = api_kiwi.request(sheet_places)
# for code in places_info:
#     manage_tool.update(code)
data = FlightData()
available_flights = data.get_flights(places_info)

# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
