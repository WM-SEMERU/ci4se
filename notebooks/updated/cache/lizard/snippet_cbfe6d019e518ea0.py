def get_image_dimension(bbox, width=None, height=None):
    utm_bbox = to_utm_bbox(bbox)
    east1, north1 = utm_bbox.lower_left
    east2, north2 = utm_bbox.upper_right
    if isinstance(width, int):
        return round(width * abs(north2 - north1) / abs(east2 - east1))
    return round(height * abs(east2 - east1) / abs(north2 - north1))