$(document).ready(function(){
    $('.payWithRazorpay').click(function(e){
        e.preventDefault();

        var first_name = $("[name='first_name']").val();
        var last_name = $("[name='last_name']").val();
        var email = $("[name='email']").val();
        var phone = $("[name='phone']").val();
        var address = $("[name='address']").val();
        var city = $("[name='city']").val();
        var state = $("[name='state']").val();
        var pin_code = $("[name='pin_code']").val();
        var country= $("[name='country']").val();
        var payment_mode = $("[name='payment_mode']").val();
      
        if(first_name =="" || last_name =="" || email =="" || phone =="" || address =="" || city =="" || state =="" || pin_code =="" || country =="" || payment_mode ==""){
            alert("All fields are required");
            return false;
        }
       else{
        $.ajax({
            method:"GET",
            url:"/proceed-to-pay",
            success:function(response){
               
                var options ={
                    "key":"YOUR_KEY_ID",
                    "amount":"50000",
                    "currency":"INR",
                    "name":"Acme Corp",
                    "description":"Test Transaction",
                    "image":"https://example.com/your_logo",
                    "order_id":"order_9A33XWu170gUtm",
                    "handler":function(response){
                        alert(response.razorpay_payment_id);
                        alert(response.razorpay_order_id);
                        alert(response.razorpay_signature);
                    },
                    "prefill":{
                        "name":"Nuel Edward",
                        "email":"nuel4xelence@gmail.com",
                        "contact":"9999999999"
                    },
                    "notes":{
                        "address":"Razorpay Corporate Office"
                    },
                    "theme":{
                        "color":"#3399cc"
                    }
                };
                var rzp1 =new Razorpay(options);
                rzp1.open()

            }

        });
       
       }
    });
});






const form  = document.getElementById("payForm");
form.addEventListener("submit", payNow);


function payNow(e){
    //prevent normal form submission
    e.preventDefault();
    
    // set configurations
    FlutterwaveCheckout({
       public_key:"FLWPUBK_TEST-7a604ecf4cca1e2f78deb205a2750ac8-X",
       tx_ref: "nuel_" +Math.floor((Math.random()*1000000000)+1),
       amount: document.getElementById("amount").value,
       currency:"NGN",
       redirect_url:"http://127.0.0.1:8000/payment_confirmed",
     
       //payment_options:true,
       //  country: "US",
       //meta: {
        //consumer_id:document.getElementById("id").value,
        //consumer_mac: "92a3-912ba-1192a",
      //},
       customer:{
           email: document.getElementById("email").value,
           phone_number:document.getElementById("phoneNumber").value,
           name:document.getElementById("fullname").value,
       },
       callback:function(data){
           const reference = data.tx_ref;
           alert("Payment was successfully completed!" + reference);
           //console.log(data);
       },
       customizations: {
        title: "Nuel Ecommerce",
        description: "Payment for the services requested"
        //logo: "https://assets.piedpiper.com/logo.png",
      },
       //customizations:true
    });
}