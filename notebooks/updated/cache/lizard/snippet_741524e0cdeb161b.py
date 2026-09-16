def setcal(self, cal, cal_error, offset, offset_err, data_type):
    status = _C.SDsetcal(self._id, cal, cal_error, offset, offset_err,
        data_type)
    _checkErr('setcal', status, 'cannot execute')