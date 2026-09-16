def setRootElement(self, root):
    if root is None:
        root__o = None
    else:
        root__o = root._o
    ret = libxml2mod.xmlDocSetRootElement(self._o, root__o)
    if ret is None:
        return None
    __tmp = xmlNode(_obj=ret)
    return __tmp