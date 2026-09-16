def setNsProp(self, ns, name, value):
    if ns is None:
        ns__o = None
    else:
        ns__o = ns._o
    ret = libxml2mod.xmlSetNsProp(self._o, ns__o, name, value)
    if ret is None:
        raise treeError('xmlSetNsProp() failed')
    __tmp = xmlAttr(_obj=ret)
    return __tmp