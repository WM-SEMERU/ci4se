def getElementsByTagName(self, tagName, root='root'):
    root, isFromRoot = self._handleRootArg(root)
    elements = []
    if isFromRoot is True and root.tagName == tagName:
        elements.append(root)
    getElementsByTagName = self.getElementsByTagName
    for child in root.children:
        if child.tagName == tagName:
            elements.append(child)
        elements += getElementsByTagName(tagName, child)
    return TagCollection(elements)