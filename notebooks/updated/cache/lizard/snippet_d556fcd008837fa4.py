def _update_zone(self, zone, status=None):
    if not zone in self._zones:
        raise IndexError('Zone does not exist and cannot be updated: %d', zone)
    old_status = self._zones[zone].status
    if status is None:
        status = old_status
    self._zones[zone].status = status
    self._zones[zone].timestamp = time.time()
    if status == Zone.CLEAR:
        if zone in self._zones_faulted:
            self._zones_faulted.remove(zone)
        self.on_restore(zone=zone)
    elif old_status != status and status is not None:
        self.on_fault(zone=zone)