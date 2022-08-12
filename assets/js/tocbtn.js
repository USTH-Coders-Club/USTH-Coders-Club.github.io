let tocbtn = () => {
    let x = document.getElementById("my_toc");
    if (x.style.display === "none") {
        x.style.display = "block";
        document.getElementById("btntoc").innerHTML = "Hide";
    }
    else {
        x.style.display = "none";
        document.getElementById("btntoc").innerHTML = "Show";
    }
}