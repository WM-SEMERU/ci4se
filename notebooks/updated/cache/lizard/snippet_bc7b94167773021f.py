def lookup_zone_exception(self, callsign, timestamp=datetime.utcnow().
    replace(tzinfo=UTC)):
    callsign = callsign.strip().upper()
    if self._lookuptype == 'clublogxml':
        return self._check_zone_exception_for_date(callsign, timestamp,
            self._zone_exceptions, self._zone_exceptions_index)
    elif self._lookuptype == 'redis':
        data_dict, index = self._get_dicts_from_redis('_zone_ex_',
            '_zone_ex_index_', self._redis_prefix, callsign)
        return self._check_zone_exception_for_date(callsign, timestamp,
            data_dict, index)
    raise KeyError