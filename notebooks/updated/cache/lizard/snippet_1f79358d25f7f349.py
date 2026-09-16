def _internal_sub(self, other, method=None):
    if hasattr(other, 'datatype'):
        if other.datatype == self.datatype:
            oval = other.value
        else:
            oval = int(other.value)
    else:
        oval = int(other)
    if method == 'rsub':
        rtn_val = oval - self.value
    else:
        rtn_val = self.value - oval
    return XsdInteger(rtn_val)