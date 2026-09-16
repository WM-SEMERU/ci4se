def _filter_optional_keys(self, data):
    for filter_key, filter_value in (self._optional_filters or {}).items():
        data_value = data.get(filter_key)
        LOG.debug('optional keys filter %s: %s (%s)', filter_key,
            filter_value, data_value)
        if data_value is None or data_value != filter_value:
            LOG.debug('optional keys filter rejecting %s: %s (%s)',
                filter_key, filter_value, data_value)
            return False
    return True