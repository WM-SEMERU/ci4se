def validatePushElement(self, doc, elem, qname):
    if doc is None:
        doc__o = None
    else:
        doc__o = doc._o
    if elem is None:
        elem__o = None
    else:
        elem__o = elem._o
    ret = libxml2mod.xmlValidatePushElement(self._o, doc__o, elem__o, qname)
    return ret