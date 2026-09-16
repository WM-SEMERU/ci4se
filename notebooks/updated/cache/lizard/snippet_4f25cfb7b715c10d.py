def reftoindex(self, sds_ref):
    sds_idx = _C.SDreftoindex(self._id, sds_ref)
    _checkErr('reftoindex', sds_idx, 'illegal SDS ref number')
    return sds_idx