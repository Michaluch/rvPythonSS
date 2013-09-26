
window.onload()
    {
    changeColor();
    }   

function randomColor() {
    var index = Math.round(Math.random() * 9);

    var ColorValue = "#FF0066 "; 
    if(index == 1)
        ColorValue = "#7B68EE"; 
    if(index == 2)
        ColorValue = "#3333CC"; 
    if(index == 3)
        ColorValue = "#CC6633"; 
    if(index == 4)
        ColorValue = "#660066"; 
    if(index == 5)
        ColorValue = "#3333CC"; 
    if(index == 6)
        ColorValue = "#00BFFF"; 
    if(index == 7)
       ColorValue = "#663333"; 
    if(index == 8)
        ColorValue = "#FF0033"; 
    if(index == 9)
        ColorValue = "#FF0033"; 
        return ColorValue;
        
}

function changeColor() 
{
    var a = document.getElementsByClassName('block');
    
    for(var i = 0; i < a.length; i++)
    {
        a[i].style.background = randomColor();
    }
}

function donotdo() {}
