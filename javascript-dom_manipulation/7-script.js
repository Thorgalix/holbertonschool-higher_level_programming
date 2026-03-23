const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then(response => response.json())
  .then(data => {
    const listMovies = document.querySelector('#list_movies');
    data.results.forEach(film => {
      const newList = document.createElement('li');
      newList.textContent = film.title;
      listMovies.appendChild(newList);
    });
  });
