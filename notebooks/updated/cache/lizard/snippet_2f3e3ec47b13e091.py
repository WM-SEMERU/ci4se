def newDocRawNode(self, ns, name, content):
    if ns is None:
        ns__o = None
    else:
        ns__o = ns._o
    ret = libxml2mod.xmlNewDocRawNode(self._o, ns__o, name, content)
    if ret is None:
        raise treeError('xmlNewDocRawNode() failed')
    __tmp = xmlNode(_obj=ret)
    return __tmp