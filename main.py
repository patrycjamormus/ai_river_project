# general
import geopandas as gpd

# custom
from utils.vectors import intersekcja  # generator_gwiazki,

# CONST
EPSG = 'epsg:2178'
RADIUS = 300
STARTING_POINT = {"x": 7527541.11, "y": 5863838.87}

# STAR DRAWING
# generator_gwiazki(STARTING_POINT=STARTING_POINT, epsg=EPSG , star_radius=RADIUS)

# DATA PREPARING
gwiazdka = gpd.read_file('lines.geojson')

linie_brzegu: list[dict, dict] = [
    {'rok': 2013, 'linia_brzegu': gpd.read_file('data/sh_in_2013.geojson')},
    # TODO dodać nowe dane wg. powyższego wzoru
]

for item in linie_brzegu:
    gwiazdka[f'distance_{item.rok}']: list = intersekcja(
        linia_brzegu=item.linia_brzegu,
        gwiazdka=gwiazdka,
        STARTING_POINT=STARTING_POINT,
        EPSG=EPSG
    )

gwiazdka.to_file('nowa_gwiazdka.geojson', driver='GeoJSON')
