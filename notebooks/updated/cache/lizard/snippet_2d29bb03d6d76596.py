def serialize_array(array, domain=(0, 1), fmt='png', quality=70):
    normalized = _normalize_array(array, domain=domain)
    return _serialize_normalized_array(normalized, fmt=fmt, quality=quality)