 $("i").click(function(){
     $(this).toggleClass("fa-thumbs-down");
 });

 var addtoCartButtons=document.getElementsByClassName("cart");

 for(var i=0; i<addtoCartButtons.length; i++){
    addtoCartButtons[i].addEventListener('click',function(){
        var productID=this.dataset.product;
        
        UpdateUserOrder(productID);
    })
 }

 function UpdateUserOrder(productID){
    alert(productID);

    var url='/updateItem/';

    fetch(url,{
        method:'POST',
        headers:{
            'content-type':'application/json',
            'X-CSRFToken':csrftoken
        },
        body:JSON.stringify({'productId':productID})
    })

    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        alert("data", data)
    })
 }

 function getCookie(name){
    //split cookie string and get all individual name=value pairs in an array
    var cookieArray=document.cookie.split(";");

    //loop through the array elements
    for(var i=0; i<cookieArray.length; i++){
        var cookiePair=cookieArray[i].split("=");

        //remove space at the begining of cookie name and compare it with the given string
        if(name==cookiePair.trim){
            // decode the value and return 
            return decodeURIComponent(cookiePair[1]);
        }
    }
    //return null if not found
    return null;
 }

function addCookie(){


    var cart=JSON.parse(getCookie('cart'));
    if(cart==undefined){
       cart={};
       console.log("Cart was created");
       document.cookie='cart='+JSON.stringify(cart)+";domaain=;path=/"
    }
   
    console.log('Cart: ',cart)    
}