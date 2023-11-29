# general
import geopandas as gpd
from shapely import Point
# custom
from utils.vectors import intersekcja, generator_gwiazki

# CONST
EPSG: str = 'epsg:2178'  # epsg code
RADIUS: int = 300  # meters
STARTING_POINT: Point = Point(7527541.11, 5863838.87)  # case study area

# STAR DRAWING
generator_gwiazki(start_point=STARTING_POINT, epsg=EPSG, star_radius=RADIUS)

# DATA PREPARING
gwiazdka: gpd.GeoDataFrame = gpd.read_file('lines.geojson')

linie_brzegu: list[dict, dict] = [
    {'rok': 2013, 'linia_brzegu': gpd.read_file('data/sh_in_2013.geojson')},
    # TODO dodać nowe dane wg. powyższego wzoru
]

for item in linie_brzegu:
    # dodaje nowa kolumne do tabeli gwiazdka
    gwiazdka[f'distance_{item["rok"]}']: list = intersekcja(
        linia_brzegu=item["linia_brzegu"],
        gwiazdka=gwiazdka,
        starting_point=STARTING_POINT,
        epsg=EPSG
    )

gwiazdka.to_file('nowa_gwiazdka.geojson', driver='GeoJSON')
