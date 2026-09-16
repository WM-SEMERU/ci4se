def contains_pyversion(marker):
    if not marker:
        return False
    marker = _ensure_marker(marker)
    return _markers_contains_pyversion(marker._markers)