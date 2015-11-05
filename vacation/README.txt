The script will run by typing "python vacation.py cities.txt" into the terminal. cities.txt can be the name of whichever file has the list 
of cities in it. If the flag "--k" is added, it will give the distance in kilometers, eg. "python vacation.py cities.txt --k". The default
is miles. 

I chose Python mainly because I've been using the language a lot recently and am most comforatable with it right now. 
Additionally, I knew I could easily find the correct packages and test quickly. I used the package geopy 
(which is installed with "pip install geopy" if you wanna test)

I first parsed the arguments coming in. the pytho I just did this manually as the arguments are not too complicated. Then I used the python
package geopy to find the latitude and longitude of each of the city locations. I stored the city, coordinate locations in an array. I didn't
use a dictionary as the cities needed to be ordered. Then based off these coordinates I found the distance between successive cities again
using the geopy package, formatted them and printed them out. I didn't feel the need to store the distances between each of the cities
as it seemed like a redundant step. The coordinates are the important piece of data and more can be done with the coordinates. 

I was looking into adding options for modes of travel. Geopy uses the Google Maps API, so I was going to use this to find the distances
for other modes of transportation. I also thought about optimized travel. This problem is close to the traveling salesman problem, but not
quite. I thought I could possibly use Dijkstra's shortest path algorithm to find the shortest path from each city to another, then search
through these shortest paths to find the shortest overall path.