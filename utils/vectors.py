from math import cos, sin, radians
import geopandas as gpd


def generator_gwiazki(STARTING_POINT: dict, epsg: int, star_radius: int = 100) -> None:
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
    print(gdf.crs)
    print(gdf.head)
    gdf.to_file(filename='lines.geojson', driver="GeoJSON")
    print('zrobione')
