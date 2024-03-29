import googlemaps
import os
import time

token = os.environ['API_TOKEN']
addre = 'The Kitchen Studio of Glen Ellyn'
neigh = 'Glen Ellyn, IL'

try:
    maps_client = googlemaps.Client(key=token, timeout=10,
                                    retry_timeout=2,
                                    queries_per_second=1,
                                    retry_over_query_limit=True)
except ValueError:
    print('The API token does not work')
    exit(code=246)

'''
neig = maps_client.geocode(neigh)[0]
geom = neig['geometry']
location = geom['location']
place_id = neig['place_id']
'''
location = {'lat': 41.8781136, 'lng': -87.6297982}

'''
result = maps_client.places(query=addre,
                            location=location,
                            radius=50000)
results = result['results'][0]
address = results['formatted_address']
location = results['geometry']['location']
name = results['name']
place_id = results['place_id']
'''
bias = 'circle:50000@'+str(location['lat'])+','+str(location['lng'])
result = maps_client.find_place(input=addre,
                                input_type="textquery",
                                fields=['place_id'],
                                location_bias=bias)
info = result['candidates'][0]
# address = info['formatted_address']
# name = info['name']
place_id = info['place_id']

contact = maps_client.place(place_id=place_id,
                            fields=['name', 'formatted_address',
                                      'formatted_phone_number', 'website'])['result']

print(result)
