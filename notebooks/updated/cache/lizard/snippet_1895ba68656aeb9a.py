def to_utm_bbox(bbox):
    if CRS.is_utm(bbox.crs):
        return bbox
    lng, lat = bbox.middle
    utm_crs = get_utm_crs(lng, lat, source_crs=bbox.crs)
    return bbox.transform(utm_crs)