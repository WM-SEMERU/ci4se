def validateOneElement(self, ctxt, elem):
    if ctxt is None:
        ctxt__o = None
    else:
        ctxt__o = ctxt._o
    if elem is None:
        elem__o = None
    else:
        elem__o = elem._o
    ret = libxml2mod.xmlValidateOneElement(ctxt__o, self._o, elem__o)
    return ret