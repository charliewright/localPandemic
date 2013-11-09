import math
class Edge(object):
  def __init__(self, n1, n2):
    self.n1 = n1
    self.n2 = n2
    self.distance = dist(n1,n2)
    self.same = (n1.category == n2.category)
    self.update_weight()

  def update_weight(self): #self.weight is [0,1]
    p_mov0 = 0.5
    dropoff = 0.04
    w = p_mov0-p_mov0/(1+math.exp(-dropoff*self.distance))
    if(self.same):
      self.weight =  w*1.2
    else:
      self.weight = w

class Venue(object):
  def __init__(self, json, category_name):
    self.json = json #store the whole object just in case
    self.name = json['name']
    self.category = category_name
    self.lat = float(json['location']['lat'])
    self.lng = float(json['location']['lng'])
    self.population = int(json['stats']['usersCount'])
    self.infected = 0
    self.new_population = self.population
    self.new_infected = self.infected
    self.edges = []

def distance_on_sphere(lat1, long1, lat2, long2):
    degrees_to_radians = math.pi/180.0
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + math.cos(phi1)*math.cos(phi2))
    if(cos > 1):
      cos = 1
    arc = math.acos( cos )
    return arc*6378100.0

def dist(n1, n2):
  return distance_on_sphere(n1.lat,n1.lng,n2.lat,n2.lng)
