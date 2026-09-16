def get_traceback(self):
    from pypy.interpreter.pytraceback import PyTraceback
    tb = self._application_traceback
    if tb is not None and isinstance(tb, PyTraceback):
        tb.frame.mark_as_escaped()
    return tb