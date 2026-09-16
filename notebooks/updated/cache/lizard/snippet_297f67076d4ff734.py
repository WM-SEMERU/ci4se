def ast_str(self, indent=0):
    line = self.line or 0
    col = self.column or 0
    name = type(self).__name__
    spell = getattr(self, 'name', '[no spelling]')
    result = ' ({})'.format(self.result) if hasattr(self, 'result') else ''
    prefix = indent * '| '
    return '{}[{}:{}] {}{}: {}'.format(prefix, line, col, name, result, spell)