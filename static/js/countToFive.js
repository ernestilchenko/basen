function countToHundred() {
    const counter = document.getElementById('to_100');
    const duration = 2000;
    const targetNumber = 100;
    const interval = 10;

    let currentNumber = 0;
    const increment = targetNumber / (duration / interval);

    const intervalId = setInterval(() => {
        currentNumber += increment; // Increment the number
        if (currentNumber >= targetNumber) {
            currentNumber = targetNumber; // Ensure it stops exactly at 100
            clearInterval(intervalId); // Stop the interval when the target is reached
        }
        counter.textContent = Math.floor(currentNumber); // Update the displayed number
    }, interval);
}

function countToFive() {
    const counter_5 = document.getElementById('to_5');
    const duration_5 = 2000; 
    const targetNumber_5 = 5;
    const interval_5 = 10;

    let currentNumber_5 = 0;
    const increment_5 = targetNumber_5 / (duration_5 / interval_5);

    const intervalId_5 = setInterval(() => {
        currentNumber_5 += increment_5;
        if (currentNumber_5 >= targetNumber_5) {
            currentNumber_5 = targetNumber_5;
            clearInterval(intervalId_5);
        }
        counter_5.textContent = Math.floor(currentNumber_5);
    }, interval_5);
}
function startCounting() {
    countToHundred();
    countToFive(); 
}
const countersSection = document.getElementById('to_100');
const observer = new IntersectionObserver(
    (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                startCounting();
                observer.unobserve(countersSection);
            }
        });
    },
    { threshold: 0.8 }
);
observer.observe(countersSection);

