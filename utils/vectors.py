# general
import geopandas as gpd
import numpy as np
from math import cos, sin, radians
from shapely.geometry import Point, LineString


def calculate_coord(starting_point: Point, angle: float, radius: int) -> Point:
    x = starting_point.x + sin(radians(angle)) * radius
    y = starting_point.y + cos(radians(angle)) * radius
    return Point(x, y)


def generator_gwiazdki(start_point: Point, epsg: str, star_radius: int = 100) -> None:
    """
    draws a star and as a result and saves it on disc as geojson file
    """
    coordinates: list[LineString] = [
        LineString([
            start_point,
            calculate_coord(starting_point=start_point, angle=no, radius=star_radius)
        ]) for no in np.arange(start=0, stop=360, step=1)]

    gdf = gpd.GeoDataFrame(geometry=gpd.GeoSeries(coordinates))
    gdf = gdf.set_crs(epsg, allow_override=True)
    gdf.to_file(filename='lines.geojson', driver="GeoJSON")


def intersekcja(linia_brzegu: gpd.GeoDataFrame, gwiazdka: gpd.GeoDataFrame, starting_point: Point, epsg: str)-> list :
    """
    calculate list with distances from starting point to intersecting point
    :param linia_brzegu: geopandas geodataframe  - jest okodowana transformacja jednak lepiej żeby dane były w 2178
    :param gwiazdka: geopandas geodataframe
    :param starting_point: dict
    :param epsg: str
    :return: list
    """
    linia_brzegu.to_crs(crs=epsg, inplace=True)
    columns_data: list = []
    line_geometry = linia_brzegu.iloc[0].geometry #wyciaganie wspolrzednych


    for gw_row in gwiazdka.itertuples():
        point_of_intersect = gw_row.geometry.intersection(line_geometry)
        dist = point_of_intersect.distance(starting_point)
        columns_data.append(dist)
    return columns_data
