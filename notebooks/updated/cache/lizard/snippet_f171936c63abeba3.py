def xpathNextFollowingSibling(self, ctxt):
    if ctxt is None:
        ctxt__o = None
    else:
        ctxt__o = ctxt._o
    ret = libxml2mod.xmlXPathNextFollowingSibling(ctxt__o, self._o)
    if ret is None:
        raise xpathError('xmlXPathNextFollowingSibling() failed')
    __tmp = xmlNode(_obj=ret)
    return __tmp