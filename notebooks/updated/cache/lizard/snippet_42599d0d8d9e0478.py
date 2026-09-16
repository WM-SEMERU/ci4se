def setDebug(self, flag=True):
    if flag:
        self.setDebugActions(_defaultStartDebugAction,
            _defaultSuccessDebugAction, _defaultExceptionDebugAction)
    else:
        self.debug = False
    return self