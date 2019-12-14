function whichDisplay() {
  // Get the checkbox
  var checkBox = document.getElementById("checkbox1");
  // Get the output text
  var l = document.getElementById("l");
  var s = document.getElementById("s");

  // If the checkbox is checked, display the output text
  if (checkBox.checked == true){
    s.style.display = "block";
    l.style.display = "none";
  } else {
    l.style.display = "block";
    s.style.display = "none";
  }
}