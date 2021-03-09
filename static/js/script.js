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
