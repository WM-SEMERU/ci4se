def listGetRawString(self, doc, inLine):
    if doc is None:
        doc__o = None
    else:
        doc__o = doc._o
    ret = libxml2mod.xmlNodeListGetRawString(doc__o, self._o, inLine)
    return ret