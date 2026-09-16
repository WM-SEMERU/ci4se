def haversine(px, py, r=r_mm):
    lat1, lon1 = px
    lat2, lon2 = py
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(
        dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    return c * r