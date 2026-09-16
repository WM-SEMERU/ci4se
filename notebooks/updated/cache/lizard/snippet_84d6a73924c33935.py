def _set_hwxy_attrs(attr):
    bbox = attr['bbox']
    attr['x0'] = bbox[0]
    attr['x1'] = bbox[2]
    attr['y0'] = bbox[1]
    attr['y1'] = bbox[3]
    attr['height'] = attr['y1'] - attr['y0']
    attr['width'] = attr['x1'] - attr['x0']
    return attr