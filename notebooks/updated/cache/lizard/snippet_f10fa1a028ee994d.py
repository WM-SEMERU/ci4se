def initialize_zones(self):
    zone_list = self.location_info.get('zone_list', {'main': True})
    for zone_id in zone_list:
        if zone_list[zone_id]:
            self.zones[zone_id] = Zone(self, zone_id=zone_id)
        else:
            _LOGGER.debug('Ignoring zone: %s', zone_id)