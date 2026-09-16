def getAttributeValue(self, namespaceURI, localName):
    if self.hasAttribute(namespaceURI, localName):
        attr = self.node.getAttributeNodeNS(namespaceURI, localName)
        return attr.value
    return None