import duckdb

con = duckdb.connect()
sql = """
  COPY (
    SELECT
      categoria,
      SUM(precio * cantidad)    AS total_ventas,
      AVG(precio)               AS precio_promedio
    FROM 'data/datos.csv'
    WHERE cantidad > 0
    GROUP BY categoria
  ) TO 'resumen_duckdb.csv' (HEADER, DELIMITER ',');
"""
con.execute(sql)
print("Resumen DuckDB guardado.")