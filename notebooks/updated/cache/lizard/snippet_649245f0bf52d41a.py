def overlap_bbox_and_point(bbox, xp, yp):
    cx, cy = get_midpoint(bbox)
    dir_x = np.sign(cx - xp)
    dir_y = np.sign(cy - yp)
    if dir_x == -1:
        dx = xp - bbox.xmax
    elif dir_x == 1:
        dx = xp - bbox.xmin
    else:
        dx = 0
    if dir_y == -1:
        dy = yp - bbox.ymax
    elif dir_y == 1:
        dy = yp - bbox.ymin
    else:
        dy = 0
    return dx, dy