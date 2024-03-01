import geopandas as gpd
from shapely.geometry import Point

def prep_ai_leaning_dataset(input:gpd.GeoDataFrame)->gpd.GeoDataFrame:
    point_list: gpd.GeoDataFrame = input.explode(ignore_index=True)
    point_list.to_file('./.outputs/data_model_xy.geojson', driver='GeoJSON')
    return point_list.get_coordinates().reset_index()



