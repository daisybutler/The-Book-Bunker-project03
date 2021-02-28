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
    // Transforms heart buttons from outline to solid when clicked
    $('.heart-button').click(function(){
        $('.heart').toggleClass('fas fa-heart');
        $('.heart').toggleClass('far fa-heart');
    })
  });
