def parse(self, input, **kwargs):
    return self._parser.parse(input, lexer=self._lexer, **kwargs)