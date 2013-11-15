import math
class Edge:
  def __init__(self, n1,n2):
    self.n1 = n1
    self.n2 = n2
    self.distance = dist(n1,n2)
    self.same = (n1.category == n2.category)
    self.weight = calc_weight(self.dist)

    def calc_weight(self,dist):
      w = p_mov0-p_mov0/(1+exp(-dropoff*dist))
      if(same):
        return w*1.2
      return w

class Venue:
  def __init__(self, json, category_name):
    self.json = json #store the whole object just in case
    self.name = json['name']
    self.category = category_name
    self.lat = int(json['location']['lat'])
    self.lng = int(json['location']['lng'])
    self.pop = int(json['stats']['usersCount'])
    self.infected = 0
    self.edges = []

def distance_on_sphere(lat1, long1, lat2, long2):
    degrees_to_radians = math.pi/180.0
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
    return arc*6378100.0

def dist(n1, n2):
  distance_on_sphere(n1.lat,n1.lng,n2.lat,n2.lng)
