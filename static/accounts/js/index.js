button = document.getElementById('clicker');
tk =document.getElementById('bye')

console.log(button)


  function myfunction(){
    document.getElementById('bye').innerHTML= 'This is from javascript, <br> this means javascript is working!';
  }


  document.getElementById('home-robot1').addEventListener('mouseover', function(){
    document.getElementById('rbt-text').style.opacity = "1";
    setTimeout(function(){
      document.getElementById('rbt-text').style.opacity = "0";
    }, 1500);
      

    console.log("hello i am working")
  })
  console.log("hello i am working")
