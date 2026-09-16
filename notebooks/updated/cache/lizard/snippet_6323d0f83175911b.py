def _AugAssign(self, t):
    self._fill()
    self._dispatch(t.node)
    self._write(' ' + t.op + ' ')
    self._dispatch(t.expr)
    if not self._do_indent:
        self._write(';')