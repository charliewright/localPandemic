import foursquare
city = "NYC"
radius = 1000
client = foursquare.Foursquare(client_id='34030ZPC2URSHBRGD44MKQMVZBTIKJIG5TA20W1APVSOYARP', client_secret='5M5UT4HQNU2SBE2FWKQQFQY5YQYV5UMCS0DWFMXHNQX4WGW2')
categories = {
  "entertainment" : "4d4b7104d754a06370d81259",
  "food" : "4d4b7105d754a06374d81259",
  "night": "4d4b7105d754a06376d81259",
  "outdoors" : "4d4b7105d754a06377d81259",
  "shopping" : "4d4b7105d754a06378d81259",
  "travel" : "4d4b7105d754a06379d81259"
}
venues = {}
for cat in categories:
  p = {
      'near': city,
      'limit': '50',
      'category': cat,
      'intent': 'browse',
      'radius': radius
      }
  venues[cat] = Venue(client.venues.search(params=p)['venues'], cat)
