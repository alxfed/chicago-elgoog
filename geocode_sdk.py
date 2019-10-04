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

pass

time.sleep(2)
'''

cook_county = maps_client.geocode('Cook County, IL, USA')[0]
geom_cook = cook_county['geometry']
cook_place_id = cook_county['place_id']

time.sleep(2)

'''
cook_conty_place = maps_client.place(place_id=cook_place_id)

time.sleep(2)
'''

'''
result = maps_client.place(query="McDonald's",
                                        location=location,
                                        radius=50000)
        results = result['results']
        next_token = result.get('next_page_token')
        time.sleep(2)
'''

print(location)