import pandas as pd
import datetime

def extract_data():
    """Extrae datos de un archivo CSV (tiene que estar en una URL)"""
    try:
        url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
        data = pd.read_csv(url)
        print("Datos extraidos correctamente.")
        return data
    except Exception as e:
        print(f"Error durante la extracción: {e}")
        return None
    
def transform_data(data):
    """Transforma los datos para su análisis"""
    try:
        #Quitar columnas sin valores
        data = data.dropna()
        print("Datos transformados correctamente.")
        return data
    except Exception as e:
        print(f"Error durante la transformación: {e}")
        return None
    
def load_data(data):
    """Carga los datos transformados a un archivo CSV local"""
    try:
        data.to_csv("covid19_confirmed_global_transformed_"+datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+".csv", index=False)
        print("Datos cargados correctamente.")
    except Exception as e:
        print(f"Error durante la carga: {e}")

data = extract_data()
print(data.head())