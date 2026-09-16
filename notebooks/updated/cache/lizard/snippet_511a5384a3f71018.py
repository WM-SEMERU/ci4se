def newDocPI(self, name, content):
    ret = libxml2mod.xmlNewDocPI(self._o, name, content)
    if ret is None:
        raise treeError('xmlNewDocPI() failed')
    __tmp = xmlNode(_obj=ret)
    return __tmp