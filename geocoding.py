
'''This is a sample call from the geocode.maps.co API that allows 
you to transform a physical address into latitude and longitude and
vice versa. I've shared my key that allows for 5000 free calls a day,
it also seems to work without the key.'''

import requests
import json

#it may work without the key just as well
geocode_key = "67bd0ac273845891467941clxf1c8a0"

#address to lat/lon
address = "32+Dawes+Drive+Johnson+City+NY"
add_url = f"https://geocode.maps.co/search?q={address}&api_key={geocode_key}"

#address from lat/lon
lat = "-76.9449999"
lon = "43.11067"
lat_lon_url = f"https://geocode.maps.co/reverse?lat={lat}&lon={lon}&api_key={geocode_key}"

# request = requests.get(add_url)
# output = request.json()
# print(output)