$(document).ready(function(){
    checkQueryString();
    checkForm();
    navBar();
    addToCart();
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