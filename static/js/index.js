button = document.getElementById('clicker');
tk =document.getElementById('bye')

button.addEventListener('click', myfunction);

function myfunction()
{
tk.innerHTML= 'This is from javascript, <br> this means javascript is working!';
}