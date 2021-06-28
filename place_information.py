#Luke Fetchko
#PlaceInformation class describes a place containing a name, address, tag, and a GeoLocation object which stores the latitude and longitude of this place
from geolocation import GeoLocation

class PlaceInformation:
    # constructs a PlaceInfromation object which contains a name, address, and tag attributes. A Geolocation object is an attribute of the PlaceInformation object.
    def __init__(self,name,address,tag,latitude,longitude):
        self.__name = name
        self.__address = address
        self.__tag = tag
        self.__geo = GeoLocation(latitude,longitude)
    # returns the instance's name
    def get_name(self):
        return self.__name
    #returns the instance's address
    def get_address(self):
        return self.__address
    #returns the instace's tag
    def get_tag(self):
        return self.__tag
    # returns the string of a PlaceInformation object which lists the name and the latitude and longtidue of it's GeoLocation object
    def __str__(self):
        return self.__name + ': ' + str(self.__geo)
    #returns the GeoLocation object of this instace
    def get_location(self):
        return self.__geo
    #calls distance_from method on this instance and passes another GeoLocation object to it, returns result of distance_from method
    def distance_from(self, spot):
        return self.__geo.distance_from(spot)
    

    
