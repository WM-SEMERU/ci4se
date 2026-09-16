def _get_boolean(self, source, bitarray):
    raw_value = self._get_raw(source, bitarray)
    return {source['shortcut']: {'description': source.get('description'),
        'unit': source.get('unit', ''), 'value': True if raw_value else
        False, 'raw_value': raw_value}}