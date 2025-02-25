'''The weather.gov API allows us to query specific states
and it returns the stations information for that entire state (yes,
it is very long, I have set the limit to 5, the default is 500!)

See the documentation for this endpoint (and all other endpoints) at 
https://www.weather.gov/documentation/services-web-api'''

import requests
import json

state = "NY"
query_stations = f"https://api.weather.gov/stations?state={state}&limit=5"

# request = requests.get(query_stations)
# output = request.json()
# print(json.dumps(output, indent=3))
