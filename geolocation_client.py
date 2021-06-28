# Luke Fetchko
# CSCI 236 -- Dr. Wooster
# March 20, 2021
# Program 03 - Geolocation
# Hours spent: 4-5
# Problems encountered: I was using the incorrect formula in my geolocation class and my distances were slightly off,
# after hours of searching I found the correct formula and now understand why it works as such.
# Program now runs as expected with accurate results
# This is a geolocation client program to test the GeoLocation class
from geolocation import GeoLocation
#Create three GeoLocation objects
stash = GeoLocation(34.988889, -106.614444)
abq_studio = GeoLocation(34.989978, -106.614357)
fbi = GeoLocation(35.131281, -106.61263)
# Print string representation of GeoLocation objects
print('the stash is at',str(stash))
print('ABQ studio is at',str(abq_studio))
print('FBI building is at',str(fbi))

print('distance in miles between:')
# Print results from calling distance_from
print('\tstash/studio =',stash.distance_from(abq_studio))
print('\tstash/fbi =',stash.distance_from(fbi))
