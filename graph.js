function Edge(n1,n2) {
    this.n1 = n1
    this.n2 = n2
    this.distance = dist(n1,n2)
    this.same = (n1.category == n2.category)
    this.update_weight()

  function update_weight() {
    p_mov0 = 0.5
    dropoff = 0.04
    w = p_mov0-p_mov0/(1+math.exp(-dropoff*this.distance))
    if (self.same) {
      this.weight =  w*1.2
    }
    else {
      this.weight = w
    }
  }
}

function Venue(json, category_name) {
    this.json = json //store the whole object just in case
    this.name = json['name']
    this.category = category_name
    this.lat = int(json['location']['lat'])
    this.lng = int(json['location']['lng'])
    this.pop = int(json['stats']['usersCount'])
    this.infected = 0
    this.edges = []
}
function distance_on_sphere(lat1, long1, lat2, long2) {
    degrees_to_radians = math.pi/180.0
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
    return arc*6378100.0
}
function dist(n1, n2) {
  distance_on_sphere(n1.lat,n1.lng,n2.lat,n2.lng)
}
