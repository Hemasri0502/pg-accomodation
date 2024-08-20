
var email = document.querySelector("#username")
var password = document.querySelector("#password")
var but = document.querySelector("#button")

function auth(){
    if(email.value==="abc"){
        if(password.value==='123'){
            
            alert('login successful')
        }
        else{
            alert('invalid password')
        }
    }
    else{
        alert('invalid username')
    }

    
}
but.addEventListener('click',auth)