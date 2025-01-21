
const header = document.querySelector('.header');

// Add a scroll event listener to the window
window.addEventListener('scroll', () => {
    // Check the scroll position
    if (window.scrollY > 50) { // Change the opacity after scrolling 50px
        header.style.background = 'rgba(255, 255, 255, 0.8)'; // Set opacity when scrolled
    } else {
        header.style.background = 'rgba(255, 255, 255, 1)'; // Restore opacity when at the top
    }
});








