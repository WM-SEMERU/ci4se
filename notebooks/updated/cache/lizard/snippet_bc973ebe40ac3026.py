def setfields(self, *fldNames):
    _checkErr('setfields', _C.VSsetfields(self._id, ','.join(fldNames)),
        'cannot execute')
    self._setfields = fldNames