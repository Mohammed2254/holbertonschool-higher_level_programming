const red_header = document.getElementById("red_header");
const myheader = document.querySelector("header");
red_header.addEventListener('click', () => {
	myheader.classList.add('red');
});
