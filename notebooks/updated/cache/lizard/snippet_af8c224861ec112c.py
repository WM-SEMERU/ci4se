def get_affected_box(self, src):
    mag = src.get_min_max_mag()[1]
    maxdist = self(src.tectonic_region_type, mag)
    bbox = get_bounding_box(src, maxdist)
    return fix_lon(bbox[0]), bbox[1], fix_lon(bbox[2]), bbox[3]