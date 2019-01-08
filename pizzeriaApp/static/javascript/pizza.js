$(document).ready(function(){
  $("#par" ).click(function( ) {
    alert( "hola"); // true
  })
})
function agregarIngrediente() {
  $("ingredients").append("<select name='ingredients' required id='id_ingredients' multiple><option value='1'>Jamón</option><option value='2'>Champiñones</option><option value='3'>Pimentón</option><option value='4'>Doble Queso</option><option value='5'>Aceitunas</option><option value='6'>Pepperoni</option><option value='7'>Salchichón</option></select>");
}
