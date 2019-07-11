'''
https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=YOUR_API_KEY
'''
import os
import requests
import urllib.request, json


token = os.environ['API_TOKEN']

#with urllib.request.urlopen('https://maps.googleapis.com/maps/api/place/textsearch/json?query=McDonald\'s+Chicago&fields=formatted_address,name&key='+token) as url:
#    data = json.loads(url.read().decode())

property_name = '100 Forest Place, Oak Park, IL'


r = requests.get(url='https://maps.googleapis.com/maps/api/place/findplacefromtext/json?query=100+Forest+Place+Oak+Park+IL%20&key=token')

# # r2 = requests.get(url='https://maps.googleapis.com/maps/api/place/findplacefromtext/json?query=McDonald\'s%20&key=token&radius=50000')

# https://maps.googleapis.com/maps/api/place/radarsearch/output?parameters


# r3 = requests.get(url='https://maps.googleapis.com/maps/api/place/textsearch/json?query=McDonald\'s+Chicago&key='+token)

'''
Google API fetches the 20 Result in one page suppose you want to use the next page 20 result then we use the next_page_token from google first page xml as a result.

1)  https://maps.googleapis.com/maps/api/place/search/xml?location=Enter latitude,Enter Longitude&radius=10000&types=store&hasNextPage=true&nextPage()=true&sensor=false&key=Enter Google_Map_key

in second step you use the first page's next_page_token data

2)https://maps.googleapis.com/maps/api/place/search/xml?location=Enter Latitude,Enter Longitude&radius=10000&types=store&hasNextPage=true&nextPage()=true&sensor=false&key=enter google_map_key &pagetoken="Enter the first page token Value"

'''

a = r3.json()
len = len(a['results'])
print(len)
results = a['results']

for result in results:
    print(result)

print('ok')