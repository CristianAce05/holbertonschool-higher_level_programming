const listMovies = document.querySelector('#list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => {
    if (!response.ok) {
      throw new Error('Failed to fetch movies');
    }

    return response.json();
  })
  .then((data) => {
    data.results.forEach((movie) => {
      const listItem = document.createElement('li');

      listItem.textContent = movie.title;
      listMovies.appendChild(listItem);
    });
  })
  .catch(() => {
    listMovies.textContent = 'Unable to load movies';
  });
