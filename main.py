import math
import foursquare
city = "NYC"
radius = 1000
client = foursquare.Foursquare(client_id='34030ZPC2URSHBRGD44MKQMVZBTIKJIG5TA20W1APVSOYARP', client_secret='5M5UT4HQNU2SBE2FWKQQFQY5YQYV5UMCS0DWFMXHNQX4WGW2')
categories = {
  "entertainment" : "4d4b7104d754a06370d81259",
  "food" : "4d4b7105d754a06374d81259",
  "night": "4d4b7105d754a06376d81259",
  "out" : "4d4b7105d754a06377d81259",
  "shopping" : "4d4b7105d754a06378d81259",
  "travel" : "4d4b7105d754a06379d81259"
}
venues = {}
for cat in categories:
  p = {'near': city,
      'limit': '50',
      'category': cat,
      'intent': 'browse',
      'radius': radius
      }
  venues[cat] = client.venues.search(params=p)['venues']
  print venues[cat]
for cat in categories:
  print len(venues[cat])
class Edge:
  def __init__(self, n1,n2):
    self.n1 = n1
    self.n2 = n2
    self.distance = dist(n1,n2)

  def dist(self, n1, n2):
    math.sqrtn((n2.lat-n1.lat)**2+(n2.lng-n1.lng)**2)

class Venue:
  def __init__(self, json):
    self.json = json #store the whole object just in case
    self.name = json['name']
    self.lat = int(json['location']['lat'])
    self.lng = int(json['location']['lng'])
    #self.sub
    self.edges = []
