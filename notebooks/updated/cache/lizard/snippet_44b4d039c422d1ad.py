def clean_errors(self):
    self._vim.eval('clearmatches()')
    self._errors = []
    self._matches = []
    self._vim.current.buffer.vars['ensime_notes'] = []