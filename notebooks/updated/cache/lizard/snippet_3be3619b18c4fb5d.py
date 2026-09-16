def _set_lookup_prop(self, result_data):
    if self._lookup_prop:
        return
    if result_data.get('id'):
        self._lookup_prop = 'id'
    elif result_data.get('title'):
        self._lookup_prop = 'name'
    else:
        return
    logger.debug('Setting lookup method for xunit to `%s`', self._lookup_prop)