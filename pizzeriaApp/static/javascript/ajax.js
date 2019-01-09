$(document).ready(function(){
  $("#target" ).submit(function(e) {
    e.preventDefault();

    $.ajax({
      url: $(this).attr('action'),
      type: $(this).attr('method'),
      data: $(this).serialize(),
      success: function(json){
        $("#data").html("<tr><th><b> Venta</b></th><th><b> Fecha</b></th><th><b> Total</b></th></tr>");
        $.each(json, function(i, item) {
          console.log(item);
          $("#data").append("<tr><td>"+ item.id + "</td><td>" + item.buy_date + "</td><td>" + item.total + "</td></tr>");
        });
        // for (const i=0; i< json.length ;i++){
        //   console.log(json[i]);
        //   // $("#data").append("<tr><td>"+ json[i].id + "</td><td>" + json[i].buy_date + "</td><td>" + json[i].total + "</td></tr>")
        // }
      }
    });
  });
});

// $("#target" ).submit(function(event) {
//   event.preventDefault();
// });
//
// function search (event){
//   event.preventDefault();
// }
