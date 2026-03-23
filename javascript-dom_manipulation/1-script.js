const redHeader = document.querySelector('#red_header');
const header = document.querySelector('header');

redHeader.addEventListener('click', () => {
  header.style.color = '#FF0000';
});
