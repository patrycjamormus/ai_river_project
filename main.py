# general
import geopandas as gpd
from shapely import Point
# custom
from utils.vectors import intersekcja, generator_gwiazki

# CONST
EPSG: str = 'EPSG:2178'  # epsg code
RADIUS: int = 300  # meters
STARTING_POINT: Point = Point(7527541.11, 5863838.87)  # case study area

# STAR DRAWING
generator_gwiazki(start_point=STARTING_POINT, epsg=EPSG, star_radius=RADIUS)

# DATA PREPARING
gwiazdka: gpd.GeoDataFrame = gpd.read_file('lines.geojson')

linie_brzegu: list[dict, dict] = [
    {'rok': 2011, 'shoreline': 'inside', 'linia_brzegu': gpd.read_file('data/in_2011.geojson')},
    {'rok': 2011, 'shoreline': 'outside', 'linia_brzegu': gpd.read_file('data/out_2011.geojson')},
    {'rok': 2013, 'shoreline': 'inside', 'linia_brzegu': gpd.read_file('data/in_2013.geojson')},
    # {'rok': 2013, 'shoreline': 'outside', 'linia_brzegu': gpd.read_file('data/out_2013.geojson')},
    # {'rok': 2016, 'shoreline': 'inside', 'linia_brzegu': gpd.read_file('data/in_2016.geojson')},
    # {'rok': 2016, 'shoreline': 'outside', 'linia_brzegu': gpd.read_file('data/out_2016.geojson')},
    # {'rok': 2019, 'shoreline': 'inside', 'linia_brzegu': gpd.read_file('data/in_2019.geojson')},
    # {'rok': 2019, 'shoreline': 'outside', 'linia_brzegu': gpd.read_file('data/out_2019.geojson')},
    # {'rok': 2020, 'shoreline': 'inside', 'linia_brzegu': gpd.read_file('data/in_2020.geojson')},
    # {'rok': 2020, 'shoreline': 'outside', 'linia_brzegu': gpd.read_file('data/out_2020.geojson')},
    # {'rok': 2022, 'shoreline': 'inside', 'linia_brzegu': gpd.read_file('data/in_2022.geojson')},
    # {'rok': 2022, 'shoreline': 'outside', 'linia_brzegu': gpd.read_file('data/out_2022.geojson')},
]

for item in linie_brzegu:
    # dodaje nowa kolumne do tabeli gwiazdka
    # print(item)
    gwiazdka[f'distance_{item["rok"]}']: list = intersekcja(
        linia_brzegu=item["linia_brzegu"],
        gwiazdka=gwiazdka,
        starting_point=STARTING_POINT,
        epsg=EPSG
    )

gwiazdka.to_file('nowa_gwiazdka.geojson', driver='GeoJSON')
