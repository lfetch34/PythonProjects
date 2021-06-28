# This program can be used to search for places of interest near a given
# location.  Read the give_intro method for more details.  It depends on a file
# called places.txt for the data.

from place_information import *
from geolocator import *

def main():
    give_intro()
    lines = open("places.txt").readlines()
    data = parse_file(lines)

    target = input("target? ")
    target = GeoLocator.find_place(target)
    if (target == None):
        print("no matches for that search string.")
    else:
        print("found " + target.get_name())
        show_matches(data, target)

# introduces the program to the user
def give_intro():
    print("This program allows you to search for places of")
    print("interest near a target location.  For each")
    print("search, you will be asked for a target radius,")
    print("and a search string for name and tags.  If you")
    print("don't want to filter on name and/or tag, simply")
    print("hit enter to see all results.")
    print()

# Parses data from the given file to construct a list of
# PlaceInformation objects.  Assumes the data is in standard format
# (tab-delimited lines with name, address, tag, latitude, longitude).
def parse_file(lines):
    entries = []
    for line in lines:
        lst = list(line.split("\t"))
        place = PlaceInformation(lst[0], lst[1], lst[2], float(lst[3]), float(lst[4]))
        entries.append(place)
    # put the code here to go thru each line in lines and split using tab as the delimeter and create a PlaceInformation object for each line and store in the list entries
    return entries
# Prompts the user for a radius and search strings and shows matching
# entries from data and their distance from the given target.
def show_matches(data, target):
    radius = 42  # not a real radius, priming the while loop
    while (radius > 0):
        print()
        radius = float(input("radius (0 to quit)? "))
        if (radius > 0):
            show_entries(data, target, radius)

# Prompts the user for search strings and shows matching entries from data
# that are within the given distance of the given target.
def show_entries(data, target, radius):
    name_filter = input("name filter (enter for none)? ")
    tag_filter = input("tag filter (enter for none)? " )
    for entry in data:
        name_match = match(entry.get_name(), name_filter)
        tag_match = match(entry.get_tag(), tag_filter)
        if (name_match and tag_match):
            distance = entry.distance_from(target.get_location())
            print("distance: ", distance)
            if (distance <= radius):
                print(str(distance) + " miles: " + entry.get_name() + " " +
                      entry.get_address())

# returns true if the bigger string contains the smaller string ignoring
# case
def match(big, small):
    return small.lower() in big.lower()


main()
