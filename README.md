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
- El script imprime información por consola.

Notas y supuestos
------------------
- El script descarga los datos desde una URL pública de GitHub (CSSE COVID-19 time series). Requiere conexión a internet.

Contacto
--------
hnaguilera0310@gmail.com

