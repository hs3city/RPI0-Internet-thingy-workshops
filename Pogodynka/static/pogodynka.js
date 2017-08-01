$(document).ready(function(){
  setInterval(function(){
    $.ajax({
        url: "/measurement.json",
        type: "GET",
        async: false,
        success: function(data) {
          state = JSON.parse(data)
          $('#temperature').innerHTML(state.temperature)
          $('#humidity').innerHTML(state.humidity)
      }})
  }, 1000

})
