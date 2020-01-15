# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    lat = 1
    lon = 2



# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class Waypoint(LatLon):
    name = "bob"

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
    difficulty = 'hard'
    size = 'large'

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

class Waypoint2:
    name = 'Catacombs'
    lat = 41.70505
    lon = -121.51521

w2 = Waypoint2()
print(w2.name, w2.lat, w2.lon)


# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
class Geocache2:
    name = "Newberry Views"
    diff = 1.5
    size = 2
    lat = -121.41556
    lon = 44.052137

g2 = Geocache2()
print(g2.name, g2.diff, g2.size, g2.lat, g2.lon)