import pandas as pd

df = pd.read_csv("data/datos.csv", sep=None, engine="python", encoding="latin1")
print("Filas y columnas:", df.shape)
print(df.info())
print("Nulos por columna:\n", df.isna().sum())

# Columnas derivadas y limpieza
df["total"] = df["precio"] * df["cantidad"]
df["fecha"] = pd.to_datetime(df["fecha"])
df["cliente"] = df["cliente"].str.strip().str.title()
df["descuento"] = df["descuento"].fillna(0)

# Agrupaciones y exportación
resumen = (
    df.query("cantidad > 0")
      .groupby("categoria")
      .agg(total_ventas=("total", "sum"),
           precio_promedio=("precio", "mean"))
      .reset_index()
)
resumen.to_csv("resumen_pandas.csv", index=False)
print("Resumen pandas guardado.")