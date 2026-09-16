def getExtensionList(self, extensions):
    basicList = extensions.split(',')
    extensionList = []
    for ext in basicList:
        if ext == MapConstants.placeholderNoExtensionFilter:
            extensionList.append('')
        elif ext != '':
            extWithDot = ext if ext.startswith('.') else '.' + ext
            extensionList.append(extWithDot)
    return list(set(extensionList))