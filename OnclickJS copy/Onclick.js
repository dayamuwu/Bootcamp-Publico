function mens_alert(){
    alert("Ninja was liked");
}

function cambio(){
    var uno = document.getElementById('btn1');
    if (uno.innerText == 'Logout')
        uno.innerHTML = 'Login';
    else uno.innerHTML = 'Logout'; 
}

function borrar(){
    document.getElementById('btn3').remove();

}