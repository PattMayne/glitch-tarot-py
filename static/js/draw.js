$(document).foundation()

// Find out if the user allowed reversals
document.addEventListener("DOMContentLoaded", () =>
    !!parseInt(document.getElementById("allow_reversals").dataset.value)
    && do_rotations()
);

// I originally wanted the dealer to be able to click the image and rotate it.
// But I decided that should be randomized.
// Anyway, this rotates the image.
// The other functions are (currently) stupidly declarative but this needs to be more readable.
const rotate = (id) => {
    let img = document.getElementById(id);
    let rotation = parseInt(img.style.rotate.replace("deg", "").trim());
    rotation = rotation == 0 ? 180 : 0;
    rotate_string = rotation.toString() + "deg";
    img.style.rotate = rotate_string;

    // update the alt description
    img.alt = img.alt + " REVERSED";

    // Now resize the container

    let container = document.getElementById('container_' + id);
    setTimeout(() => {
        const rect = img.getBoundingClientRect();
        container.style.width = rect.width + 'px';
    }, 0);
}


// get all the IMG elements, run a function on them to randomly possibly reverse the card.
const do_rotations = () => Array.from(document.getElementsByClassName("tarot_img")).map(
        img => Math.floor(Math.random() * 5) == 0 && rotate(img.id))
