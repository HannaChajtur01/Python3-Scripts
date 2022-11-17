import csv
import json

# Este script debe ser ejecutado dentro de la carpeta donde está el CSV que se desea convertir a JSON

# Insertar el nombre del archivo CSV
with open("name.csv", "r") as f:
    reader = csv.reader(f)

    data = []
    for row in reader:
        # Actualiza las variables de data.append con los nombres de las columnas del archivo CSV a convertir a JSON
        data.append({'name':row[0], 'description':row[1], 'page_title':row[2], 'meta_description':row[3], 'Image Src':row[4]})
        print(data)

with open("name.json", "w") as f:
    json.dump(data, f, indent=4)