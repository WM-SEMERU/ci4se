def activate_boost_by_name(self, zone_name, target_temperature, num_hours=1):
    zone = self.get_zone(zone_name)
    if zone is None:
        raise RuntimeError('Unknown zone')
    return self.activate_boost_by_id(zone['zoneId'], target_temperature,
        num_hours)