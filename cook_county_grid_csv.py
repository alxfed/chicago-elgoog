'''
geo-grid for Maps API search
'''
import csv

top = 42.152
right = -87.51

init_lat = 41.46
lat_step = .018 # 2000m
init_lng = -88.28
lng_step = .024 # 2000m
indx = 1

lat = init_lat
with open('cook_county_grid.csv', 'w') as csvfile:
    gridwriter = csv.writer(csvfile, delimiter=',')
    while lat <= top:
        lng = init_lng
        while lng <= right:
            gridwriter.writerow([indx, lat, lng])
            indx += 1
            lng += lng_step
        lat += lat_step


csvfile.close()
print('ok')