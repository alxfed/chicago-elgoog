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


'''
chicago = maps_client.geocode('Chicago, IL, USA')[0]
geom = chicago['geometry']
location = geom['location']
place_id = chicago['place_id']
'''

# the cycle
location = {'lat': 41.8781136, 'lng': -87.6297982}
next_token = 'first_page'
results = []

while next_token:
    if next_token.startswith('first_page'):
        result = maps_client.places(query="McDonald's",
                                        location=location,
                                        radius=50000)
        results = result['results']
        next_token = result.get('next_page_token')
        time.sleep(2)
    else:
        result = maps_client.places(query="McDonald's",
                                        location=location,
                                        radius=50000,
                                        page_token=next_token)
        results.extend(result['results'])
        next_token = result.get('next_page_token')
        time.sleep(2)


print(len(results))
