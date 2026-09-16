def addSibling(self, elem):
    if elem is None:
        elem__o = None
    else:
        elem__o = elem._o
    ret = libxml2mod.xmlAddSibling(self._o, elem__o)
    if ret is None:
        raise treeError('xmlAddSibling() failed')
    __tmp = xmlNode(_obj=ret)
    return __tmp