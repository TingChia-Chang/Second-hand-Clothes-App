$(document).ready(function(){
    checkQueryString();
    // checkForm();
    navBar();
    addToCart();
    // showComment();
    addComment();
    deleteComment();
})

function checkQueryString(){
    var query = window.location.search;
    var urlParams = new URLSearchParams(query);
    if(urlParams.has('search-clothes')){
        var keyword = urlParams.get("search-clothes");
        console.log(keyword)
        if(keyword == 'hoodie'){
            $('.no-result').hide();
        }
        else{
            $('#content').hide();
        }
    }
    //implement search fuction
}

function checkForm() {
    $('#submit').click(function(e){
        e.preventDefault();
        var input_name = $('#name').val();
        var input_size = $('#size').val();
        var input_price = $('#price').val();
        var input_des = $('#description').val();
        var nameMsg = $('<p id="name-msg">Please enter the name!</p>')
        var groupMsg = $('<p id="group-msg">Please choose the group!</p>')
        var kindMsg = $('<p id="kind-msg">Please choose the kind!</p>')
        var sizeMsg = $('<p id="size-msg">Please enter the size!</p>')
        var priceMsg = $('<p id="price-msg">Please enter the price!</p>')
        var desMsg = $('<p id="des-msg">Please enter the description!</p>')
        //define err messages
        if(input_name == ""){
            $('#form-name').append(nameMsg).css({position:'relative'});
            $('#form-name').children().last().css({
                top : "8px",
                right : 0,
                position : "absolute",
                color : "red",
                fontSize : "0.7em",
            })

            $('#name').css({
                borderColor : "red"
            })

            $('#name').change(function() {
                $(this).css({
                    borderColor : "revert"
                })
            })

            setTimeout(() => {
                $(nameMsg).fadeOut('slow', function(){
                    $(this).remove()
                })
            }, 2000);
        }
        //show the error message and change the border colot of the input

        if(input_size == ""){
            $('#form-size').append(sizeMsg).css({position:'relative'});
            $('#form-size').children().last().css({
                top : "8px",
                right : 0,
                position : "absolute",
                color : "red",
                fontSize : "0.7em",
            })

            $('#size').css({
                borderColor : "red"
            })

            $('#size').change(function() {
                $(this).css({
                    borderColor : "revert"
                })
            })

            setTimeout(() => {
                $(sizeMsg).fadeOut('slow', function(){
                    $(this).remove()
                })
            }, 2000);
        }
        //show the error message and change the border colot of the input

        if(input_price == ""){
            $('#form-price').append(priceMsg).css({position:'relative'});
            $('#form-price').children().last().css({
                top : "8px",
                right : 0,
                position : "absolute",
                color : "red",
                fontSize : "0.7em",
            })

            $('#price').css({
                borderColor : "red"
            })

            $('#price').change(function() {
                $(this).css({
                    borderColor : "revert"
                })
            })

            setTimeout(() => {
                $(priceMsg).fadeOut('slow', function(){
                    $(this).remove()
                })
            }, 2000);
        }
        //show the error message and change the border colot of the input

        if(input_des == ""){
            $('#form-des').append(desMsg).css({position:'relative'});
            $('#form-des').children().last().css({
                top : "8px",
                right : 0,
                position : "absolute",
                color : "red",
                fontSize : "0.7em",
            })

            $('#description').css({
                borderColor : "red"
            })

            $('#description').change(function() {
                $(this).css({
                    borderColor : "revert"
                })
            })

            setTimeout(() => {
                $(desMsg).fadeOut('slow', function(){
                    $(this).remove()
                })
            }, 2000);
        }
        //show the error message and change the border colot of the input

        if(!$('#women').is(":checked") && !$('#men').is(":checked")){
            $('#check-women').append(groupMsg).css({position:'relative'});
            $('#check-women').children().last().css({
                top : "8px",
                right : 0,
                position : "absolute",
                color : "red",
                fontSize : "0.7em",
            })

            setTimeout(() => {
                $(groupMsg).fadeOut('slow', function(){
                    $(this).remove()
                })
            }, 2000);
        }
        //show the error message and change the border colot of the input

        if(!$('#top').is(":checked") && !$('#bottom').is(":checked")){
            $('#check-top').append(kindMsg).css({position:'relative'});
            $('#check-top').children().last().css({
                top : "8px",
                right : 0,
                position : "absolute",
                color : "red",
                fontSize : "0.7em",
            })

            setTimeout(() => {
                $(kindMsg).fadeOut('slow', function(){
                    $(this).remove()
                })
            }, 2000);
        }
        //show the error message and change the border colot of the input

        
    })
}

function navBar(){
    $('#primary-nav').on("mouseover", "li", function(event) {
        $(this).css({backgroundColor:'grey'})
    })
    //turn the backgound color of li to grey when mouseover
    $('#primary-nav').on("mouseout", "li", function(event) {
        $(this).css({backgroundColor:'revert'})
    })
    //turn the backgound color of li  back to original one when mouseout
}

function addToCart(){
    $('#add_cart').click(function(e){
        e.preventDefault();
        var cartMsg = $('<p id="cart-msg">The item has been added to cart!</p>')
        $(cartMsg).appendTo($(this).parent()).fadeIn(2000).fadeOut(1000, function(){
            $(this).remove()
        })
    })
    //show a confirm message when the button is clicked
}

// function showComment(){
//     $('#show_comment').click(function(e){
//         var clothes_id = $(this).attr('data-clothes-id');
//         var clothes_url = $(this).attr('data-ajax-url');
//         $.ajax({
 
//             // The URL for the request
//             url: clothes_url,
         
//             // The data to send (will be converted to a query string)
//             data: {
//                 clothes_id: clothes_id,
//             },
         
//             // Whether this is a POST or GET request
//             type: "POST",
         
//             // The type of data we expect back
//             dataType : "json",
//             headers : {'X-CSRFToken': csrftoken},
//             context: this
//         })
//           // Code to run if the request succeeds (is done);
//           // The response is passed to the function
//           .done(function( json ) {
//             // alert("request received successfully");
//             // console.log(json.comment)
//             // $( ".show" ).hide();

//             comments = JSON.parse(json.comment)
//             console.log(comments[0].fields)
//             for(comment in comments){
//                 console.log( comments[comment].fields.comment );
//                 console.log( comments[comment].fields.username );
//                 $("#comment-content").prepend('<div class="show-comment"><p><a href="'+json.url+'">'+comments[comment].fields.username+'</a> : '+comments[comment].fields.comment+'</p><p>'+comments[comment].fields.created_time+'</p></div>')
//                 // $( "<p>" ).text( comments[comment].fields.comment ).appendTo("#comment-content");
                
//             }
//             // json.comment[comment]
//             $(this).hide()

//           })
//           // Code to run if the request fails; the raw request and
//           // status codes are passed to the function
//           .fail(function( xhr, status, errorThrown ) {
//             // alert( "Sorry, there was a problem!" );
//             console.log( "Error: " + errorThrown );
//             // console.log( "Status: " + status );
//             // console.dir( xhr );
//           })
//           // Code to run regardless of success or failure;
//           .always(function( xhr, status ) {
//             // alert( "The request is complete!" );
//           });
//     })
    
// }

function deleteComment(){
    $('div').on('click', '#comment-delete', function(e){
        console.log('click')
        var comment_id = $(this).attr('comment-id');
        var comment_url = $("#comment-content").attr('data-ajax-url');
        // var clothes_comment = $('#comment-input').val();
        $.ajax({
 
            // The URL for the request
            url: comment_url,
         
            // The data to send (will be converted to a query string)
            data: {
                comment_id: comment_id,
                // clothes_comment : clothes_comment
            },
         
            // Whether this is a POST or GET request
            type: "POST",
         
            // The type of data we expect back
            dataType : "json",
            headers : {'X-CSRFToken': csrftoken},
            context: this
        })
          // Code to run if the request succeeds (is done);
          // The response is passed to the function
          .done(function( json ) {
            $(this).parent().remove()
          })
          // Code to run if the request fails; the raw request and
          // status codes are passed to the function
          .fail(function( xhr, status, errorThrown ) {
            // alert( "Sorry, there was a problem!" );
            console.log( "Error: " + errorThrown );
            // console.log( "Status: " + status );
            // console.dir( xhr );
          })
          // Code to run regardless of success or failure;
          .always(function( xhr, status ) {
            // alert( "The request is complete!" );
          });
    })
    
}

function addComment(){
    $('#comment-button').click(function(e){
        console.log('click')
        var clothes_id = $(this).attr('data-clothes-id');
        var clothes_url = $(this).attr('data-ajax-url');
        var clothes_comment = $('#comment-input').val();
        $.ajax({
 
            // The URL for the request
            url: clothes_url,
         
            // The data to send (will be converted to a query string)
            data: {
                clothes_id: clothes_id,
                clothes_comment : clothes_comment
            },
         
            // Whether this is a POST or GET request
            type: "POST",
         
            // The type of data we expect back
            dataType : "json",
            headers : {'X-CSRFToken': csrftoken},
            context: this
        })
          // Code to run if the request succeeds (is done);
          // The response is passed to the function
          .done(function( json ) {
            // alert("request received successfully");
            // console.log(json.comment)
            if(!json.error){
                $("#comment-content").prepend('<div class="show-comments"><p><a href="'+json.url+'">'+json.username+'</a> : '+json.comment+'</p><p>'+json.time+'</p><button id="comment-delete" comment-id="'+json.id+'">Delete</button></div>')
                $(".no-comment").remove()
            }
          })
          // Code to run if the request fails; the raw request and
          // status codes are passed to the function
          .fail(function( xhr, status, errorThrown ) {
            // alert( "Sorry, there was a problem!" );
            console.log( "Error: " + errorThrown );
            // console.log( "Status: " + status );
            // console.dir( xhr );
          })
          // Code to run regardless of success or failure;
          .always(function( xhr, status ) {
            // alert( "The request is complete!" );
          });
    })
    
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');