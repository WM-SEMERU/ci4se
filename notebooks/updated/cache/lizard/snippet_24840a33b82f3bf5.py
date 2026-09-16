def deactivate_boost_by_name(self, zone_name):
    zone = self.get_zone(zone_name)
    if zone is None:
        raise RuntimeError('Unknown zone')
    return self.deactivate_boost_by_id(zone['zoneId'])