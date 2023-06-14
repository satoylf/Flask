var temp = document.getElementById("temp");
var humi = document.getElementById("humi");
var pres = document.getElementById("pres");
setInterval(function(){
  $.ajax({
    url: "/status",
    type: "get",
    success: function(data) {
      temp.textContent = data['t'] + " C";
      humi.textContent = data['h'] + " %";
      pres.textContent = data['p'] + " hPa";
    },
    error: function(xhr) {
      // Handle error
    }
  });
}, 1000);
setInterval(function(){
  $.ajax({
    url: "/warn",
    type: "get",
    success: function(data) {
      if (data !== "") {
        var string = "";
        if (data.includes("T")) {
          string += "Temperatura fora da ideal\n";
        }
        if (data.includes("H")) {
          string += "Humidade fora da ideal\n";
        }
        if (data.includes("P")) {
          string += "Pressão fora da ideal\n";
        }
        alert(string);
      }
    },
    error: function(xhr) {
      // Handle error
    }
  });
}, 1000);
