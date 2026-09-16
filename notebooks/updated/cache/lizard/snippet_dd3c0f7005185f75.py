def get_location_metres(original_location, dNorth, dEast):
    earth_radius = 6378137.0
    dLat = dNorth / earth_radius
    dLon = dEast / (earth_radius * math.cos(math.pi * original_location.lat /
        180))
    newlat = original_location.lat + dLat * 180 / math.pi
    newlon = original_location.lon + dLon * 180 / math.pi
    return LocationGlobal(newlat, newlon, original_location.alt)