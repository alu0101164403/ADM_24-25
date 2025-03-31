import pandas as pd
from datasource import CSVDataSource
from cleaner import GenericCleaner
from visualizer import Visualizer
from strategies import BarChartStrategy, LineChartStrategy

# 1. Cargar y limpiar datos
source = CSVDataSource("US_Accidents_March23.csv")
df = source.get_dataframe()

cleaner = GenericCleaner(
    cols_to_drop=[
        'Description', 'Start_Lat', 'Start_Lng', 'End_Lat', 'End_Lng',
        'Source', 'Country', 'Distance(mi)', 'Airport_Code', 'Weather_Timestamp',
        'Timezone', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight'
    ],
    cols_required=['Street', 'City', 'Zipcode', 'Sunrise_Sunset'],
    cols_fill_mean=[
        'Temperature(F)', 'Wind_Chill(F)', 'Precipitation(in)', 'Wind_Speed(mph)',
        'Visibility(mi)', 'Pressure(in)', 'Humidity(%)'
    ],
    cols_fill_mode=['Weather_Condition', 'Wind_Direction']
)
df = cleaner.clean(df)

# 2. Procesar fecha y hora
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
df = df.dropna(subset=['Start_Time'])  # Eliminar fechas no válidas
df['Hour'] = df['Start_Time'].dt.hour

# 3. Visualizador
viz = Visualizer()

# A. BARRAS: Accidentes por condición meteorológica (Weather_Condition)
viz.set_strategy(BarChartStrategy(x='Weather_Condition', top_n=15))
viz.render(df)

# B. LÍNEAS: Evolución del número de accidentes por hora del día
accidents_per_hour = df['Hour'].value_counts().sort_index()
df_hourly = pd.DataFrame({'Hour': accidents_per_hour.index, 'Accidents': accidents_per_hour.values})

viz.set_strategy(LineChartStrategy(x='Hour', y='Accidents'))
viz.render(df_hourly)
