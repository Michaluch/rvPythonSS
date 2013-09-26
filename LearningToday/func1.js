function randomNumber(){
    return Math.round(Math.random() * 255);
}

function randomColor() {
    color = "#"+(randomNumber()).toString(16)+(randomNumber()).toString(16)+(randomNumber()).toString(16);
    return color;
        
}

function changeColor() 
{
    var a = document.getElementsByClassName('block');
    
    for(var i = 0; i < a.length; i++)
    {
        a[i].style.background = randomColor();
    }
}

window.onload = OnloadFunction
    
function OnloadFunction()    
    {
    changeColor();
    
    var searchform = document.getElementById("search")
    searchform.onblur = function(){
        if (this.value == '') {this.setAttribute('value', 'Search courses')};
        }
    searchform.onfocus = function() {
        if (this.value == 'Search courses') {this.setAttribute('value', '')};
    }
    
    var a = document.getElementsByClassName('block');
    
    for(var i = 0; i < a.length; i++)
    {
        a[i].onmouseover = function() {
            this.style.background = randomColor();
            }
    }
    
    b = document.getElementById("buttonchange")
    b.onclick = function(){
        changeColor();}
    }


