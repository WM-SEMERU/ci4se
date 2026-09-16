def xpathNextNamespace(self, cur):
    if cur is None:
        cur__o = None
    else:
        cur__o = cur._o
    ret = libxml2mod.xmlXPathNextNamespace(self._o, cur__o)
    if ret is None:
        raise xpathError('xmlXPathNextNamespace() failed')
    __tmp = xmlNode(_obj=ret)
    return __tmp