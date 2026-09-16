def get_info(self):
    info = {'name': self.name if self.name else '<no name>', 'path': self.
        name if self.name else '<no name>', 'field_type': type(self).
        __name__, 'value': {'raw': repr(self._current_value), 'rendered': {
        'base64': b64encode(self._current_rendered.tobytes()).decode(),
        'length_in_bits': len(self._current_rendered), 'length_in_bytes':
        len(self._current_rendered.tobytes())}}, 'mutation': {
        'total_number': self._num_mutations, 'current_index': self.
        _current_index, 'mutating': self._mutating(), 'fuzzable': self.
        _fuzzable}}
    return info