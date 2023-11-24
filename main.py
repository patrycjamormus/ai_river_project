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

linie_brzegu = [
    gpd.read_file('data/sh_in_2013.geojson'),
    # TODO dodać nowe lata
]

for idx, linia_brzegu in enumerate(linie_brzegu):
    gwiazdka[f'distance_{idx}']: list = intersekcja(
        linia_brzegu=linia_brzegu,
        gwiazdka=gwiazdka,
        STARTING_POINT=STARTING_POINT,
        EPSG=EPSG
    )

gwiazdka.to_file('nowa_gwiazdka.geojson', driver='GeoJSON')
