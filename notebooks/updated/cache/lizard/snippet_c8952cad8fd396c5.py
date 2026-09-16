def writeMibObjects(self, *varBinds, **context):
    if 'cbFun' not in context:
        context['cbFun'] = self._defaultErrorHandler
    self.flipFlopFsm(self.FSM_WRITE_VAR, *varBinds, **context)