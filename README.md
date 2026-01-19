# App Web ML - Predicción de Precio de Vehículos

Aplicación web completa para predecir el precio de vehículos usando Machine Learning. El proyecto incluye entrenamiento de modelos, evaluación con validación cruzada, ajuste de hiperparámetros y una interfaz web interactiva.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación](#instalación)
- [Uso](#uso)
- [Entrenamiento de Modelos](#entrenamiento-de-modelos)
- [Despliegue en la Nube](#despliegue-en-la-nube)
- [Documentación Técnica](#documentación-técnica)

## ✨ Características

### Backend
- ✅ Carga del modelo entrenado (Random Forest)
- ✅ Recepción de datos desde formulario web
- ✅ Validación completa de entradas (backend y frontend)
- ✅ Manejo robusto de errores
- ✅ Predicción del precio con conversión a euros
- ✅ Logging para debugging

### Frontend
- ✅ Formulario intuitivo y responsive
- ✅ Validación en tiempo real con JavaScript
- ✅ Mensajes de error claros y específicos
- ✅ Indicador de carga durante el procesamiento
- ✅ Visualización clara del precio estimado
- ✅ Diseño moderno y profesional

### Modelos de Machine Learning
- ✅ Regresión Lineal con validación cruzada
- ✅ Random Forest con GridSearch (hiperparámetros optimizados)
- ✅ Gradient Boosting con RandomSearch
- ✅ Comparación exhaustiva de modelos
- ✅ Visualizaciones de errores reales vs predichos
- ✅ Gráficas de residuos
- ✅ Métricas completas (MSE, MAE, R²)

## 📁 Estructura del Proyecto

```
AppWebML/
├── main.py                          # Aplicación Flask principal
├── requirements.txt                 # Dependencias Python
├── Procfile                         # Configuración para Render
├── runtime.txt                      # Versión de Python
├── .gitignore                       # Archivos a ignorar en Git
│
├── notebooks/                       # Notebooks de entrenamiento
│   └── entrenamiento_y_evaluacion.ipynb
│
├── modelos/                         # Modelos entrenados (.pkl)
│   └── randomforest_vehiculos.pkl
│
├── entrenamiento_modelos/           # Scripts y resultados de entrenamiento
│   ├── RandomForest.py
│   ├── GradientBoosting.py
│   ├── RegresionLineal.py
│   └── *.png                        # Gráficas generadas
│
├── templates/                       # Plantillas HTML
│   └── index.html
│
└── static/                          # Archivos estáticos
    ├── style.css                    # Estilos CSS
    └── validation.js                # Validación JavaScript
```

## 🛠 Tecnologías Utilizadas

### Backend
- **Flask 2.3.3**: Framework web ligero y flexible
- **scikit-learn 1.3.2**: Machine Learning y preprocesamiento
- **pandas 2.0.3**: Manipulación de datos
- **joblib 1.3.2**: Serialización de modelos
- **numpy 1.24.3**: Operaciones numéricas
- **gunicorn 21.2.0**: Servidor WSGI para producción

### Frontend
- **HTML5**: Estructura semántica
- **CSS3**: Estilos modernos y responsive
- **JavaScript (Vanilla)**: Validación del lado del cliente

### Machine Learning
- **Modelos**: Regresión Lineal, Random Forest, Gradient Boosting
- **Técnicas**: Validación cruzada, GridSearch, RandomSearch
- **Métricas**: MSE, MAE, R² Score
- **Visualización**: matplotlib, seaborn

## 🚀 Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd AppWebML
   ```

2. **Crear un entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # En Windows
   venv\Scripts\activate
   
   # En Linux/Mac
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verificar que el modelo esté presente**
   - Asegúrate de que el archivo `modelos/randomforest_vehiculos.pkl` existe
   - Si no existe, ejecuta el notebook de entrenamiento primero

## 🏃 Uso

### Ejecutar la Aplicación Localmente

```bash
python main.py
```

La aplicación estará disponible en `http://localhost:5000`

### Usar la Aplicación Web

1. Abre tu navegador y ve a `http://localhost:5000`
2. Completa el formulario con los datos del vehículo:
   - **Marca**: Nombre de la marca (ej: Toyota, Honda)
   - **Modelo**: Nombre del modelo (ej: Corolla, Civic)
   - **Tipo de combustible**: Gasolina o Diésel
   - **Tipo de transmisión**: Manual o Automática
   - **Kilometraje**: Número de kilómetros recorridos
   - **Año de fabricación**: Año entre 1900 y 2025
3. Haz clic en "Calcular precio"
4. El precio estimado se mostrará en euros

## 📊 Entrenamiento de Modelos

### Ejecutar el Notebook de Entrenamiento

1. **Abrir Jupyter Notebook**
   ```bash
   jupyter notebook notebooks/entrenamiento_y_evaluacion.ipynb
   ```

2. **Ejecutar todas las celdas**
   - El notebook incluye:
     - Carga y exploración de datos
     - Preprocesamiento
     - Entrenamiento de 3 modelos
     - Validación cruzada
     - GridSearch para Random Forest
     - RandomSearch para Gradient Boosting
     - Comparación de modelos
     - Visualizaciones
     - Guardado del modelo final

3. **Resultados**
   - Los modelos se guardan en `modelos/`
   - Las gráficas se guardan en `entrenamiento_modelos/`

### Modelos Entrenados

- **Regresión Lineal**: Modelo base con validación cruzada
- **Random Forest**: Optimizado con GridSearch (modelo seleccionado)
- **Gradient Boosting**: Optimizado con RandomSearch

### Justificación del Modelo Final

**Random Forest** fue seleccionado como modelo final porque:
- ✅ Buen balance entre rendimiento y velocidad
- ✅ Menor riesgo de overfitting gracias a GridSearch
- ✅ Mejor interpretabilidad que Gradient Boosting
- ✅ Resultados consistentes en validación cruzada
- ✅ Adecuado para producción

## ☁️ Despliegue en la Nube

### Opción 1: Render (Recomendado)

1. **Crear cuenta en Render**
   - Ve a [render.com](https://render.com)
   - Regístrate con tu cuenta de GitHub

2. **Subir el proyecto a GitHub**
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
     - **Name**: `app-web-ml`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install --upgrade pip && pip install -r requirements.txt`
     - **Start Command**: `gunicorn main:app`
     - **Python Version**: `3.11.9` (o deja en blanco para usar runtime.txt)
     - **Plan**: Free
   - Haz clic en "Create Web Service"

4. **Esperar el despliegue**
   - Render construirá y desplegará tu aplicación automáticamente
   - Obtendrás una URL como: `https://app-web-ml.onrender.com`

### Opción 2: Railway

1. Ve a [railway.app](https://railway.app)
2. Conecta tu repositorio de GitHub
3. Railway detectará automáticamente que es una app Python
4. Despliega automáticamente

### Opción 3: PythonAnywhere

1. Ve a [pythonanywhere.com](https://www.pythonanywhere.com)
2. Crea una cuenta gratuita
3. Sube tus archivos vía web o Git
4. Configura el WSGI file

## 📚 Documentación Técnica

### Flujo de la Aplicación

1. **Usuario introduce datos** → Formulario web con validación
2. **Frontend valida** → JavaScript valida antes de enviar
3. **Backend recibe datos** → Flask procesa la petición POST
4. **Backend valida** → Validación adicional en el servidor
5. **Modelo predice** → Random Forest genera predicción
6. **Conversión** → Precio en rupias convertido a euros
7. **Resultado** → Precio estimado mostrado al usuario

### Validación Implementada

#### Frontend (JavaScript)
- Validación en tiempo real al perder foco
- Validación al enviar el formulario
- Mensajes de error específicos por campo
- Prevención de envío con datos inválidos

#### Backend (Python)
- Validación de tipos de datos
- Validación de rangos (año, kilometraje)
- Validación de valores permitidos (combustible, transmisión)
- Manejo de excepciones

### Manejo de Errores

- Errores de validación mostrados al usuario
- Errores del modelo capturados y logueados
- Mensajes de error claros y útiles
- Logging para debugging en producción

## ⚠️ Notas Importantes

- **Plan gratuito de Render**: Puede tener tiempos de inicio lentos (hasta 50 segundos) si la app está inactiva
- **Servicios gratuitos**: Pueden "dormir" después de inactividad
- **Modelo**: Asegúrate de que `modelos/randomforest_vehiculos.pkl` esté incluido en el repositorio
- **Datos**: El modelo fue entrenado con datos en rupias, se convierte a euros para mostrar
- **Tasa de conversión**: Actualmente fija en 90 rupias por euro (fines académicos)

## 🔧 Solución de Problemas

### Error al cargar el modelo
- Verifica que `modelos/randomforest_vehiculos.pkl` existe
- Ejecuta el notebook de entrenamiento si falta

### Error en Render al construir
- Verifica que `requirements.txt` tiene todas las dependencias
- Asegúrate de que el Build Command incluye `pip install --upgrade pip`
- Revisa los logs de Render para más detalles

### La aplicación no responde
- Verifica que el puerto está configurado correctamente
- En producción, asegúrate de usar `gunicorn` como servidor WSGI

## 📝 Licencia

Este proyecto es de uso académico.

## 👤 Autor

Proyecto desarrollado para el curso de Inteligencia Artificial.

---

**¡Gracias por usar App Web ML!** 🚗💻
