import geopandas as gpd
import os

geojson_file = '/Users/carson.elmpicard/Downloads/Census_Towns_Boundaries_2020.geojson'
gdf = gpd.read_file(geojson_file)

output_dir = '/Users/carson.elmpicard/Downloads/GeoJSON_files'
os.makedirs(output_dir, exist_ok=True)

for index, row in gdf.iterrows():
    town_value = row['TOWN20']
    
    output_geojson_path = os.path.join(output_dir, f'{town_value}.geojson')
    
    single_entry_gdf = gpd.GeoDataFrame([row], crs=gdf.crs)
    
    single_entry_gdf.to_file(output_geojson_path, driver='GeoJSON')
    
    print(f'Exported {output_geojson_path}')

print('GeoJSON export complete.')
