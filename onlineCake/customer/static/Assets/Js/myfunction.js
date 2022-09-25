
 var addtoCartButtons=document.getElementsByClassName("cart");

 for(var i=0; i<addtoCartButtons.length; i++){
    addtoCartButtons[i].addEventListener('click',function(){
        var productID=this.dataset.product;
        var action=this.dataset.action;
        
        addCookie(productID, action);
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


function addCookie(productId, action){
	console.log('User is not authenticated')

	if (action == 'add'){

        if (cart[productId] == undefined){
        cart[productId] = {'quantity':1}

        }else{
            cart[productId]['quantity'] += 1
        }
        alert("item addded successfully")
         

	}

	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
}

