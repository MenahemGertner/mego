var counter = 0;
function clicked(element) {
  const p = element.firstElementChild;
  const about = document.getElementById("about");
  p.innerHTML = `clicked ${++counter} times`;
  about.style.borderRadius = counter % 2 === 0 ? "0" : "25px";
}
