var keys = [];
var locus = document.getElementById("keypresses");
locus.innerHTML = "Keys currently pressed: ";
window.addEventListener(
  "keydown",
  function (e) {
    if (!keys.includes(e.key)) {
      keys.push(e.key);
    }
    locus.innerHTML = "Keys currently pressed:" + keys.join(", ").toString();
  },
  false
);

window.addEventListener(
  "keyup",
  function (e) {
    keys = keys.filter((item) => item !== e.key);
    locus.innerHTML = "Keys currently pressed: " + keys.join(", ").toString();
  },
  false
);
