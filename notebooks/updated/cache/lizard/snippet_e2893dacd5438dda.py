def isElement(self, node, name, nsuri=None):
    if node.nodeType != node.ELEMENT_NODE:
        return 0
    return node.localName == name and (nsuri is None or self.nsUriMatch(
        node.namespaceURI, nsuri))