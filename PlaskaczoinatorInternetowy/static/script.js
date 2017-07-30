function make_slap(){
  $.ajax({
    url: "/plask",
    type: "GET",
    async: false,
    success: function(data) {
      if(data=='OK'){
        alert("Sprzedałeś plaskacza!")
      } else {
        alert("Ktoś inny sprzedał plaskacza!")
      }
  }})
}
