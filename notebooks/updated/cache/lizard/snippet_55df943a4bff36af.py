def importNode(self, document, node, deep=0):
    nodetype = node.nodeType
    if nodetype in (node.DOCUMENT_NODE, node.DOCUMENT_TYPE_NODE):
        raise DOMException('Illegal node type for importNode')
    if nodetype == node.ENTITY_REFERENCE_NODE:
        deep = 0
    clone = node.cloneNode(deep)
    self._setOwnerDoc(document, clone)
    clone.__imported__ = 1
    return clone