var yourHeading = document.querySelector('h4');

yourHeading.textContent = "It's a beautiful day";

// event
document.getElementById('my_cat').onclick = function() {
	alert('Meowwwwwwwwwwwwwwwwww');
}

var myImage = document.getElementById('the_fox');

myImage.onclick = function() {
	var mySrc = myImage.getAttribute('src');
	if (mySrc === 'images/firefox_logo.jpg') {
		myImage.setAttribute('src', 'images/firefox_logo1.jpg');
	} else {
		myImage.setAttribute('src', 'images/firefox_logo.jpg');
	}
}

var myButton = document.querySelector('button');
var myHeading = document.querySelector('h3');

function setUserName() {
	var myName = prompt('Please enter your name.');
	localStorage.setItem('name', myName);
	myHeading.textContent = 'Hello, ' + myName;
}

if (!localStorage.getItem('name')) {
	setUserName();
} else {
	var storedName = localStorage.getItem('name');
	myHeading.textContent = 'Hello, ' + storedName;
}

myButton.onclick = function() {
	setUserName();
}

/*	
**	Syntax
*/

var iceCream = 'chocolate';

if (iceCream === 'chocolate') {
	alert('Yay');
} else {
	alert('AWWWWWWWWWWWWwww');
}

function multiply(n1,n2) {
	return result;
}