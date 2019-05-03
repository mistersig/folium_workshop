conda create --name folium -c conda-forge python=3.6 folium fiona jupyter basemap pandas shapely geopandas


import os
import numpy
import folium
import geopandas 
import pd
print('success')



# Convert pd to gpd with geom column
speedPoints = os.path.join('data', 'speed_camera_violations.csv')

speedViolations = pd.read_csv(speedPoints)

# speedViolations = geopandas.GeoDataFrame(
#     speedViolations, geometry=geopandas.points_from_xy(speedViolations.LONGITUDE, speedViolations.LATITUDE))
# speedViolations.crs = {'init' :'epsg:4326'} 
# speedViolations.head(5)


m = folium.Map(
    location=[41.884510, -87.630232],
    tiles='CartoDB positron',
    zoom_start=10
)

locations = speedViolations[['LATITUDE', 'LONGITUDE']]
locationlist = locations.values.tolist()


# marker_cluster = folium.MarkerCluster().add_to(m)

# for point in range(0, len(locationlist)):
#     folium.Marker(locationlist[point], popup=df_counters['Name'][point]).add_to(marker_cluster)
# map2


for point in range(0, len(locationlist)):
    folium.Marker(locationlist[point], 
    popup=speedViolations['CAMERA_ID'][point],
    icon=folium.Icon(color='red', 
    icon_color='#fff', icon='camera', angle=0, prefix='fa')).add_to(marker_cluster)
m














wardGeom = os.path.join('data', 'boundaries.geojson')
wards = geopandas.read_file(wardGeom)
wards

m = folium.Map(
    location=[41.884510, -87.630232],
    tiles='CartoDB positron',
    zoom_start=10
)
folium.GeoJson(wards).add_to(m)
m.save('index.html')
m



runoffData = os.path.join(
    'data', 'runoff_election_turnout.csv'
)
runoff = pd.read_csv(runoffData)
runoff.head(5)



from branca.colormap import linear

colormap = linear.YlGn_09.scale(
    runoff.Turnout.min(),
    runoff.Turnout.max())

# print(colormap(5.0))

colormap

unemployment_dict = runoff.set_index('ward')['Turnout']

unemployment_dict[12]



m = folium.Map(
    location=[41.884510, -87.630232],
    tiles='CartoDB positron',
    zoom_start=10
)

folium.Choropleth(
    geo_data=wards,
    data=runoff,
    columns=['ward', 'Turnout'],
    key_on='feature.properties.ward',
    fill_color='YlGn',
).add_to(m)











