document.addEventListener('DOMContentLoaded', () => {
    AOS.init({
    duration: 800, // Длительность анимации (в миллисекундах)
    offset: 100, // Смещение (в пикселях) перед началом анимации
    easing: "ease-in-out", // Тип плавности (CSS transition easing)
    delay: 0, // Задержка (в миллисекундах)
    once: true, // Анимация происходит только один раз (если false — повторяется при каждом скролле)
    });
    });
    