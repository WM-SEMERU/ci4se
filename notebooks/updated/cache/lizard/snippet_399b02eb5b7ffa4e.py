def get_zone_mode(self, zone_name):
    zone = self.get_zone(zone_name)
    if zone is None:
        raise RuntimeError('Unknown zone')
    return ZoneMode(zone['mode'])