def stream(self, code):
    self._say('Streaming code.')
    if type(code) in [str, text_type]:
        code = code.split('\n')
    self._parse('stream()', code)