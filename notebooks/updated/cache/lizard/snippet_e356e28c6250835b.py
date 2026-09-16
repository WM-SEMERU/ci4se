def set_zone_order(self, zone_ids):
    reordered_zones = []
    current_zone_ids = [z['id'] for z in self.my_osid_object_form._my_map[
        'zones']]
    if set(zone_ids) != set(current_zone_ids):
        raise IllegalState('zone_ids do not match existing zones')
    for zone_id in zone_ids:
        for current_zone in self.my_osid_object_form._my_map['zones']:
            if zone_id == current_zone['id']:
                reordered_zones.append(current_zone)
                break
    self.my_osid_object_form._my_map['zones'] = reordered_zones