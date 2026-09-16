def validateRoot(self, ctxt):
    if ctxt is None:
        ctxt__o = None
    else:
        ctxt__o = ctxt._o
    ret = libxml2mod.xmlValidateRoot(ctxt__o, self._o)
    return ret