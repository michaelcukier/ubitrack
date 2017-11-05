if($( window ).width()<1110){


$(".link").click(function(){
    $(".link").toggle();
});

}else{
  $("#burger").hide();
}

$( window ).resize(function() {
  if($( window ).width()<1110){
    $("#burger").show();
    $(".link").hide();
  }else{
    $(".link").show();
    $("#burger").hide();
  }
});

$("#burger").click(function(){
    $(".link").toggle();
});
