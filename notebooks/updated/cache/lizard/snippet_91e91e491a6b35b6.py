def bbox_flip(bbox, d, rows, cols):
    if d == 0:
        bbox = bbox_vflip(bbox, rows, cols)
    elif d == 1:
        bbox = bbox_hflip(bbox, rows, cols)
    elif d == -1:
        bbox = bbox_hflip(bbox, rows, cols)
        bbox = bbox_vflip(bbox, rows, cols)
    else:
        raise ValueError('Invalid d value {}. Valid values are -1, 0 and 1'
            .format(d))
    return bbox