function Edge(n1,n2) {
  this.n1 = n1;
  this.n2 = n2;
  this.distance = dist(n1,n2);
  this.same = (n1.category == n2.category);

  this.weight = function() {
    p_mov0 = 0.5;
    dropoff = 0.01;
    w = p_mov0-p_mov0/(1+Math.exp(-dropoff*this.distance));
    if (self.same) {
      return w*1.2;
    }
    else {
      return w;
    }
  }
}

function Venue(json, id) {
  this.id = id
  this.name = json['name'];
  this.category = json['category'];
  this.lat = json['lat'];
  this.lng = json['lng'];
  this.population = json['population'];
  this.infected = 0;
  this.edges = [];
  this.contentString = function() {
    return (this.name + "\n Hipsters: " + this.infected)
  }
}

function distance_on_sphere(lat1, lon1, lat2, lon2) {
  var radlat1 = Math.PI * lat1/180
    var radlat2 = Math.PI * lat2/180
    var radlon1 = Math.PI * lon1/180
    var radlon2 = Math.PI * lon2/180
    var theta = lon1-lon2
    var radtheta = Math.PI * theta/180
    var dist = Math.sin(radlat1) * Math.sin(radlat2) + Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
    dist = Math.acos(dist)
    dist = dist * 180/Math.PI
    dist = dist * 60 * 1.1515
    dist = dist * 1609.344 //Get km
    return dist
}
function dist(n1, n2) {
  return distance_on_sphere(n1.lat,n1.lng,n2.lat,n2.lng)
}
