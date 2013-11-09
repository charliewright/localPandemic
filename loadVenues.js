function loadVenues() {
   var data_file = "/data.json";
   var http_request = new XMLHttpRequest();
   http_request = new XMLHttpRequest();
   http_request.onreadystatechange  = function(){
      if (http_request.readyState == 4  )
      {
        var jsonObj = JSON.parse(http_request.responseText);

        // be accessed as jsonObj.name and jsonObj.country.
      }
   }
   http_request.open("GET", data_file, true);
   http_request.send();
}
