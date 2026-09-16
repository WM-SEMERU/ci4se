def xpathNextChild(self, ctxt):
    if ctxt is None:
        ctxt__o = None
    else:
        ctxt__o = ctxt._o
    ret = libxml2mod.xmlXPathNextChild(ctxt__o, self._o)
    if ret is None:
        raise xpathError('xmlXPathNextChild() failed')
    __tmp = xmlNode(_obj=ret)
    return __tmp