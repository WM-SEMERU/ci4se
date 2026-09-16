def _get_boxes(pos, size=None, margin=0, keep_aspect_ratio=True):
    pos = np.asarray(pos, dtype=np.float64)
    x, y = pos.T
    x = x[:, (np.newaxis)]
    y = y[:, (np.newaxis)]
    w, h = size if size is not None else _get_box_size(x, y, margin=margin)
    x0, y0 = x - w, y - h
    x1, y1 = x + w, y + h
    x0min, y0min, x1max, y1max = x0.min(), y0.min(), x1.max(), y1.max()
    if not keep_aspect_ratio:
        b = x0min, y0min, x1max, y1max
    else:
        dx = x1max - x0min
        dy = y1max - y0min
        if dx > dy:
            b = x0min, (y1max + y0min) / 2.0 - dx / 2.0, x1max, (y1max + y0min
                ) / 2.0 + dx / 2.0
        else:
            b = (x1max + x0min) / 2.0 - dy / 2.0, y0min, (x1max + x0min
                ) / 2.0 + dy / 2.0, y1max
    r = Range(from_bounds=b, to_bounds=(-1, -1, 1, 1))
    return np.c_[r.apply(np.c_[x0, y0]), r.apply(np.c_[x1, y1])]