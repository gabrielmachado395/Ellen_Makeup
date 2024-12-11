document.querySelectorAll('.btn-quantidade').forEach(button => {
    button.addEventListener('click', function () {
        const quantidadeSpan = this.parentElement.querySelector('.quantidade');
        let quantidade = parseInt(quantidadeSpan.textContent);

        if (this.textContent === '+') {
            quantidade += 1;
        } else if (this.textContent === '-' && quantidade > 1) {
            quantidade -= 1;
        }

        quantidadeSpan.textContent = quantidade;

        
    })
})