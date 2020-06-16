import folium

folium_map=folium.Map(location=[19.07890,34.56784521],zoom_start=5,tiles="CartoDB dark_matter")
'''More tiles are
openstreetmap
Mapbox Bright
stamenterrain
stamentonner
stamenwatercolor
cartodbpositron
'''

folium_map.save("map.html")
