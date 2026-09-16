def _safe_get(mapping, key, default=None):
    try:
        return mapping.get(key, default)
    except AttributeError:
        return default