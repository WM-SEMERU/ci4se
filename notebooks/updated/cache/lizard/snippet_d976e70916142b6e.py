def procedures(self, *a, **kw):
    fut = self._run_operation(self._impl.procedures, *a, **kw)
    return fut