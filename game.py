import pickle
from venueGraph import *
json_venues = pickle.load(open('venues.txt', 'r'))
edge_dist = 18
graph = []
def connect():
  for cat in json_venues:
    for item in json_venues[cat]:
      graph.append(Venue(item,cat))
  for venue1 in graph:
    for venue2 in graph:
      if venue1 != venue2:
        if dist(venue1,venue2) < edge_dist:
          venue1.edges.append(Edge(venue1,venue2))

connect()

