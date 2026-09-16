def contextDoc(self):
    ret = libxml2mod.xmlXPathGetContextDoc(self._o)
    if ret is None:
        raise xpathError('xmlXPathGetContextDoc() failed')
    __tmp = xmlDoc(_obj=ret)
    return __tmp