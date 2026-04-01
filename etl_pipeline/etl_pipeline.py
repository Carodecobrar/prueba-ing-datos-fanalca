import pandas as pd
import datetime

def extract_data():
    """Extrae datos de un archivo CSV (tiene que estar en una URL)"""
    try:
        url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
        data = pd.read_csv(url)
        print("---------------------------Datos extraidos correctamente---------------------------")
        return data
    except Exception as e:
        print(f"Error durante la extracción: {e}")
        return None
    
def transform_data(data):
    """Transforma los datos para su análisis"""
    try:
        #Columnas fijas
        fixed_columns = ['Province/State', 'Country/Region', 'Lat', 'Long']
        #Columnas de fechas
        date_columns = [col for col in data.columns if col not in fixed_columns]
        #Agrupacion
        dataframe_agrupado = data.melt(
            id_vars=fixed_columns,
            value_vars=date_columns,
            var_name='Date',
            value_name='Confirmed'
        )
        #Formato de fechas
        dataframe_agrupado['Date'] = pd.to_datetime(dataframe_agrupado['Date'])
        #Nuevas columnas
        dataframe_agrupado['Month'] = dataframe_agrupado['Date'].dt.month
        dataframe_agrupado['Day'] = dataframe_agrupado['Date'].dt.day
        #Ordenamiento descendente
        dataframe_agrupado = dataframe_agrupado.sort_values(by=['Country/Region', 'Date'], ascending=False)
        print("---------------------------Datos transformados correctamente---------------------------")
        return dataframe_agrupado
    except Exception as e:
        print(f"Error durante la transformación: {e}")
        return None
    
def load_data(data):
    """Carga los datos transformados a un archivo CSV local"""
    try:
        data.to_csv("covid19_confirmed_global_transformed_"+datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+".csv", index=False)
        print("---------------------------Datos cargados correctamente---------------------------")
    except Exception as e:
        print(f"Error durante la carga: {e}")

data = extract_data()
print(data.head())
print(transform_data(data).head())