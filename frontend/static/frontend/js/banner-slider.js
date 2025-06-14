document.addEventListener("DOMContentLoaded", function () {
  const banner = document.querySelector(".banner");
  const images = [
    "/static/frontend/img/b_m_w.jpg",
    "/static/frontend/img/mercedes_benz_class_gle.jpg",
    "/static/frontend/img/mercedes_class_s.jpg",
    "/static/frontend/img/lamborghini_noir.jpg"
  ];
  let index = 0;

  function changeBackground() {
    index = (index + 1) % images.length;
    banner.style.backgroundImage = `url('${images[index]}')`;
  }

  // Initial set
  banner.style.backgroundImage = `url('${images[0]}')`;

  // Change every 2 seconds
  setInterval(changeBackground, 2000);
});
