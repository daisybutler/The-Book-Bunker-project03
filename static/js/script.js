$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.fixed-action-btn').floatingActionButton();
    $('.tooltipped').tooltip();

    /* Shows and hides the 'Show All Books' button on 'All Books' 
    page depending on if the user has filtered results with search bar */
    $('#show-all-books-btn').click(function(){
        $('#show-all-books-btn').addClass('hide-button');
    })
    
    /*
    $('.bookmark').click(function(){
        $(this).children('i').toggleClass('far')
        $(this).children('i').toggleClass('fas')
    }) */
});



// ------------------------ Uses an edited version of the code found at: https://codepen.io/deveb22/pen/QxPmGz

// Hides or displays the #back-to-top-button depending on the user's scroll position (on All Books page only).

var btn = $('#back-to-top-button');

$(window).scroll(function () {
	if ($(window).scrollTop() > 300) {
		btn.addClass('show');
	} else {
		btn.removeClass('show');
	}
});

btn.on('click', function (e) {
	e.preventDefault();
	$('html, body').animate({
		scrollTop: 0
	}, '300');
});


// Floating action button for user settings
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems, {
        direction: 'down',
        hoverEnabled: false
    });
});