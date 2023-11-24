# general
import geopandas as gpd
from math import cos, sin, radians
from shapely.geometry import Point, LineString


def generator_gwiazki(STARTING_POINT: dict, epsg: int, star_radius: int = 100) -> None:
    """
    draws a star and as a result and saves it on disc as geojson file
    """
    results: list = []

    def calculate_coord(st_point: dict, angle: float, radius: int) -> dict:
        x = st_point["x"] + sin(radians(angle)) * radius
        y = st_point["y"] + cos(radians(angle)) * radius
        return {"x": x, "y": y}

    for no in range(361):
        point = calculate_coord(st_point=STARTING_POINT, angle=no, radius=star_radius)
        item = {
            "id": no,
            "azimuth": no,
            "Coordinates":
                f'LINESTRING('
                f'{STARTING_POINT["x"]} '
                f'{STARTING_POINT["y"]}, '
                f'{point["x"]} {point["y"]})',
            "year": 2020
        }
        results.append(item)

    coordinates: list = [item['Coordinates'] for item in results]
    gdf = gpd.GeoDataFrame(geometry=gpd.GeoSeries.from_wkt(coordinates))
    gdf = gdf.set_crs(epsg, allow_override=True)
    gdf.to_file(filename='lines.geojson', driver="GeoJSON")


def intersekcja(linia_brzegu: object, gwiazdka: object, STARTING_POINT: dict, EPSG: str) -> list:
    """
    calculate list with distances from starting point to intersecting point
    :param linia_brzegu: geopandas geodataframe
    :param gwiazdka: geopandas geodataframe
    :param STARTING_POINT: dict
    :param EPSG: str
    :return: list
    """
    linia_brzegu.to_crs(crs=EPSG, inplace=True)
    columns_data: list = []
    for gw_row in gwiazdka.itertuples():
        for ln_row in linia_brzegu.itertuples():
            point_of_intersect = gw_row.geometry.intersection(ln_row.geometry)
            dis = point_of_intersect.distance(
                Point(STARTING_POINT['x'], STARTING_POINT['y'])
            )
            columns_data.append(dis)
    return columns_data
