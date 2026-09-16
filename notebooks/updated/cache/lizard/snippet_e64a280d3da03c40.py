def equals(self, that, include_ref=False, fref=None):
    if not include_ref:
        return self == that
    if include_ref and self != that:
        return False
    if include_ref and fref is None:
        fref = WDBaseDataType.refs_equal
    return fref(self, that)