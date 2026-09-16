def project(vec1, vec2):
    if isinstance(vec1, Vector3) and isinstance(vec2, Vector3) or isinstance(
        vec1, Vector4) and isinstance(vec2, Vector4):
        return dot(vec1, vec2) / vec2.length() * vec2.normalize_copy()
    else:
        raise ValueError('vec1 and vec2 must be Vector3 or Vector4 objects.')