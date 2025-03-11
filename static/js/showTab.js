function showTab(index) {
    const tabs = document.querySelectorAll('.tab-content');
    const buttons = document.querySelectorAll('.tab-button');

    tabs.forEach(tab => tab.classList.remove('active'));
    buttons.forEach(button => button.classList.remove('active'));

    tabs[index].classList.add('active');
    buttons[index].classList.add('active');
}

document.addEventListener('DOMContentLoaded', () => {
    showTab(0);
});