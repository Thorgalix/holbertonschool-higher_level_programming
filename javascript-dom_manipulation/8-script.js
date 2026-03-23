const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';

document.addEventListener('DOMContentLoaded', () => {
  fetch(url)
    .then(response => response.json())
    .then(data => {
      const hello = document.querySelector('#hello');
      hello.textContent = data.hello;
    });
});
