def string(self, name):
    self._assert_is_string(name)
    frame = self._next_frame()
    try:
        val = frame.decode('utf-8')
        self.results.__dict__[name] = val
    except UnicodeError as err:
        raise MessageParserError('Message contained invalid Unicode characters'
            ) from err
    return self