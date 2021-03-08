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
    // Transforms heart buttons from outline to solid when clicked to represent a like/unlike
    //$('.heart-button').click(function () {
       // if ($('.heart').toggleClass('far fa-heart') == True) {
            //$.post("/like_book", book_id=selected_book._id).done(function (reply) {
              //  $('.heart').toggleClass('fas fa-heart');
               // alert('Liked');
           // })
        //} else {
           // alert("Already liked")            
       // }
    //})
});
