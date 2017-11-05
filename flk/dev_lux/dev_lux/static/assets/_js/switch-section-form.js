

$('#annonces').click(function() {
   if($('#annonces').is(':checked')) {
     $("#input-article").css("display","block");
     $("#ap-annonces").css("display","block");

     $("#input-members").css("display","none");
     $("#ap-membres").css("display","none");
     $("#input-event").css("display","none");
     $("#ap-event").css("display","none");
   }
});
$('#membres').click(function() {
   if($('#membres').is(':checked')) {
     $("#input-members").css("display","block");
     $("#ap-membres").css("display","block");

     $("#input-article").css("display","none");
     $("#ap-annonces").css("display","none");
     $("#input-event").css("display","none");
     $("#ap-event").css("display","none");
   }
});
$('#event').click(function() {
   if($('#event').is(':checked')) {
     //show
     $("#input-event").css("display","block");
     $("#ap-event").css("display","block");
     //hide
     $("#input-article").css("display","none");
     $("#ap-annonces").css("display","none");
     $("#input-members").css("display","none");
     $("#ap-members").css("display","none");
   }
});
//ap events
$('#in-date').bind('keyup', function(){
    var text = $(this).val();
    $('#ap-date').empty();
    $('#ap-date').append(text);
});
$('#in-description').bind('keyup', function(){
    var text = $(this).val();
    $('#ap-desc').empty();
    $('#ap-desc').append(text);
});
//ap members
$('#in-name').bind('keyup', function(){
    var text = $(this).val();
    $('#name-members').empty();
    $('#name-members').append(text);
});
$('#in-sec-name').bind('keyup', function(){
    var text = $(this).val();
    $('#name-sec-members').empty();
    $('#name-sec-members').append(text);
});
$('#in-status').bind('keyup', function(){
    var text = $(this).val();
    $('#status-members').empty();
    $('#status-members').append(text);
});
$('#in-stars').bind('keyup', function(){
    var text = $(this).val();
    $('#stars-members').empty();
    $('#stars-members').append(text);
});
$('#in-adress').bind('keyup', function(){
    var text = $(this).val();
    $('#adress-members').empty();
    $('#adress-members').append(text);
});
//END


$('#titleApercu').bind('keyup', function(){
    var text = $(this).val();
    $('#previewtitle').empty();
    $('#previewtitle').append(text);
});
// TEXT AREA
  $('#textApercu').bind('keyup', function(){
      var text = $(this).val();
      $('#preview').empty();
      $('#preview').append(text);
  });

  $( "#stat" ).click(function() {
    $("#statis").css("left","0");
    $("#publ1").css("left","100%");
    $("#trad").css("left","100%");
    $("#ban-pub").css("left","100%");

  });
  $( "#publications" ).click(function() {
    $("#statis").css("left","100%");
    $("#publ1").css("left","0");
    $("#trad").css("left","100%");
    $("#ban-pub").css("left","100%");
  });
  $( "#publicites" ).click(function() {
    $("#statis").css("left","100%");
    $("#publ1").css("left","100%");
    $("#trad").css("left","100%");
    $("#ban-pub").css("left","0");

  });
  $( "#langues" ).click(function() {
    $("#trad").css("left","0");
    $("#statis").css("left","100%");
    $("#publ1").css("left","100%");
    $("#ban-pub").css("left","100%");
  });

//////////////////////////////////////////////

  $( "#homepage" ).click(function() {
      $(".all-text-page").css("display","none");
      $(".page_homepage").css("display","block");
  });
  $( "#membres-page" ).click(function() {
    $(".all-text-page").css("display","none");
      $(".page_membres").css("display","block");
  });
  $( "#business-page" ).click(function() {
    $(".all-text-page").css("display","none");
      $(".page_business").css("display","block");
  });
  $( "#shop-pages" ).click(function() {
    $(".all-text-page").css("display","none");
      $(".page_shop").css("display","block");
  });
  $( "#decou-pages" ).click(function() {
    $(".all-text-page").css("display","none");
      $(".page_decou").css("display","block");
  });
  $( "#contact-pages" ).click(function() {
    $(".all-text-page").css("display","none");
      $(".page_contact").css("display","block");
  });

  $( ".box-alert" ).click(function() {
    $(".box-alert").css("display","none");
  });
