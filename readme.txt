Hello!
This repo was created to accompany the follow presenation 
https://docs.google.com/presentation/d/1P-Wds4qSCyCruAC4ecL7omiHZKVD0UpGtYxqWijZAJw/edit?usp=sharing

This is a high level introduction into folium. This workshop is to help you get started with visualizing spatial data using folium, a python library for Leaflet. Run through data types examples and finish with analyzing the recent Chicago Mayoral Election. 

#Create Conda Virtual Env 
conda create --name folium -c conda-forge python=3.6 folium fiona jupyter basemap pandas shapely geopandas
conda activate folium
jupyter notebook
conda deactivate

Start with either:

Dealing with points >>>>>> Displaying Points with Folium.ipynb

Working with polygons >>>> Thematic Mapping.ipynb

