function loadVenues() {
  var data_file = "/data/New Haven";
  var http_request = new XMLHttpRequest();
  http_request = new XMLHttpRequest();
  http_request.onreadystatechange  = function(){
    if (http_request.readyState == 4)
    {
      jsons = JSON.parse(http_request.responseText);
      venues = [];
      for(obj in jsons) {
        venues.push(new Venue(jsons[obj], obj));
      }
      $.each(venues, function(i, venue) {
        $('#map_canvas').gmap('addMarker', { 
          'position': new google.maps.LatLng(venue.lat, venue.lng), 
          'bounds': true,
          'icon': 'images/blue_icon.png',
          'venue_id' : venue.id
        }).mouseover(function() {
          $('#map_canvas').gmap('openInfoWindow', { 'content': venue.contentString() }, this);
        });
      });
      simulate(venues);
    }
  }
  http_request.open("GET", data_file, true);
  http_request.send();
}
$(document).ready(function() {
  loadVenues();
});
