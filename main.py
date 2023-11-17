from math import cos, sin, radians
# import pandas as pd
import geopandas as gpd

results = []

STARTING_POINT = {"x": 0, "y": 0}


def calculate_coord(st_point: dict, angle: float, radius: float = 100) -> dict:
    x = st_point["x"] + sin(radians(angle)) * radius
    y = st_point["y"] + cos(radians(angle)) * radius
    return {"x": x, "y": y}

# data basic structure


for no in range(361):
    point = calculate_coord(st_point=STARTING_POINT, angle=no)
    item = {
        "id": no,
        "azimuth": no,
        "Coordinates": f'LINESTRING('
                       f'{STARTING_POINT["x"]} '
                       f'{STARTING_POINT["y"]}, '
                       f'{point["x"]} {point["y"]})',
        "year": 2020
    }
    results.append(item)

coordinates: list = [item['Coordinates'] for item in results]
gdf = gpd.GeoDataFrame(geometry=gpd.GeoSeries.from_wkt(coordinates))
gdf.to_file(filename='lines.geojson', driver="GeoJSON")

print(gdf)
