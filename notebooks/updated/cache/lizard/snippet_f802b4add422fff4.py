def _convert_point(cls, feature):
    lon, lat = feature['geometry']['coordinates']
    popup = feature['properties'].get('name', '')
    return cls(lat, lon)