
function getRandom() {
	var temp = Math.floor((Math.random() * 255));
	return temp;
}

function changeToRandom(name) {
	var temp = "rgb(" + getRandom() + "," + getRandom() + "," + getRandom() + ")";
	var temp_rgba = ("rgba" + temp.slice(3,-1) + ",0.65);");
	document.getElementById(name).style.backgroundColor = temp;
	
/* 	alert(temp_rgba); */
	var css = '#' + name + ':hover{box-shadow:0 0 0px 10px ' + temp_rgba + '}';
	style = document.createElement('style');
	if (style.styleSheet) style.styleSheet.cssText = css;
	else style.appendChild(document.createTextNode(css));
	document.getElementsByTagName('head')[0].appendChild(style);
}

function hide_text() {
	document.getElementById("main_search_form").placeholder = "";
}

function show_text() {
	document.getElementById("main_search_form").placeholder = "Search courses";
}

function changeBoxAll() {
		var elements = document.getElementsByClassName("main_box_style");
		for (var i = 0, len = elements.length; i < len; i++) {
			changeToRandom(elements[i].id); /* 		alert(elements[i].id) */
		}
	}

function changeBoxOne(name) {
	changeToRandom(name.id);
}

window.onload = function()
{
	changeBoxAll()	
}