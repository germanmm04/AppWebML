# App Web ML - Predicción de Precio de Vehículos

Aplicación web Flask para predecir el precio de vehículos usando Machine Learning.

## 🚀 Despliegue en Render (Recomendado)

### Pasos para desplegar:

1. **Crear cuenta en Render**
   - Ve a [render.com](https://render.com)
   - Regístrate con tu cuenta de GitHub (recomendado)

2. **Subir el proyecto a GitHub**
   - Si no tienes un repositorio, créalo en GitHub
   - Sube todos los archivos del proyecto:
     ```bash
     git init
     git add .
     git commit -m "Initial commit"
     git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
     git push -u origin main
     ```

3. **Desplegar en Render**
   - En Render, haz clic en "New +" → "Web Service"
   - Conecta tu repositorio de GitHub
   - Configuración:
     - **Name**: `app-web-ml` (o el nombre que prefieras)
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn main:app`
     - **Plan**: Selecciona "Free" (plan gratuito)
   - Haz clic en "Create Web Service"

4. **Esperar el despliegue**
   - Render construirá y desplegará tu aplicación automáticamente
   - Una vez completado, obtendrás una URL como: `https://app-web-ml.onrender.com`

## 📋 Requisitos

- Python 3.8+
- Flask
- scikit-learn
- pandas
- joblib

## 🏃 Ejecutar localmente

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python main.py
```

La aplicación estará disponible en `http://localhost:5000`

## 📁 Estructura del proyecto

```
AppWebML/
├── main.py                 # Aplicación Flask principal
├── requirements.txt        # Dependencias Python
├── Procfile               # Configuración para Render
├── modelos/               # Modelos de ML entrenados
│   └── randomforest_vehiculos.pkl
├── templates/             # Plantillas HTML
│   └── index.html
└── static/               # Archivos estáticos (CSS)
    └── style.css
```

## 🔧 Alternativas de despliegue

### Railway
1. Ve a [railway.app](https://railway.app)
2. Conecta tu repositorio de GitHub
3. Railway detectará automáticamente que es una app Python
4. Despliega automáticamente

### Fly.io
1. Instala Fly CLI: `curl -L https://fly.io/install.sh | sh`
2. Ejecuta: `fly launch`
3. Sigue las instrucciones

### PythonAnywhere
1. Ve a [pythonanywhere.com](https://www.pythonanywhere.com)
2. Crea una cuenta gratuita
3. Sube tus archivos vía web o Git
4. Configura el WSGI file

## ⚠️ Notas importantes

- El plan gratuito de Render puede tener tiempos de inicio lentos (hasta 50 segundos)
- Los servicios gratuitos pueden "dormir" después de inactividad
- Asegúrate de que todos los archivos `.pkl` estén incluidos en el repositorio
