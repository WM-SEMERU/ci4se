def bbox_to_dimensions(bbox, resolution):
    utm_bbox = to_utm_bbox(bbox)
    east1, north1 = utm_bbox.lower_left
    east2, north2 = utm_bbox.upper_right
    resx, resy = resolution if isinstance(resolution, tuple) else (resolution,
        resolution)
    return round(abs(east2 - east1) / resx), round(abs(north2 - north1) / resy)