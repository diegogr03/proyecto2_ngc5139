#!/bin/bash

echo "Descargando datos de Omega Centauri desde Vizier..."

# Coordenadas: 201.6965, -47.4795; Radio: 0.5 grados
QUERY="SELECT Source, RA_ICRS, DE_ICRS, pmRA, pmDE, Gmag, BPmag, RPmag 
FROM \"I/355/gaiadr3\"
WHERE CONTAINS(POINT('ICRS', RA_ICRS, DE_ICRS), CIRCLE('ICRS', 201.6965, -47.4795, 0.5))=1"

wget -O omega_bruto.csv "http://tapvizier.u-strasbg.fr/TAPVizieR/tap/sync?request=doQuery&lang=ADQL&format=csv&query=$QUERY"

echo "Archivo omega_bruto.csv generado."
