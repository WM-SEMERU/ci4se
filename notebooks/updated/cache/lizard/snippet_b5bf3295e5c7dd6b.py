def _create_record(self, rtype, name, content):
    if not self._list_records(rtype, name, content):
        self._update_records([{}], {'type': rtype, 'hostname': self.
            _relative_name(name), 'destination': content, 'priority': self.
            _get_lexicon_option('priority')})
    LOGGER.debug('create_record: %s', True)
    return True