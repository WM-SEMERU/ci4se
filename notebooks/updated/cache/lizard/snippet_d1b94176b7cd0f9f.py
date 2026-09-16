def _skip_saveframe(self, lexer):
    token = ''
    while token != 'save_':
        token = next(lexer)