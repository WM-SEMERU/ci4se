def _store_cached_zone_variable(self, zone_id, name, value):
    zone_state = self._zone_state.setdefault(zone_id, {})
    name = name.lower()
    zone_state[name] = value
    logger.debug('Zone Cache store %s.%s = %s', zone_id.device_str(), name,
        value)
    for callback in self._zone_callbacks:
        callback(zone_id, name, value)