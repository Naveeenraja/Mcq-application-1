  document.addEventListener("DOMContentLoaded", function(event) {
    /*===== Expand side bar =====*/
   
    const showNavbar = (toggleId, navId, bodyId, headerId) =>{
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId),
    bodypd = document.getElementById(bodyId),
    headerpd = document.getElementById(headerId)
    // Validate that all variables exist
    if(toggle && nav && bodypd && headerpd){
    toggle.addEventListener('click', ()=>{
    // show navbar
    nav.classList.toggle('show')
    // change icon
    toggle.classList.toggle('bx-x')
    // add padding to body
    bodypd.classList.toggle('body-pd')
    // add padding to header
    headerpd.classList.toggle('body-pd')
    })
    }
    }
    
    showNavbar('header-toggle','nav-bar','body-pd','header')
    
    /*===== LINK ACTIVE =====*/
    const linkColor = document.querySelectorAll('.nav_link')
    
    function colorLink(){
    if(linkColor){
    linkColor.forEach(l=> l.classList.remove('active'))
    linkColor.forEach(l=> l.classList.remove('bg-primary'))
    this.classList.add('active')
    this.classList.add('bg-primary')
    var str= this.id
    console.log(str)
    if (str === "about"){
        $('#content').load("/tab/about");
    }
    else if (str=== "dashboard"){

        $('#content').load("/tab/dashboard");
    }
    else if (str=== "test"){

        $('#content').load("/tab/test");
    }
    else if (str=== "mark"){

        $('#content').load("/tab/mark");
    }
    else if (str=== "help"){
        $('#content').load("/tab/help");

    }
    else if (str=== "stats"){
        $('#content').load("/tab/status");
    
    }
    }
    }
    linkColor.forEach(l=> l.addEventListener('click', colorLink))
    
     // Your code to run since DOM is loaded and ready
    });