def delete_record(self, identifier=None, rtype=None, name=None, content=None):
    version = None
    ret = False
    opts = {}
    if identifier is not None:
        opts['id'] = identifier
    else:
        if not rtype and not name and not content:
            raise ValueError(
                'Error, at least one parameter from type, name or content must be set'
                )
        if rtype:
            opts['type'] = rtype.upper()
        if name:
            opts['name'] = self._relative_name(name)
        if content:
            opts['value'] = self._txt_encode(content) if opts['type'
                ] == 'TXT' else content
    records = self._api.domain.zone.record.list(self._api_key, self.
        _zone_id, 0, opts)
    if records:
        try:
            version = self._api.domain.zone.version.new(self._api_key, self
                ._zone_id)
            for record in records:
                del record['id']
                self._api.domain.zone.record.delete(self._api_key, self.
                    _zone_id, version, record)
            self._api.domain.zone.version.set(self._api_key, self._zone_id,
                version)
            ret = True
        finally:
            if not ret and version is not None:
                self._api.domain.zone.version.delete(self._api_key, self.
                    _zone_id, version)
    LOGGER.debug('delete_record: %s', ret)
    return ret