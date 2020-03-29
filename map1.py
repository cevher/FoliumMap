import folium
import pandas as pd 

# reading and processing data from text file
data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
long = list(data["LON"])
markers = list(data["NAME"])


# Creating base map and feature group
map = folium.Map(location=[30.58,-99.09], zoom_start=4)
fg = folium.FeatureGroup(name="My Map")


#iterating through and adding data to map
for lt,ln,mrk in zip(lat,long,markers):
    fg.add_child(folium.Marker(location=[lt,ln], popup=mrk, icon=folium.Icon(color='red')))

map.add_child(fg)
map.save("Map1.html")