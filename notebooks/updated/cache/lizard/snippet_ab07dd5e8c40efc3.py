def _on_stream_update(self, data):
    self._streams[data.get('id')].update(data.get('stream'))
    _LOGGER.info('stream %s updated', self._streams[data.get('id')].
        friendly_name)
    for group in self._groups.values():
        if group.stream == data.get('id'):
            group.callback()