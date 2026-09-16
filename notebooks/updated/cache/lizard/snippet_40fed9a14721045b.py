def context(self):
    ret = libxml2mod.xmlXPathParserGetContext(self._o)
    if ret is None:
        raise xpathError('xmlXPathParserGetContext() failed')
    __tmp = xpathContext(_obj=ret)
    return __tmp