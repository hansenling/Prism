from geopy.geocoders import Nominatim
from geopy.distance import vincenty
import fileinput
import sys
import tsp

def parseinput():
	args = sys.argv[1:]
	readfile = args[0]
	f = open(readfile, 'r')
	cities = []
	units = 'miles'

	while True:
		line = f.readline()
		if line == '':
			break
		cities.append(line)

	
	if '--k' in args:
		units = 'kilometers'

	return cities, units

def getlocations(cities):
	citylocations = []

	for city in cities:
		geolocator = Nominatim()
		locationdata = geolocator.geocode(city)
		location  = (locationdata.latitude, locationdata.longitude)
		citylocations.append((city,location))

	return citylocations

def printdistances(citylocations, units):

	print("Success! Your vacation itinerary is:\n")
	
	for cityindex in range(len(citylocations)-1):
		if units == 'kilometers':
			distance = vincenty(citylocations[cityindex][1], citylocations[cityindex+1][1]).kilometers
		else:
			distance = vincenty(citylocations[cityindex][1], citylocations[cityindex+1][1]).miles
		name1 = citylocations[cityindex][0]
		name2 = citylocations[cityindex+1][0]
		name1=name1.replace('"','')
		name1=name1.replace('\n','')
		name2=name2.replace('"','')
		name2=name2.replace('\n','')
		print("	   {0} -> {1}: {2} {3}".format(name1, name2, distance, units))

def main():
	cities, units = parseinput()
	locations = getlocations(cities)
	printdistances(locations, units)

main()