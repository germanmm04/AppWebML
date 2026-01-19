# Importar librerías
import joblib
import pandas as pd
from keras.src.losses import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("../coches.csv")

# Supongamos que tus datos están en un DataFrame llamado df
# Variables predictoras
categorical_features = ['Brand', 'model', 'FuelType', 'Transmission']
numeric_features = ['kmDriven', 'Year']

# Variable objetivo
target = 'AskPrice'

# Separar datos en X e y
X = df[categorical_features + numeric_features]
y = df[target]

# Dividir en entrenamiento y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocesamiento para variables categóricas y numéricas
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features),
        ('num', StandardScaler(), numeric_features)
    ])

# Crear pipeline con preprocesamiento y regresión lineal
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Entrenar el modelo
pipeline.fit(X_train, y_train)

# Guardar el pipeline completo (incluye preprocesamiento y regresor)
joblib.dump(pipeline, '../modelos/RegresionLineal_coches.pkl')

print("Modelo exportado correctamente.")

# Hacer predicciones
y_pred = pipeline.predict(X_test)

# Evaluar el modelo
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

