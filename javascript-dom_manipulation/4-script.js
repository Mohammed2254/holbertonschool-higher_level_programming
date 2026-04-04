const add_ietm = document.getElementById('add_item');
const insert_li = document.querySelector('.my_list');
add_ietm.addEventListener('click', () => {
	const newLi = document.createElement('li');
	newLi.textContent = "Item";
	insert_li.appendChild(newLi);
});