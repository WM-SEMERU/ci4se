def find(self, vName):
    refNum = _C.VSfind(self._hdf_inst._id, vName)
    _checkErr('find', refNum, 'cannot find vdata %s' % vName)
    return refNum