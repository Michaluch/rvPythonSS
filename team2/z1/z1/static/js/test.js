/**
 * Created with PyCharm.
 * User: alex
 * Date: 9/4/13
 * Time: 6:37 PM
 * To change this template use File | Settings | File Templates.
 */
var plates = document.getElementsByClassName("course-plate");
var focused_plate = null;
var focused_plate_bgcolor = null;
var mouseover_plate = null;
var mouseover_plate_bgcolor = null;
var plates_alternative_colour = false;


function has_class(elem, klass) {
     return (" " + elem.className + " " ).indexOf( " "+klass+" " ) > -1;
}

function get_random_color() {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.round(Math.random() * 15)];
    }
    return color;
}

function color_plates() {
    for (var i = 0; i < plates.length; i++) {
        var color_class = plates[i].className.split(' ')[1];
        switch (color_class) {
            case "plate-green":
                plates[i].style.backgroundColor = "#20a24b";
                break;
            case "plate-orange":
                plates[i].style.backgroundColor = "#f28e22";
                break;
            case "plate-skyblue":
                plates[i].style.backgroundColor = "#22b0f2";
                break;
            case "plate-red":
                plates[i].style.backgroundColor = "#a40f0f";
                break;
            case "plate-salat":
                plates[i].style.backgroundColor = "#22f2a1";
        }
    }
}

function color_plates_alternative(){
    for (var i = 0; i < plates.length; i++) {
        plates[i].style.backgroundColor = get_random_color();
    }
}



window.onload = function() {

    color_plates();

    var search_frontpage = document.getElementById("search-frontpage");
    search_frontpage.onfocus = function() {
        this.removeAttribute("placeholder");
    }
    search_frontpage.onblur = function() {
        if(this.value == ""){
        this.setAttribute("placeholder", "Search courses");
    }
    }

    var logo_button = document.getElementById("logo-button");
    logo_button.onclick = function(){
        if (!plates_alternative_colour){
            color_plates_alternative();
            plates_alternative_colour = true;
        }else{
            color_plates();
            plates_alternative_colour = false;
        }
    }

    document.onfocus = function(event) {
        document.getElementById("temp").innerHTML = event.target + " focused";
    }

    document.onblur = function(event) {
        document.getElementById("temp").innerHTML = event.target + " blured";
    }

    document.onclick = function(event) {
        if (has_class(event.target, "course-plate")) {
            if((focused_plate !== null) && (focused_plate_bgcolor !== null)) {
                focused_plate.style.backgroundColor = focused_plate_bgcolor;
            }
            focused_plate_bgcolor = mouseover_plate_bgcolor || event.target.style.backgroundColor;
            focused_plate = event.target;
            event.target.style.backgroundColor = "#333333";
        }else if(!has_class(event.target, "course-plate")){
            if((focused_plate !== null) && (focused_plate_bgcolor !== null)) {
                focused_plate.style.backgroundColor = focused_plate_bgcolor;
                focused_plate_bgcolor = null;
            }
        }
    }

    document.onmouseover = function(event) {
        if(has_class(event.target, "course-plate")) {
            mouseover_plate_bgcolor = event.target.style.backgroundColor;
            mouseover_plate = event.target;
            event.target.style.backgroundColor = get_random_color();
        }
    }
    document.onmouseout = function(event) {
        if(has_class(event.target, "course-plate") && (mouseover_plate_bgcolor !== null)){
            event.target.style.backgroundColor = mouseover_plate_bgcolor;
        }
    }


}

