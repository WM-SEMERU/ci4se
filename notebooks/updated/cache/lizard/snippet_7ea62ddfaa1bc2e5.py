def robust_int(v):
    if isinstance(v, int):
        return v
    if isinstance(v, float):
        return int(v)
    v = str(v).replace(',', '')
    if not v:
        return None
    return int(v)