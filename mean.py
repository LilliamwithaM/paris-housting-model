import pandas as pd

# Reemplaza 'tu_archivo.csv' con la ubicación de tu archivo CSV
archivo_csv = 'data/paris-housing.csv'

# Reemplaza 'nombre_de_la_columna' con el nombre de la columna de la que deseas calcular el promedio
nombre_columna = 'price_r'

# Carga el archivo CSV en un DataFrame de pandas
df = pd.read_csv(archivo_csv)

# Verifica si la columna especificada existe en el DataFrame
if nombre_columna in df.columns:
    # Calcula el promedio de los datos en la columna
    promedio = df[nombre_columna].mean()
    print(f'El promedio de la columna {nombre_columna} es: {promedio}')
else:
    print(f'La columna {nombre_columna} no se encontró en el archivo CSV.')

# Puedes agregar manejo de excepciones para lidiar con posibles errores al leer el archivo CSV