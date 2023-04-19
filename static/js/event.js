

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
       currency:"USD",
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
        title: "nuel",
        description: "Payment for the services requested"
        //logo: "https://assets.piedpiper.com/logo.png",
      },
       //customizations:true
    });
}


