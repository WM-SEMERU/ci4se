def get_contained_extras(marker):
    if not marker:
        return set()
    extras = set()
    marker = _ensure_marker(marker)
    _markers_collect_extras(marker._markers, extras)
    return extras