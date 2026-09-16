def createElementNS(self, namespace, qname):
    document = self._getOwnerDocument()
    node = document.createElementNS(namespace, qname)
    return ElementProxy(self.sw, node)