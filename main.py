import geopandas as gpd


from utils.nw_input_data_prep import prep_ai_leaning_dataset


INPUT = gpd.read_file('.inputs/in_out_geojson/in_2022.geojson')
def main():
    # 1. przygotowuje dane do uczenia - dane muszą obsługiwać współrzędne x,y
    prep_ai_leaning_dataset(input=INPUT)




if __name__ == "__main__":
    main()
