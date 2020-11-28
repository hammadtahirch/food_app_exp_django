/**
 * Create a map with a marker.
 * Creating or dragging the marker sets the latitude and longitude values
 * in the input fields.
 */
;(function($) {

    function init (){
    debugger;
        var input = document.getElementById('id_address');
        // var options = {
        //   types: ['(regions)'],
        //   componentRestrictions: {country: "IN"}
        // };
        var options = {}

        var autocomplete = new google.maps.places.Autocomplete(input, options);

        google.maps.event.addListener(autocomplete, 'place_changed', function() {
        debugger;
          var place = autocomplete.getPlace();
          var lat = place.geometry.location.lat();
          var lng = place.geometry.location.lng();
          var placeId = place.place_id;
          // to set city name, using the locality param
          var componentForm = {
            locality: 'short_name',
            administrative_area_level_1:'long_name',
            country:'long_name',
            postal_code:'short_name',
          };
          for (var i = 0; i < place.address_components.length; i++) {

            var addressType = place.address_components[i].types[0];
            var val = place.address_components[i][componentForm[addressType]];
            if (addressType === "locality") {
              document.getElementById("id_city").value = val;
            }else if(addressType === "administrative_area_level_1"){
              document.getElementById("id_province").value = val;
            }else if(addressType === "country"){
              document.getElementById("id_country").value = val;
            }else if(addressType ==="postal_code"){
              document.getElementById("id_postal_code").value = val;
            }
          }
          document.getElementById("id_latitude").value = lat;
          document.getElementById("id_longitude").value = lng;
        });
    }

  $(document).ready(function(){
   init()
  });

})(django.jQuery);