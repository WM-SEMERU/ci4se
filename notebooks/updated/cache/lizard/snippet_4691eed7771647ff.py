def getcompress(self):
    status, comp_type, value, v2, v3, v4, v5 = _C._SDgetcompress(self._id)
    _checkErr('getcompress', status, 'no compression')
    if comp_type == SDC.COMP_NONE:
        return comp_type,
    elif comp_type == SDC.COMP_SZIP:
        return comp_type, value, v2, v3, v4, v5
    else:
        return comp_type, value