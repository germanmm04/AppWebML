from flask import Flask, render_template, request
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Cargar modelo entrenado (usar ruta compatible con Linux/Windows)
ruta_modelo = os.path.join('modelos', 'randomforest_vehiculos.pkl')
modelo = joblib.load(ruta_modelo)

# Tasa fija de conversión (rupias -> euros)
# [No verificado] Tasa fija usada únicamente con fines académicos
INR_POR_EURO = 90

@app.route('/', methods=['GET', 'POST'])
def index():
    precio = None

    if request.method == 'POST':
        # Recoger datos del formulario
        datos = {
            'Brand': request.form['marca'],
            'model': request.form['modelo'],
            'FuelType': request.form['combustible'],
            'Transmission': request.form['transmision'],
            'kmDriven': float(request.form['kilometraje']),
            'Year': int(request.form['anio'])
        }

        # Crear DataFrame para el modelo
        df = pd.DataFrame([datos])

        # Predicción en rupias
        precio_rupias = modelo.predict(df)[0]

        # Conversión a euros
        precio = precio_rupias / INR_POR_EURO

    return render_template('index.html', precio=precio)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
