import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Conexión
con = sqlite3.connect('arqueologia.db')
df = pd.read_sql("SELECT * FROM estrellas", con)

# Grafica de movimiento Propio
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(df['pmRA'], df['pmDE'], s=0.1, color='indigo',alpha=0.5)
plt.title("Identificando el Cúmulo")
plt.xlim(-10,4)
plt.ylim(-12,2)
plt.xlabel("pmRA (mas/yr)")
plt.ylabel("pmDE (mas/yr)")
plt.grid()

# Definimos los límites
pmRA_min, pmRA_max = -6, 0
pmDE_min, pmDE_max = -9, -4.5

# Aplicamos el filtro
df_cluster = df[
    (df['pmRA'] >= pmRA_min) & (df['pmRA'] <= pmRA_max) & 
    (df['pmDE'] >= pmDE_min) & (df['pmDE'] <= pmDE_max)
]

print(f"Estrellas totales: {len(df)}")
print(f"Estrellas en el cúmulo tras el filtro: {len(df_cluster)}")

# Diagrama color-magnitud
plt.subplot(1, 2, 2)

# Graficamostodas las estrellas de fondo en rojo
color_all = df['BPmag'] - df['RPmag']
plt.scatter(color_all, df['Gmag'], s=0.1, color='red', alpha=0.2, label='Estrellas de campo')

# Graficamos SOLO el cúmulo en azul encima
color_cluster = df_cluster['BPmag'] - df_cluster['RPmag']
plt.scatter(color_cluster, df_cluster['Gmag'], s=0.2, color='blue', alpha=0.6, label='Omega Centauri')

plt.gca().invert_yaxis() 
plt.title("Diagrama color-magnitud de Omega Centauri")
plt.xlabel("Índice de Color (BP - RP)")
plt.ylabel("Magnitud G")
plt.xlim(-0.5, 2.0)
plt.legend(markerscale=10)
plt.grid()
plt.savefig("analisis_final.png")
plt.show()
