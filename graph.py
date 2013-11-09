import math
class Edge:
  def __init__(self, n1,n2):
    self.n1 = n1
    self.n2 = n2
    self.distance = dist(n1,n2)
    self.same = (n1.category == n2.category)

  def dist(self, n1, n2):
    math.sqrtn((n2.lat-n1.lat)**2+(n2.lng-n1.lng)**2)

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
