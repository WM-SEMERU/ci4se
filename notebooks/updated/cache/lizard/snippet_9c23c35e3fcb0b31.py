def spatial_clip(catalog, corners, mindepth=None, maxdepth=None):
    cat_out = catalog.copy()
    if mindepth is not None:
        for event in cat_out:
            try:
                origin = _get_origin(event)
            except IOError:
                continue
            if origin.depth < mindepth * 1000:
                cat_out.events.remove(event)
    if maxdepth is not None:
        for event in cat_out:
            try:
                origin = _get_origin(event)
            except IOError:
                continue
            if origin.depth > maxdepth * 1000:
                cat_out.events.remove(event)
    for event in cat_out:
        try:
            origin = _get_origin(event)
        except IOError:
            continue
        if not corners.contains_point((origin.latitude, origin.longitude)):
            cat_out.events.remove(event)
    return cat_out