def validateDtdFinal(self, ctxt):
    if ctxt is None:
        ctxt__o = None
    else:
        ctxt__o = ctxt._o
    ret = libxml2mod.xmlValidateDtdFinal(ctxt__o, self._o)
    return ret