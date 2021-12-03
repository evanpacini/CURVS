var keys = [];
var velocityHTML = document.getElementById("velocities");
var tdm = document.getElementById("tdm"); // Tank drive mode
velocityHTML.innerHTML = "Velocities: 0, 0";
// QASW
// Q=left+ A=left- S=right- W=right+
// WASD
// W=thrust+ A=left S=thrust- D=right
tdm.addEventListener("change", () => {
  console.log("Tank drive mode: " + tdm.checked);
});

window.addEventListener(
  "keydown",
  function (e) {
    if (!keys.includes(e.key)) {
      keys.push(e.key);
    }
    onKeyEvent();
  },
  false
);

window.addEventListener(
  "keyup",
  function (e) {
    keys = keys.filter((item) => item !== e.key);
    onKeyEvent();
  },
  false
);

function onKeyEvent() {
  vs = keysToVs(keys);
  velocityHTML.innerHTML = "Velocities: " + vs.join(", ").toString();
  postVs(vs);
}

function keysToVs(keys) {
  if (tdm.checked) {
    var v1 = keys.includes("q") - keys.includes("a"); // left motor
    var v2 = keys.includes("w") - keys.includes("s"); // right motor
    return [v1, v2];
  } else {
    var v1 = keys.includes("w") - keys.includes("s"); // thrust
    var v2 = keys.includes("d") - keys.includes("a"); // direction
    return [v1, v2];
  }
}

function postVs(vs) {
  fetch("/motor-control", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ vs })
  });
}
