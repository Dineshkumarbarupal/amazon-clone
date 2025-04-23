const hamburger = document.getElementById('_c_b');
const sideMenu = document.getElementById('sideMenu');
const closeBtn = document.getElementById('closeBtn');

hamburger.addEventListener('click', () => {
  console.log("Menu clicked");
  sideMenu.classList.add('open');
});

closeBtn.addEventListener('click', () => {
  sideMenu.classList.remove('open');
});
