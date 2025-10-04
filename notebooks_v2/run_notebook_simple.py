import papermill as pm
from datetime import datetime

# Modificar Parámetro
# Poner el país en inglés 
country = "Brazil"

# Timestamp para versionado (YYYYMMDD_HHMMSS)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Ruta del notebook de salida
output_path = f"notebooks_v2/output/covid_{country}_{timestamp}.ipynb"

# Ejecutar notebook
pm.execute_notebook(
    input_path="notebooks_v2/notebook_simple.ipynb",
    output_path=output_path,
    parameters={"country": country},
)

print(f"Ejecucion ok, notebook guardado en: {output_path}")
