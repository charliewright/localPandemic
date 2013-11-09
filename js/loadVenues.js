function loadVenues() {
  var data_file = "/nycdata.json";
  var http_request = new XMLHttpRequest();
  http_request = new XMLHttpRequest();
  http_request.onreadystatechange  = function(){
    if (http_request.readyState == 4  )
    {
      jsons = JSON.parse(http_request.responseText);
      venues = [];
      for(obj in jsons) {
        venues.push(new Venue(jsons[obj]));
      }
      $.each(venues, function(i, venue) {
        console.log(venue.lat, venue.lng);
        $('#map_canvas').gmap('addMarker', { 
          'position': new google.maps.LatLng(venue.lat, venue.lng), 
          'bounds': true 
        }).click(function() {
          $('#map_canvas').gmap('openInfoWindow', { 'content': venue.name }, this);
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
