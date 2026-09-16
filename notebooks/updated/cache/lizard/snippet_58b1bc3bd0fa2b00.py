def append_to_arg_count(self, data):
    assert data in '-0123456789'
    current = self._arg
    if data == '-':
        assert current is None or current == '-'
        result = data
    elif current is None:
        result = data
    else:
        result = '%s%s' % (current, data)
    self.input_processor.arg = result