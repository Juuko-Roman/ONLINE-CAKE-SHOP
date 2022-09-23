function getCookie(name){
    var cookieValue=null;
    if(document.cookie && document.cookie !==''){

        //split cookie string and get all individual name=value pairs in an array
        var cookieArray=document.cookie.split(";");

        //loop through the array elements
        for(var i=0; i<cookieArray.length; i++){
            var cookie=cookieArray[i].trim();

            //Doesthis cookiebegin with the name we want 
            if(cookie.substring(0,name.length+1)==(name+'=')){
                // decode the value and return 
                cookieValue = decodeURIComponent(cookie.substring(name.length+1));
                break;
            }
        }        
    }
    //return cookie value
    return cookieValue;
 }
 var csrftoken=getCookie('csrftoken');