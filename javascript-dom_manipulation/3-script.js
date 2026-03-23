const toggleHeader = document.querySelector('#toggle_header');
const header = document.querySelector('header');

toggleHeader.addEventListener('click', () => {
  const nextClass = header.classList.contains('red') ? 'green' : 'red';

  header.classList.remove('red', 'green');
  header.classList.add(nextClass);
});
