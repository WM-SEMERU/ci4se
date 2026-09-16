def quantize_datetime(dt, resolution=None):
    resolution = int(resolution or 6)
    if hasattr(dt, 'timetuple'):
        dt = dt.timetuple()
    if isinstance(dt, time.struct_time):
        dt = list(dt)[:6]
        dt += [int((dt[5] - int(dt[5])) * 1000000)]
        dt[5] = int(dt[5])
        return datetime.datetime(*(dt[:resolution] + [1] * max(3 -
            resolution, 0)))
    if isinstance(dt, tuple) and len(dt) <= 9 and all(isinstance(val, (
        float, int)) for val in dt):
        dt = list(dt) + [0] * max(6 - len(dt), 0)
        if len(dt) == 6 and isinstance(dt[5], float):
            dt = list(dt) + [1000000 * (dt[5] - int(dt[5]))]
            dt[5] = int(dt[5])
        dt = tuple(int(val) for val in dt)
        return datetime.datetime(*(dt[:resolution] + [1] * max(resolution -
            3, 0)))
    return [quantize_datetime(value) for value in dt]