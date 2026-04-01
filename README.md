# ETL Pipeline - prueba-ing-datos-fanalca

Descripción
-----------
Es un ETL Pipeline que procesa datos de un CSV y los muestra en consola.

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```powershell
python -m pip install --upgrade pip; python -m pip install -r requirements.txt
```

Cómo ejecutar
-------------
Desde la raíz del repositorio (o desde el directorio `etl_pipeline`):

```powershell
python .\etl_pipeline\etl_pipeline.py
```

Salida
------
- El script imprime información por consola (progreso) y genera un archivo CSV llamado `covid19_confirmed_global_transformed_YYYY-MM-DD_HH-MM-SS.csv` en el directorio de trabajo.

Notas y supuestos
------------------
- El script descarga los datos desde una URL pública de GitHub (CSSE COVID-19 time series). Requiere conexión a internet.
- Solo se detectó la dependencia `pandas` en el código; si añade más librerías, actualice `requirements.txt`.

Contacto
--------
hnaguilera0310@gmail.com

