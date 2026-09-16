def processFrame(frame):
    global current_yaw_delta_from_depth
    y = int(old_div(video_height, 2))
    rowstart = y * video_width
    v = 0
    v_max = 0
    v_max_pos = 0
    v_min = 0
    v_min_pos = 0
    dv = 0
    dv_max = 0
    dv_max_pos = 0
    dv_max_sign = 0
    d2v = 0
    d2v_max = 0
    d2v_max_pos = 0
    d2v_max_sign = 0
    for x in range(0, video_width):
        nv = frame[(rowstart + x) * 4 + 3]
        ndv = nv - v
        nd2v = ndv - dv
        if nv > v_max or x == 0:
            v_max = nv
            v_max_pos = x
        if nv < v_min or x == 0:
            v_min = nv
            v_min_pos = x
        if abs(ndv) > dv_max or x == 1:
            dv_max = abs(ndv)
            dv_max_pos = x
            dv_max_sign = ndv > 0
        if abs(nd2v) > d2v_max or x == 2:
            d2v_max = abs(nd2v)
            d2v_max_pos = x
            d2v_max_sign = nd2v > 0
        d2v = nd2v
        dv = ndv
        v = nv
    logger.info('d2v, dv, v: ' + str(d2v) + ', ' + str(dv) + ', ' + str(v))
    if dv_max_sign:
        edge = old_div(video_width, 4)
    else:
        edge = 3 * video_width / 4
    if d2v_max > 8:
        current_yaw_delta_from_depth = old_div(float(d2v_max_pos - edge),
            video_width)
    elif v_max < 255:
        current_yaw_delta_from_depth = old_div(float(v_max_pos), video_width
            ) - 0.5
    elif current_yaw_delta_from_depth < 0:
        current_yaw_delta_from_depth = -1
    else:
        current_yaw_delta_from_depth = 1