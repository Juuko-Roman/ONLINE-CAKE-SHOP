 $("i").click(function(){
     $(this).toggleClass("fa-thumbs-down");
 });

 var addtoCartButtons=document.getElementsByClassName("cart");

 for(var i=0; i<addtoCartButtons.length; i++){
    addtoCartButtons[i].addEventListener('click',function(){
        var productID=this.dataset.product;
        
        addCookie(productID);
        // UpdateUserOrder(productID);  this is for authenticatedusers
    })
 }

//  function UpdateUserOrder(productID){
//     alert(productID);

//     var url='/updateItem/';

//     fetch(url,{
//         method:'POST',
//         headers:{
//             'content-type':'application/json',
//             'X-CSRFToken':csrftoken
//         },
//         body:JSON.stringify({'productId':productID})
//     })

//     .then((response)=>{
//         return response.json()
//     })

//     .then((data)=>{
//         alert("data:"+data)
//     })
//  }



function addCookie(productId){

    alert(productId);
    if(cart[productId] == undefined){
        cart[productId]={'quantity':1};
    }
    else{
        cart[productId]['quantity']+=1;
    }        
    console.log(cart);
    document.cookie='cart='+JSON.stringify(cart)+";domaain=;path=/";
    
}