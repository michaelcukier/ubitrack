

$(window).scroll(function() {
    var windscroll = $(window).scrollTop();
    if (windscroll >= 100) {
        $('section').each(function(i) {
            if ($(this).position().top <= windscroll + 450) {
                $('nav a.active-menu-top').removeClass('active-menu-top');
                $('nav a').eq(i).addClass('active-menu-top');
            }
        });

    } else {
        $('nav a.active-menu-top').removeClass('active-menu-top');
        $('nav a:first').addClass('active-menu-top');
    }

})


// to top right away
if ( window.location.hash ) scroll(0,0);
// void some browsers issue
setTimeout( function() { scroll(0,0); }, 1);

$(function() {

    // your current click function
    $('a[href^="#"]').on('click', function(e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $($(this).attr('href')).offset().top-50 + 'px'
        }, 1000, 'swing');
    });

    // *only* if we have anchor on the url
    if(window.location.hash) {

        // smooth scroll to the anchor id
        $('html, body').animate({
            scrollTop: $(window.location.hash).offset().top-50 + 'px'
        }, 1000, 'swing');
    }

});
