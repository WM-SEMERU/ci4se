def _set_zone_name(self, zoneid, name):
    zoneid -= 1
    data = {'_set_zone_name': 'Set Name', 'select_zone': str(zoneid),
        'zone_name': name}
    self._controller.post(data)