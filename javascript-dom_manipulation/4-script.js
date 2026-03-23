
document.querySelector('#add_item').addEventListener('click', () => {
  const myList = document.querySelector('.my_list');
  const newList = document.createElement('li');
  newList.textContent = 'Item';
  myList.appendChild(newList);
});
