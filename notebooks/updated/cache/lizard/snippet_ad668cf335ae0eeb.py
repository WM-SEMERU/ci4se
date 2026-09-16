def uid(self):
    if self._uid is not None:
        return self._uid
    self._parse_zone_group_state()
    return self._uid