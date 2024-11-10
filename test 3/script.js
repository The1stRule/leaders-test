
const form = document.getElementById('myForm');
const errorMessage = document.getElementById('error-message')


const formSubmit = () => {
    const city = form.city.value;

    errorMessage.style.display = 'none';

    if(city === '') {
        errorMessage.textContent = 'Fill out all fields';
        errorMessage.style.display = 'block';
        return;
    }
}


form.addEventListener('submit', (e) => {
    e.preventDefault();

    formSubmit();
});