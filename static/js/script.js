$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.fixed-action-btn').floatingActionButton();
    $('.tooltipped').tooltip();
    $('.modal').modal();
    $('#show-all-books-btn').click(function(){
        $('#show-all-books-btn').addClass('hide-button');
    })
  });



/*
function showAllBooksBtn() {
    btn = document.getElementById('#show-all-books-btn');
    btn.classList.remove('hide-button');
}

function hideAllBooksButton() {
    btn = document.getElementById('#show-all-books-btn');
    btn.classList.add('hide-button');
}*/

