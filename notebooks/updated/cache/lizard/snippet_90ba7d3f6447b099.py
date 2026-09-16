def _get_split_zone(zone, _conn, private_zone):
    for _zone in _conn.get_zones():
        if _zone.name == zone:
            _private_zone = True if _zone.config['PrivateZone'].lower(
                ) == 'true' else False
            if _private_zone == private_zone:
                return _zone
    return False