document.addEventListener('DOMContentLoaded', () => {
  const hello = document.querySelector('#hello');

  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then((response) => {
      if (!response.ok) {
        throw new Error('Failed to fetch translation');
      }

      return response.json();
    })
    .then((data) => {
      hello.textContent = data.hello;
    })
    .catch(() => {
      hello.textContent = 'Unable to load translation';
    });
});
