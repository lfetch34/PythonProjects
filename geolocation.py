# This class stores information about a location on Earth.  Locations are
# specified using latitude and longitude.  The class includes a method for
# computing the distance between two locations.

from math import *

RADIUS = 3963.1676  # Earth radius in miles

class GeoLocation:

    # constructs a geo location object with given latitude and longitude
    def __init__(self, latitude, longitude):
        self.__latitude = float(latitude)
        self.__longitude = float(longitude)

    # returns the latitude of this geo location
    def get_latitude(self):
        return self.__latitude

    # returns the longitude of this geo location
    def get_longitude(self):
        return self.__longitude

    # returns a string representation of this geo location
    def __str__(self):
        return "latitude: " + str(self.__latitude) + ", longitude: " + str(self.__longitude)

    # WRITE THIS METHOD FOR AN A
    # returns the distance in miles between this geo location and the given
    # other geo location
    #
    # YOU NEED TO WRITE THIS METHOD; EMAIL ME IF YOU CANNOT FIGURE IT OUT; YOUR GRADE WILL BE LOWER
    def distance_from(self, other):
        lat1 = radians(self.__latitude)
        lat2 = radians(other.get_latitude())
        lon1 = radians(self.__longitude)
        lon2 = radians(other.get_longitude())
        take_acos = sin(lat1) * sin(lat2) + cos(lat1)*cos(lat2)*cos(lon2-lon1)
        return acos(take_acos) * RADIUS
        


