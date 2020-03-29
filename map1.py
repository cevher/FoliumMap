import folium

map = folium.Map(location=[30.58,-99.09], zoom_start=6)


fg = folium.FeatureGroup(name="My Map")
cordinates = [[38.2, -99.1], [37.2, -97.1], [35.2, -95.1]]

for cordinate in cordinates:
    fg.add_child(folium.Marker(location=cordinate, popup="Hi There", icon=folium.Icon(color='red')))

map.add_child(fg)
map.save("Map1.html")