from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from joblib import dump
import pandas as pd
import pathlib

df = pd.read_csv(pathlib.Path('data/paris-housing.csv'))
y = df['price_r']
X = df.drop('price_r', axis=1)  # Elimina la columna 'numberOfRooms'
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print('Training model..')
regressor = RandomForestRegressor(n_estimators=10, max_depth=1, random_state=0)
regressor.fit(X_train, y_train)
print('Model trained.')

# Evaluar el modelo (por ejemplo, con el error cuadrático medio)
y_pred = regressor.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Guardar el modelo entrenado
print('Saving model..')
dump(regressor, pathlib.Path('model/paris-housing-v1.joblib'))
