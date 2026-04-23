import pandas as pd
import sqlite3

# Leyendo csv
df = pd.read_csv("omega_bruto.csv")

# Limpiando csv
cols = ['pmRA', 'pmDE', 'Gmag', 'RPmag','BPmag']
df_limpio = df.dropna(subset=cols)

# Conexión a SQL
con = sqlite3.connect('arqueologia.db') 

df_limpio.to_sql('estrellas', con, if_exists='replace', index=False)

con.close()

