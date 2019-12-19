// Bulma burger navibar js
document.addEventListener('DOMContentLoaded', () => {
    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {

        // Add a click event on each of them
        $navbarBurgers.forEach(el => {
            el.addEventListener('click', () => {

                // Get the target from the "data-target" attribute
                const target = el.dataset.target;
                const $target = document.getElementById(target);

                // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
                el.classList.toggle('is-active');
                $target.classList.toggle('is-active');

            });
        });
    }

});

// Ask for ensure when delete an article js
const tiles = document.getElementsByClassName("is-child");
for (const i = 0; i < tiles.length; i++) {
    tiles[i].addEventListener('mouseover', function () {
        this.className += " animated pulse";
    });
    tiles[i].addEventListener('mouseout', function () {
        this.className = this.className.replace(" animated pulse", "");
    });
}


// Bulma upload file js which is used to display the filename.

const fileInput = document.querySelector('#file-js input[type=file]');
fileInput.onchange = () => {
    if (fileInput.files.length > 0) {
        const fileName = document.querySelector('#file-js .file-name');
        fileName.textContent = fileInput.files[0].name;
    }
}

