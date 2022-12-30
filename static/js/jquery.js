/*var price = parseFloat($('#sales').text().replace("$","")); 
//var total = parseFloat($('.total').text().replace("$",""));
/*$total = $('.total');
$('.decrement-btn').on("click", function(){
  $qty = $('.qty-input');
  var current_qty = parseInt($qty.val());
  if(current_qty > 0){
      $qty.val(current_qty-1)

      $total.val(price *(current_qty -1))
  }
})


$('.increment-btn').on("click", function(){
  $qty = $('.qty-input');
  var current_qty = parseInt($qty.val());
  if(current_qty >= 0){
      $qty.val(current_qty+1);

      $total.val(price*(current_qty+1));
      
  }
})*/

$(document).ready(function(){

  var price = parseFloat($('#sales').text().replace("$","")); 
  //var total = parseFloat($('.total').text().replace("$",""));
  $total = $('.total');
  $('.increment-btn').click(function(e){
    e.preventDefault();
   

    //var current_qty = parseInt($.val());
    //$total = $('.total');

    var increase_value =$(this).closest('.product_data').find('.qty-input').val();
    var value = parseInt(increase_value);

    value =isNaN(value) ? 1 :value;

    if (value >0 ){
      value++;
      $(this).closest('.product_data').find('.qty-input').val(value);
      $total.val(price *(value))
    
    }

  })


  $('.decrement-btn').click(function(e){
     e.preventDefault();

     var price = parseFloat($('#sales').text().replace("$",""));
     //var total = parseFloat($('.total').text().replace("$",""));
     $total = $('.total');

     var decrease_value =$(this).closest('.product_data').find('.qty-input').val();

     var value = parseInt(decrease_value);

     value = isNaN(value) ? 1: value;
     if(value >1){
      value --;

      $total.val(price *(value))
      
      $(this).closest('.product_data').find('.qty-input').val(value);

     }
  });

});


$('.addToCart').click(function(e){
  e.preventDefault();

  var product_id = $(this).closest('.product_data').find('.prod_id').val();
  var product_qty = $(this).closest('.product_data').find('.qty-input').val();
  var token =$('input[name=csrfmiddlewaretoken]').val();

  $.ajax({
    method: "POST",
    url: "/add_to_cart",
    data:{
      'product_id': product_id,
      'product_qty' :product_qty,
      csrfmiddlewaretoken: token
    },
    success: function(response){
      alertify.success(response.status)
      console.log(response);
      //alert(response)
    }
  });

});


$('.changeQuantity').click(function(e){
  e.preventDefault();

  var product_id = $(this).closest('.product_data').find('.prod_id').val();
  var product_qty = $(this).closest('.product_data').find('.qty-input').val();
  var token =$('input[name=csrfmiddlewaretoken]').val();

  $.ajax({
    method: "POST",
    url: "/update_cart",
    data:{
      'product_id': product_id,
      'product_qty' :product_qty,
      csrfmiddlewaretoken: token
    },
    success: function(response){
      alertify.success(response.status)
      console.log(response);
    
    }
  });
});



  $(document).on('click','.delete-cart-item', function(e){  
    e.preventDefault();

  var product_id = $(this).closest('.product_data').find('.prod_id').val();
  var token =$('input[name=csrfmiddlewaretoken]').val();

  $.ajax({
    method: "POST",
    url: "delete_cart_item",
    data:{
      'product_id': product_id,
     
      csrfmiddlewaretoken: token
    },
    success: function(response){
      alertify.success(response.status)
      $('.cartdata').load(location.href + ".cartitem")
    }
  });


  });



  $('.addToWishlist').click(function(e){
    e.preventDefault();

  var product_id = $(this).closest('.product_data').find('.prod_id').val();
  var token =$('input[name=csrfmiddlewaretoken]').val();

  $.ajax({
    method: "POST",
    url: "/addTowishList",
    data:{
      'product_id': product_id,
      csrfmiddlewaretoken: token
    },
    success: function(response){
      alertify.success(response.status)
      $('.show').load(location.href + ".show");
    }
     });
  });

  


 $(document).on('click','.delete-wishlist-item', function(e){
    e.preventDefault();

  var product_id = $(this).closest('.product_data').find('.prod_id').val();
  var token =$('input[name=csrfmiddlewaretoken]').val();

  $.ajax({
    method: "POST",
    url: "/delete_wishlist_item",
    data:{
      'product_id': product_id,
     
      csrfmiddlewaretoken: token
    },
    success: function(response){
      alertify.success(response.status)
      $('.wishdata').load(location.href + ".wishitem");
    }
  });


  });
