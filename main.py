from flask import Flask, render_template, request
import joblib
import pandas as pd
import os
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Cargar modelo entrenado (usar ruta compatible con Linux/Windows)
try:
    ruta_modelo = os.path.join('modelos', 'randomforest_vehiculos.pkl')
    modelo = joblib.load(ruta_modelo)
    app.logger.info("Modelo cargado correctamente")
except Exception as e:
    app.logger.error(f"Error al cargar el modelo: {str(e)}")
    modelo = None

# Tasa fija de conversión (rupias -> euros)
# [No verificado] Tasa fija usada únicamente con fines académicos
INR_POR_EURO = 90

def validar_datos(marca, modelo_nombre, combustible, transmision, kilometraje, anio):
    """Valida los datos del formulario"""
    errores = []
    
    # Validar marca
    if not marca or len(marca.strip()) < 2:
        errores.append("La marca debe tener al menos 2 caracteres")
    
    # Validar modelo
    if not modelo_nombre or len(modelo_nombre.strip()) < 2:
        errores.append("El modelo debe tener al menos 2 caracteres")
    
    # Validar combustible
    if combustible not in ['Petrol', 'Diesel']:
        errores.append("Tipo de combustible inválido")
    
    # Validar transmisión
    if transmision not in ['Manual', 'Automatic']:
        errores.append("Tipo de transmisión inválido")
    
    # Validar kilometraje
    try:
        km = float(kilometraje)
        if km < 0 or km > 1000000:
            errores.append("El kilometraje debe estar entre 0 y 1,000,000 km")
    except (ValueError, TypeError):
        errores.append("El kilometraje debe ser un número válido")
    
    # Validar año
    try:
        año_int = int(anio)
        año_actual = 2025
        if año_int < 1900 or año_int > año_actual:
            errores.append(f"El año debe estar entre 1900 y {año_actual}")
    except (ValueError, TypeError):
        errores.append("El año debe ser un número válido")
    
    return errores

@app.route('/', methods=['GET', 'POST'])
def index():
    precio = None
    error = None

    if request.method == 'POST':
        try:
            # Verificar que el modelo esté cargado
            if modelo is None:
                error = "Error: El modelo no está disponible. Por favor, contacte al administrador."
                return render_template('index.html', precio=precio, error=error)
            
            # Recoger datos del formulario
            marca = request.form.get('marca', '').strip()
            modelo_nombre = request.form.get('modelo', '').strip()
            combustible = request.form.get('combustible', '')
            transmision = request.form.get('transmision', '')
            kilometraje = request.form.get('kilometraje', '')
            anio = request.form.get('anio', '')
            
            # Validar datos
            errores = validar_datos(marca, modelo_nombre, combustible, transmision, kilometraje, anio)
            
            if errores:
                error = ". ".join(errores)
                return render_template('index.html', precio=precio, error=error)
            
            # Preparar datos para el modelo
            datos = {
                'Brand': marca,
                'model': modelo_nombre,
                'FuelType': combustible,
                'Transmission': transmision,
                'kmDriven': float(kilometraje),
                'Year': int(anio)
            }

            # Crear DataFrame para el modelo
            df = pd.DataFrame([datos])

            # Predicción en rupias
            precio_rupias = modelo.predict(df)[0]
            
            # Validar que la predicción sea razonable
            if precio_rupias < 0:
                error = "Error: El modelo generó una predicción inválida. Por favor, verifique los datos ingresados."
                return render_template('index.html', precio=precio, error=error)

            # Conversión a euros
            precio = precio_rupias / INR_POR_EURO
            
            app.logger.info(f"Predicción realizada: {precio:.2f} € para {marca} {modelo_nombre}")
            
        except KeyError as e:
            error = f"Error: Falta el campo {str(e)} en el formulario"
            app.logger.error(f"Error de validación: {str(e)}")
        except Exception as e:
            error = f"Error al procesar la predicción: {str(e)}"
            app.logger.error(f"Error en la predicción: {str(e)}")

    return render_template('index.html', precio=precio, error=error)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
