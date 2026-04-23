#!/bin/bash

bash 1_descarga_omega.sh

echo "Creando base de datos..."
python3 2_crear_db.py

echo "Haciendo el análisis de los datos y generando diagrama HR..."
python3 3_analisis.py

echo "Se ha terminado el proceso"
