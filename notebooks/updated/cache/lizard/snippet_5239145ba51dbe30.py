def set_muted(self, status):
    self._group['muted'] = status
    yield from self._server.group_mute(self.identifier, status)
    _LOGGER.info('set muted to %s on %s', status, self.friendly_name)