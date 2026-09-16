def fault_zone(self, zone, simulate_wire_problem=False):
    if isinstance(zone, tuple):
        expander_idx, channel = zone
        zone = self._zonetracker.expander_to_zone(expander_idx, channel)
    status = 2 if simulate_wire_problem else 1
    self.send('L{0:02}{1}\r'.format(zone, status))