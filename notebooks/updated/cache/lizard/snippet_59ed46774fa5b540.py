def setdatastrs(self, label, unit, format, coord_sys):
    status = _C.SDsetdatastrs(self._id, label, unit, format, coord_sys)
    _checkErr('setdatastrs', status, 'cannot execute')