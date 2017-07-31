function zwieksz_licznik(){
  $.ajax({
    url: "/licznik",
    type: "POST",
    data: JSON.stringify({"browser": navigator.userAgent, "add": 5),
    async: false,
    success: function(data) {
      alert(data)
  }})
}

