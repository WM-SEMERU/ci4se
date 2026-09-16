def getElementsByAttr(self, attrName, attrValue, root='root', useIndex=True):
    root, isFromRoot = self._handleRootArg(root)
    if useIndex is True and attrName in self._otherAttributeIndexes:
        elements = self._otherAttributeIndexes[attrName].get(attrValue, [])
        if isFromRoot is False:
            _hasTagInParentLine = self._hasTagInParentLine
            elements = [x for x in elements if _hasTagInParentLine(x, root)]
        return TagCollection(elements)
    return AdvancedHTMLParser.getElementsByAttr(self, attrName, attrValue, root
        )