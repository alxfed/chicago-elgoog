'''
transforming csv into kml
'''

import csv
import simplekml

inputfile = csv.reader(open('cook_county_grid_opt.csv','r'))
kml=simplekml.Kml()

for row in inputfile:
  kml.newpoint(name=row[0], coords=[(row[2],row[1])])

kml.save('cook_county_grid_opt.kml')

print('ok')