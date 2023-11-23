document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    if (username.trim() === '' || password.trim() === '') {
        alert('Por favor, complete todos los campos.');
    } else {
        // Aquí puede agregar la lógica para enviar el formulario y validar las credenciales de los usuarios.
        alert('Usuario y contraseña validados con éxito.');
    }
});