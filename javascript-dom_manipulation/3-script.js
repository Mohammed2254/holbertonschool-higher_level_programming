const red_header = document.getElementById("toggle_header");
const myheader = document.querySelector("header");
red_header.addEventListener('click', () => {
	if (myheader.classList.contains('green')) {
		myheader.classList.remove('green');
		myheader.classList.add('red');
	}
	else {
		myheader.classList.remove('red');
		myheader.classList.add('green');
	}

})