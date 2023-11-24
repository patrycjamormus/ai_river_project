from math import cos, sin, radians
# import pandas as pd
import geopandas as gpd
from utils.vectors import generator_gwiazki

EPSG = 'epsg:2178'  # układ 1992
RADIUS = 300
# 5863838.87, 7527541.11
STARTING_POINT = {"x": 7527541.11, "y": 5863838.87}
# generator_gwiazki(STARTING_POINT=STARTING_POINT, epsg=EPSG , star_radius=RADIUS)

# intersekcja żeby zebrać dane przecięcia jednej i drugiej warstwy
linia_brzegu_2013 = gpd.read_file('sh_in_2013.geojson')
gwiazdka = gpd.read_file('lines.geojson')

# print(gwiazdka)
# print (linia_brzegu_2013.head())

punkty_przeciecia = gwiazdka.unary_union.intersection(linia_brzegu_2013.to_crs(crs=EPSG).unary_union)
punkty_przeciecia.to_file(filename='punkty_przeciecia_2013.geojson', driver="GeoJSON")