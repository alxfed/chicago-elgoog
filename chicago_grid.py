'''
geo-grid for Maps API search
'''
import csv

top = 42.16
right = 87.51

init_lat = 41.4
lat_step = .018 # 2000m
init_lng = -88.3
lng_step = .024 # 2000m
indx = 1

lat = init_lat
with open('chicago_grid.csv', 'w') as csvfile:
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