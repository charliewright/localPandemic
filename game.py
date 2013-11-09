import random
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
          venue1.edges.append(Edge(venue2,venue1))
connect()
def total_population():
  sum_pop = 0
  for v in graph:
    sum_pop += v.population
  return sum_pop

def total_infected():
  sum_infected = 0
  for v in graph:
    sum_infected += v.infected
  return sum_infected

def update():
  for v in graph:
    sum_incoming_virus = 0
    for edge in v.edges:
      incoming = edge.n1
      current_node = edge.n2
      sum_incoming_virus += int(edge.weight*incoming.infected)
    self_virus = int(v.infected * 0.01)
    v.new_infected = min(current_node.infected + sum_incoming_virus + self_virus, current_node.population)

  for v in graph:
    v.infected = v.new_infected
    v.population = v.new_population

start_node = graph[random.randrange(0,len(graph))]
start_node.infected = int(start_node.population*0.1)

total_pop = total_population()
total_inf= total_infected()
print total_inf, total_pop
while(total_inf < total_pop):
  update()
  total_inf= total_infected()
  print total_inf, total_pop
