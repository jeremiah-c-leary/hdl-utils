// JavaScript

document.querySelector("#car_summary").addEventListener("click", function (evt) {
  document.querySelector("#car_signals").setAttribute("visibility", "visible");
  document.querySelector("#clocks_and_resets").setAttribute("height", 100);
  document.querySelector("#car_summary").setAttribute("visibility", "hidden");
});

document.querySelector("#car_signals").addEventListener("click", function (evt) {
  document.querySelector("#car_signals").setAttribute("visibility", "hidden");
  document.querySelector("#clocks_and_resets").setAttribute("height", 50);
  document.querySelector("#car_summary").setAttribute("visibility", "visible");
});



document.querySelector("#if1_summary").addEventListener("click", function (evt) {
  document.querySelector("#if1_signals").setAttribute("visibility", "visible");
  document.querySelector("#Interface1").setAttribute("height", 125);
  document.querySelector("#if1_summary").setAttribute("visibility", "hidden");
});

document.querySelector("#if1_signals").addEventListener("click", function (evt) {
  document.querySelector("#if1_signals").setAttribute("visibility", "hidden");
  document.querySelector("#Interface1").setAttribute("height", 50);
  document.querySelector("#if1_summary").setAttribute("visibility", "visible");
});

document.querySelector("#if2_summary").addEventListener("click", function (evt) {
  document.querySelector("#if2_signals").setAttribute("visibility", "visible");
  document.querySelector("#Interface2").setAttribute("height", 125);
  document.querySelector("#if2_summary").setAttribute("visibility", "hidden");
});

document.querySelector("#if2_signals").addEventListener("click", function (evt) {
  document.querySelector("#if2_signals").setAttribute("visibility", "hidden");
  document.querySelector("#Interface2").setAttribute("height", 50);
  document.querySelector("#if2_summary").setAttribute("visibility", "visible");
});
