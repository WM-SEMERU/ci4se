def _getAttr(self, attr):
    meth = '_get_%s' % attr
    if not hasattr(self, meth):
        raise AttributeError("No getter for attribute '%s'." % attr)
    meth = getattr(self, meth)
    value = meth()
    return value