import geopandas as gpd

dane_: gpd.geodataframe = gpd.read_file('in_2011.geojson')
# dane_['rok'] = 2011