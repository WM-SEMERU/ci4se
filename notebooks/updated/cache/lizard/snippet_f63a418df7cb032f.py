def _process_incoming_presence(self, stanza_obj):
    self._logger.debug('incoming presence: %r', stanza_obj)
    stanza_obj = self.service_inbound_presence_filter.filter(stanza_obj)
    if stanza_obj is None:
        self._logger.debug('incoming presence dropped by service filter chain')
        return
    stanza_obj = self.app_inbound_presence_filter.filter(stanza_obj)
    if stanza_obj is None:
        self._logger.debug(
            'incoming presence dropped by application filter chain')
        return
    self.on_presence_received(stanza_obj)