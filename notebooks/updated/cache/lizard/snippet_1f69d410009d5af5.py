def lastElementChild(self):
    ret = libxml2mod.xmlLastElementChild(self._o)
    if ret is None:
        return None
    __tmp = xmlNode(_obj=ret)
    return __tmp