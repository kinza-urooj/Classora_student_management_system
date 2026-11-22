// Small frontend behavior: dismiss flash messages after a few seconds.
document.querySelectorAll(".flash").forEach(function(message) {
  setTimeout(function() {
    message.style.transition = "opacity .5s";
    message.style.opacity = "0";
    setTimeout(function() { message.remove(); }, 500);
  }, 4500);
});

// Light and Dark Mode Toggle
const themeButton = document.getElementById("themeToggle");

// Load saved theme when page opens
if (localStorage.getItem("theme") === "light") {
    document.body.classList.add("light-mode");
    themeButton.innerHTML = "☾";
}

// Change theme when button is clicked
themeButton.addEventListener("click", function () {

    document.body.classList.toggle("light-mode");

    // If light mode is active
    if (document.body.classList.contains("light-mode")) {
        localStorage.setItem("theme", "light");
        themeButton.innerHTML = "☾";
    }

    // Otherwise use dark mode
    else {
        localStorage.setItem("theme", "dark");
        themeButton.innerHTML = "☀";
    }
});