def get_center_from_json(cls, data):
    center_lat = None
    center_lon = None
    center = data.get('center')
    if isinstance(center, dict):
        center_lat = center.get('lat')
        center_lon = center.get('lon')
        if center_lat is None or center_lon is None:
            raise ValueError('Unable to get lat or lon of way center.')
        center_lat = Decimal(center_lat)
        center_lon = Decimal(center_lon)
    return center_lat, center_lon