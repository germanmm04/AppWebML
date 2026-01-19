// Validación del formulario en el lado del cliente
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('predictionForm');
    const submitBtn = document.getElementById('submitBtn');
    const btnText = document.getElementById('btnText');
    const btnLoader = document.getElementById('btnLoader');

    // Función para mostrar errores
    function showError(fieldId, errorId, message) {
        const field = document.getElementById(fieldId);
        const errorSpan = document.getElementById(errorId);
        field.classList.add('error');
        errorSpan.textContent = message;
        errorSpan.style.display = 'block';
    }

    // Función para limpiar errores
    function clearError(fieldId, errorId) {
        const field = document.getElementById(fieldId);
        const errorSpan = document.getElementById(errorId);
        field.classList.remove('error');
        errorSpan.textContent = '';
        errorSpan.style.display = 'none';
    }

    // Validación en tiempo real
    document.getElementById('marca').addEventListener('blur', function() {
        const value = this.value.trim();
        if (!value) {
            showError('marca', 'error-marca', 'La marca es obligatoria');
        } else if (value.length < 2) {
            showError('marca', 'error-marca', 'La marca debe tener al menos 2 caracteres');
        } else {
            clearError('marca', 'error-marca');
        }
    });

    document.getElementById('modelo').addEventListener('blur', function() {
        const value = this.value.trim();
        if (!value) {
            showError('modelo', 'error-modelo', 'El modelo es obligatorio');
        } else if (value.length < 2) {
            showError('modelo', 'error-modelo', 'El modelo debe tener al menos 2 caracteres');
        } else {
            clearError('modelo', 'error-modelo');
        }
    });

    document.getElementById('combustible').addEventListener('change', function() {
        if (!this.value) {
            showError('combustible', 'error-combustible', 'Debes seleccionar un tipo de combustible');
        } else {
            clearError('combustible', 'error-combustible');
        }
    });

    document.getElementById('transmision').addEventListener('change', function() {
        if (!this.value) {
            showError('transmision', 'error-transmision', 'Debes seleccionar un tipo de transmisión');
        } else {
            clearError('transmision', 'error-transmision');
        }
    });

    document.getElementById('kilometraje').addEventListener('blur', function() {
        const value = parseFloat(this.value);
        if (!this.value) {
            showError('kilometraje', 'error-kilometraje', 'El kilometraje es obligatorio');
        } else if (isNaN(value) || value < 0) {
            showError('kilometraje', 'error-kilometraje', 'El kilometraje debe ser un número positivo');
        } else if (value > 1000000) {
            showError('kilometraje', 'error-kilometraje', 'El kilometraje no puede ser mayor a 1,000,000 km');
        } else {
            clearError('kilometraje', 'error-kilometraje');
        }
    });

    document.getElementById('anio').addEventListener('blur', function() {
        const value = parseInt(this.value);
        const currentYear = new Date().getFullYear();
        if (!this.value) {
            showError('anio', 'error-anio', 'El año es obligatorio');
        } else if (isNaN(value) || value < 1900 || value > currentYear) {
            showError('anio', 'error-anio', `El año debe estar entre 1900 y ${currentYear}`);
        } else {
            clearError('anio', 'error-anio');
        }
    });

    // Validación al enviar el formulario
    form.addEventListener('submit', function(e) {
        let isValid = true;

        // Validar todos los campos
        const marca = document.getElementById('marca').value.trim();
        const modelo = document.getElementById('modelo').value.trim();
        const combustible = document.getElementById('combustible').value;
        const transmision = document.getElementById('transmision').value;
        const kilometraje = parseFloat(document.getElementById('kilometraje').value);
        const anio = parseInt(document.getElementById('anio').value);

        // Validar marca
        if (!marca || marca.length < 2) {
            showError('marca', 'error-marca', 'La marca es obligatoria y debe tener al menos 2 caracteres');
            isValid = false;
        }

        // Validar modelo
        if (!modelo || modelo.length < 2) {
            showError('modelo', 'error-modelo', 'El modelo es obligatorio y debe tener al menos 2 caracteres');
            isValid = false;
        }

        // Validar combustible
        if (!combustible) {
            showError('combustible', 'error-combustible', 'Debes seleccionar un tipo de combustible');
            isValid = false;
        }

        // Validar transmisión
        if (!transmision) {
            showError('transmision', 'error-transmision', 'Debes seleccionar un tipo de transmisión');
            isValid = false;
        }

        // Validar kilometraje
        if (!document.getElementById('kilometraje').value || isNaN(kilometraje) || kilometraje < 0 || kilometraje > 1000000) {
            showError('kilometraje', 'error-kilometraje', 'El kilometraje debe ser un número entre 0 y 1,000,000');
            isValid = false;
        }

        // Validar año
        const currentYear = new Date().getFullYear();
        if (!document.getElementById('anio').value || isNaN(anio) || anio < 1900 || anio > currentYear) {
            showError('anio', 'error-anio', `El año debe estar entre 1900 y ${currentYear}`);
            isValid = false;
        }

        if (!isValid) {
            e.preventDefault();
            return false;
        }

        // Mostrar loader mientras se procesa
        submitBtn.disabled = true;
        btnText.style.display = 'none';
        btnLoader.style.display = 'inline-block';
    });

    // Limpiar errores al escribir
    const inputs = form.querySelectorAll('input, select');
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            const errorId = 'error-' + this.id;
            const errorSpan = document.getElementById(errorId);
            if (errorSpan) {
                clearError(this.id, errorId);
            }
        });
    });
});
