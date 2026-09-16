def getFirstElementCustomFilter(self, filterFunc, root='root'):
    root, isFromRoot = self._handleRootArg(root)
    elements = []
    if isFromRoot is True and filterFunc(root) is True:
        return root
    getFirstElementCustomFilter = self.getFirstElementCustomFilter
    for child in root.children:
        if filterFunc(child) is True:
            return child
        subRet = getFirstElementCustomFilter(filterFunc, child)
        if subRet:
            return subRet
    return None