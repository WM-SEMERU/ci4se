def validateRoot(self, doc):
    if doc is None:
        doc__o = None
    else:
        doc__o = doc._o
    ret = libxml2mod.xmlValidateRoot(self._o, doc__o)
    return ret