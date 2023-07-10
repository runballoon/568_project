
window.onload = function () {
    var nodes = document.getElementById('nav-left').getElementsByTagName('li');

    for (var i = 0; i < nodes.length; i++) {
        nodes[i].addEventListener("click", function (ev) {
            var current = document.getElementsByClassName("active");
            current[0].className = current[0].className.replace("active", "");
            this.className = "active";
        })
    }
}