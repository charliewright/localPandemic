import foursquare
import json

radius = 1000
client = foursquare.Foursquare(client_id='34030ZPC2URSHBRGD44MKQMVZBTIKJIG5TA20W1APVSOYARP', client_secret='5M5UT4HQNU2SBE2FWKQQFQY5YQYV5UMCS0DWFMXHNQX4WGW2')
def get_venues(city):
  def to_json(json):
    return {
        'name' : json['name'],
        'category' : '4d4b7105d754a06374d81259',
        'lat' : float(json['location']['lat']),
        'lng' : float(json['location']['lng']),
        'population' : int(json['stats']['usersCount']),
        'infected' : 0,
        'new_population' : int(json['stats']['usersCount']),
        'new_infected' : 0
        }
  p = {
      'near': city,
      'limit': '50',
      'category': '4d4b7105d754a06374d81259',
      'intent': 'browse',
      'radius': radius
      }
  cat_venues = []
  for venue in client.venues.search(params=p)['venues']:
    cat_venues.append(to_json(venue))
  return json.dumps(cat_venues)
