from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import pywhatkit
import geocoder

import webbrowser as web

def map(place):
    url = "https://www.google.com/maps/place/" + str(place)
    web.open(f"{url}")

