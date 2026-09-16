def pixel_to_geo(pixel, level):
    pixel_x = pixel[0]
    pixel_y = pixel[1]
    map_size = float(TileSystem.map_size(level))
    x = TileSystem.clip(pixel_x, (0, map_size - 1)) / map_size - 0.5
    y = 0.5 - TileSystem.clip(pixel_y, (0, map_size - 1)) / map_size
    lat = 90 - 360 * atan(exp(-y * 2 * pi)) / pi
    lon = 360 * x
    return round(lat, 6), round(lon, 6)