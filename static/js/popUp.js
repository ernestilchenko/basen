
// Wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function () {
    // Select elements
    const fourthScreenTitle = document.querySelector('.fourth-screen-title');
    const popup = document.querySelector('.popup');
    
    // Timer to trigger the popup
    setTimeout(() => {
    // Hide the first-screen-title
    if (fourthScreenTitle) {
        fourthScreenTitle.style.display = 'none';
    }
    
    // Show the popup with animation
    if (popup) {
        popup.classList.add('show');
    }
    }, 3000); // 5000ms = 5 seconds
    });