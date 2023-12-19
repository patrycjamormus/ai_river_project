# general
import pandas as pd
import geopandas as gpd
from shapely import Point
# custom
from utils.vectors import intersekcja, generator_gwiazdki

# CONST
EPSG: str = 'EPSG:2178'  # epsg code
RADIUS: int = 300  # meters
STARTING_POINT: Point = Point(7527541.11, 5863838.87)  # case study area

# STAR DRAWING
generator_gwiazdki(start_point=STARTING_POINT, epsg=EPSG, star_radius=RADIUS)

# DATA PREPARING
gwiazdka: gpd.GeoDataFrame = gpd.read_file('lines.geojson')

linie_brzegu: list[dict, dict] = [
    {'rok': 2011, 'shoreline': 'in', 'linia_brzegu': gpd.read_file('data/in_2011.geojson')},
    {'rok': 2011, 'shoreline': 'out', 'linia_brzegu': gpd.read_file('data/out_2011.geojson')},
    {'rok': 2013, 'shoreline': 'in', 'linia_brzegu': gpd.read_file('data/in_2013.geojson')},
    {'rok': 2013, 'shoreline': 'out', 'linia_brzegu': gpd.read_file('data/out_2013.geojson')},
    {'rok': 2016, 'shoreline': 'in', 'linia_brzegu': gpd.read_file('data/in_2016.geojson')},
    {'rok': 2016, 'shoreline': 'out', 'linia_brzegu': gpd.read_file('data/out_2016.geojson')},
    {'rok': 2019, 'shoreline': 'in', 'linia_brzegu': gpd.read_file('data/in_2019.geojson')},
    {'rok': 2019, 'shoreline': 'out', 'linia_brzegu': gpd.read_file('data/out_2019.geojson')},
    {'rok': 2020, 'shoreline': 'in', 'linia_brzegu': gpd.read_file('data/in_2020.geojson')},
    {'rok': 2020, 'shoreline': 'out', 'linia_brzegu': gpd.read_file('data/out_2020.geojson')},
    {'rok': 2022, 'shoreline': 'in', 'linia_brzegu': gpd.read_file('data/in_2022.geojson')},
    {'rok': 2022, 'shoreline': 'out', 'linia_brzegu': gpd.read_file('data/out_2022.geojson')},
]

lista_df_na_kolejne_lata: list = []

for item in linie_brzegu:
    # dodaje nowa kolumne do tabeli gwiazdka
    # print(item)
    df_n= gwiazdka.copy()
    df_n ['rok'] = item['rok']
    df_n ['in'] = True if item ['shoreline'] == 'in' else False
    df_n[f'distance']: list = intersekcja(
        linia_brzegu=item["linia_brzegu"],
        gwiazdka=gwiazdka,
        starting_point=STARTING_POINT,
        epsg=EPSG
    )
    df_n ['angle'] =df_n.index
    lista_df_na_kolejne_lata.append(df_n)


df_full = pd.concat(lista_df_na_kolejne_lata)
print(df_full)
df_full.to_file('nowa_gwiazdka.geojson', driver='GeoJSON')

