import folium
import pandas as pd 

# reading and processing data from text file
data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
long = list(data["LON"])
markers = list(data["NAME"])
elev = list(data["ELEV"])


# function to create random color producer
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <=elevation < 3000:
        return 'orange'
    else:
        return 'red'

# Creating base map and feature group
map = folium.Map(location=[30.58,-99.09], zoom_start=4)
fg = folium.FeatureGroup(name="My Map")


#iterating through and adding data to map
for lt,ln,mrk, el in zip(lat,long,markers, elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius= 6, popup=mrk+ '\n'+str(el), 
        fill_color=color_producer(el), color='grey', fill_opacity=0.7))

## Adding second feature group of population and change color based on hte population 
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),
        style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 
        else 'orange' if 10000000 <= x['properties']['POP2005']< 20000000 else 'red'}))

map.add_child(fg)
map.add_child(fgp)

###Adding layer control to final map
map.add_child(folium.LayerControl())

## Saving the map to the fiel
map.save("Map1.html")