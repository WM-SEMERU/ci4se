def _handle_unsubscribed(self, *args, chanId=None, **kwargs):
    log.debug('_handle_unsubscribed: %s - %s', chanId, kwargs)
    try:
        self.channels.pop(chanId)
    except KeyError:
        raise NotRegisteredError()
    try:
        self._heartbeats.pop(chanId)
    except KeyError:
        pass
    try:
        self._late_heartbeats.pop(chanId)
    except KeyError:
        pass