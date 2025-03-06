const textarea = document.getElementById('enhancedTextarea');
const charCount = document.getElementById('enhancedCharCount');

textarea.addEventListener('input', () => {
const remaining = 200 - textarea.value.length;
charCount.textContent = `Pozostało ${remaining} symbołów`;
});