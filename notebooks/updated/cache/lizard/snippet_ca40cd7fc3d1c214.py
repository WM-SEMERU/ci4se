def validateNotationUse(self, ctxt, notationName):
    if ctxt is None:
        ctxt__o = None
    else:
        ctxt__o = ctxt._o
    ret = libxml2mod.xmlValidateNotationUse(ctxt__o, self._o, notationName)
    return ret