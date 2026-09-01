function toggleOn() {
    document.getElementById("container-3").style.display = "block";
    document.getElementById("toggle").setAttribute("onchange", "toggleOff()");
}
function toggleOff() {
    document.getElementById("container-3").style.display = "none";
    document.getElementById("toggle").setAttribute("onchange", "toggleOn()");
}