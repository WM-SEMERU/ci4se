def add(self, items):
    for item in items:
        if item.ack_id not in self._leased_messages:
            self._leased_messages[item.ack_id] = _LeasedMessage(added_time=
                time.time(), size=item.byte_size)
            self._bytes += item.byte_size
        else:
            _LOGGER.debug('Message %s is already lease managed', item.ack_id)