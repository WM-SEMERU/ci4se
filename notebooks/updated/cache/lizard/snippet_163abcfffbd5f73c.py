def check_bbox(bbox):
    for name, value in zip(['x_min', 'y_min', 'x_max', 'y_max'], bbox[:4]):
        if not 0 <= value <= 1:
            raise ValueError(
                'Expected {name} for bbox {bbox} to be in the range [0.0, 1.0], got {value}.'
                .format(bbox=bbox, name=name, value=value))
    x_min, y_min, x_max, y_max = bbox[:4]
    if x_max <= x_min:
        raise ValueError(
            'x_max is less than or equal to x_min for bbox {bbox}.'.format(
            bbox=bbox))
    if y_max <= y_min:
        raise ValueError(
            'y_max is less than or equal to y_min for bbox {bbox}.'.format(
            bbox=bbox))