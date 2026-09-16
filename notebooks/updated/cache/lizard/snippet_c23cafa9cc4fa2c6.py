def addVarBinds(self, *varBinds):
    debug.logger & debug.FLAG_MIB and debug.logger(
        'additional var-binds: %r' % (varBinds,))
    if self._state & self.ST_CLEAN:
        raise SmiError('%s object is already sealed' % self.__class__.__name__)
    else:
        self._additionalVarBinds.extend(varBinds)
    return self