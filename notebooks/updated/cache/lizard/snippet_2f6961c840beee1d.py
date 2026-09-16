def pois_from_place(place, amenities=None):
    city = gdf_from_place(place)
    polygon = city['geometry'].iloc[0]
    return create_poi_gdf(polygon=polygon, amenities=amenities)