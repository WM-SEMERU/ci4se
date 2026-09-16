def coord_to_pixel(self, lat, lon, width, ground_width, lat2, lon2):
    pixel_width = ground_width / float(width)
    if lat is None or lon is None or lat2 is None or lon2 is None:
        return 0, 0
    dx = mp_util.gps_distance(lat, lon, lat, lon2)
    if lon2 < lon:
        dx = -dx
    dy = mp_util.gps_distance(lat, lon, lat2, lon)
    if lat2 > lat:
        dy = -dy
    dx /= pixel_width
    dy /= pixel_width
    return int(dx), int(dy)