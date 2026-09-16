def _point_in_bbox(point, bounds):
    return not (point['coordinates'][1] < bounds[0] or point['coordinates']
        [1] > bounds[2] or point['coordinates'][0] < bounds[1] or point[
        'coordinates'][0] > bounds[3])