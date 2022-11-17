import pandas as pd
import wget

# Este script tiene que ser ejecutado dentro de la misma dirección donde se encuentra el archivo CSV
# Insertar nombre del archivo CSV
data = pd.read_csv("name.csv")

for index, row in data.iterrows():
    # Actualiza la variable de row[''] con el nombre de la columna que contiene los enlaces a descargar
    link = wget.download(row['image_url'])

# Como ejeutar este script:
# 1. Instala Python3
# 2. python3 install pandas
# 3. python3 install wget
# 4. python3 downloadimagesFromCSV.py