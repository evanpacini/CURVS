var keys = [];
var velocityHTML = document.getElementById("velocities");
var tdm = true; // Tank drive mode
velocityHTML.innerHTML = "Velocities: 0, 0";
// QASW
// Q=left+ A=left- S=right- W=right+
// WASD
// W=thrust+ A=left S=thrust- D=right
document
  .getElementById("tdm")
  .addEventListener("change", () => (tdm = this.checked));

window.addEventListener(
  "keydown",
  function (e) {
    if (!keys.includes(e.key)) {
      keys.push(e.key);
    }
    velocityHTML.innerHTML =
      "Velocities: " + keysToSpeed(keys).join(", ").toString();
  },
  false
);

window.addEventListener(
  "keyup",
  function (e) {
    keys = keys.filter((item) => item !== e.key);
    velocityHTML.innerHTML =
      "Velocities: " + keysToSpeed(keys).join(", ").toString();
  },
  false
);

function keysToSpeed(keys) {
  if (tdm) {
    var v1 = keys.includes("q") - keys.includes("a"); // left motor
    var v2 = keys.includes("w") - keys.includes("s"); // right motor
    return [v1, v2];
  } else {
    var v1 = keys.includes("w") - keys.includes("s"); // thrust
    var v2 = keys.includes("d") - keys.includes("a"); // direction
    return [v1, v2];
  }
}
