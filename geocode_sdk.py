import googlemaps
import os
import time

token = os.environ['API_TOKEN']

try:
    maps_client = googlemaps.Client(key=token, timeout=10,
                                    retry_timeout=2,
                                    queries_per_second=1,
                                    retry_over_query_limit=True)
except ValueError:
    print('The API token does not work')
    exit(code=246)

chicago = maps_client.geocode('Chicago, IL, USA')[0]
geom = chicago['geometry']
location = geom['location']
place_id = chicago['place_id']

print(location)