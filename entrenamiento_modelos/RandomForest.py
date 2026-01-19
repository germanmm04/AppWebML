# Importar librerías
from keras.src.losses import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import joblib

df = pd.read_csv("../coches.csv")

# Variables categóricas y numéricas

categorical_features = ['Brand', 'model', 'FuelType', 'Transmission']
numeric_features = ['kmDriven', 'Year']

# Variable objetivo
target = 'AskPrice'

# Separar datos
X = df[categorical_features + numeric_features]
y = df[target]

# Dividir en entrenamiento y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocesamiento
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features),
        ('num', 'passthrough', numeric_features)  # Random Forest no necesita escalado
    ])

# Pipeline con Random Forest
pipeline_rf = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Entrenar el modelo
pipeline_rf.fit(X_train, y_train)

# Hacer predicciones
y_pred = pipeline_rf.predict(X_test)

# Evaluar el modelo
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae:.2f}")
print(f"R^2 Score: {r2:.2f}")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

# Exportar el modelo
joblib.dump(pipeline_rf, '../modelos/randomforest_vehiculos.pkl')
print("Modelo Random Forest exportado correctamente.")
