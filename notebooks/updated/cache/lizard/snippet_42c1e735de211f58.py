def _add_zone(self, zone, name='', status=Zone.CLEAR, expander=False):
    if not zone in self._zones:
        self._zones[zone] = Zone(zone=zone, name=name, status=None,
            expander=expander)
    self._update_zone(zone, status=status)